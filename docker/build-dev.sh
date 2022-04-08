#!/bin/bash

# Base build
cd base/ && \

docker build \
       --tag=cbointake \
       --no-cache . && \

cd .. && \

# stop old instances and remove the containers
# volumes are left intact
# images are left in storage in the event a rollback is needed
docker stop cbointake-django cbointake-celery cbointake-beat cbointake-poller
docker rm cbointake-django cbointake-celery cbointake-beat cbointake-poller

# Start web
docker run -it -d \
       --restart always \
       --env-file=.env \
       --link rabbitmq \
       --link broker \
       --name cbointake-django \
       -v /etc/ssl/certs:/etc/ssl/certs:ro \
       -v /etc/openldap/cacerts:/etc/openldap/cacerts:ro \
       -v cbointake-logs:/cbo-portal/log \
       -v cbointake-data:/cbo-portal/created \
       -p 8122:8000 \
       --entrypoint "/usr/local/bin/web-entrypoint.sh" \
       cbointake && \

# Start tasks
docker run -it -d \
       --restart always \
       --env-file=.env \
       --link rabbitmq \
       --link broker \
       --name cbointake-celery \
       -v cbointake-data:/cbo-portal/created \
       --entrypoint "/usr/local/bin/task-entrypoint.sh" \
       cbointake && \

# Start Polling Workers
# Start tasks
docker run -it -d \
       --restart always \
       --env-file=.env \
       --link rabbitmq \
       --link broker \
       --name cbointake-poller \
       --entrypoint "/usr/local/bin/poller-entrypoint.sh" \
       cbointake && \

# Start Scheduler
docker run -it -d \
       --restart always \
       --env-file=.env \
       --link rabbitmq \
       --link broker \
       --name cbointake-beat \
       --entrypoint "/usr/local/bin/scheduler-entrypoint.sh" \
       cbointake && \

# Copy out the static assets which were compiled during build
docker cp cbointake-django:/static.tgz ./ && \

# Transfer static assets to FE server
scp static.tgz 98.7.188.13:/usr/share/nginx/html/sre/cbo-intake/static && \
ssh 98.7.188.13 "cd /usr/share/nginx/html/sre/cbo-intake/static; tar xzf static.tgz; cd ..; chmod 755 static -R"

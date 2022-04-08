FROM alpine/git  as base

COPY id_rsa /tmp/id_rsa

RUN apk add --update git openssh-client && \
    chmod 600 /tmp/id_rsa && \
    eval $(ssh-agent) && \
    echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    ssh-add /tmp/id_rsa && \
    git clone --depth=1 -b port_request_manage git@git.netops.charter.com:brianmask/cbo-portal.git /cbo-portal && \
    rm -rf /tmp/id_rsa

FROM node:carbon-alpine as frontend

COPY --from=base /cbo-portal /cbo-portal

RUN cd /cbo-portal/frontend && \
    npm install && \
    npm run build

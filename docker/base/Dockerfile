FROM alpine/git  as base

COPY id_rsa /tmp/id_rsa

RUN apk add --update git openssh-client && \
    chmod 600 /tmp/id_rsa && \
    eval $(ssh-agent) && \
    echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    ssh-add /tmp/id_rsa && \
    git clone --depth=1 -b port_request_manage git@git.netops.charter.com:brianmask/cbo-portal.git /cbo-portal && \
    git clone --depth=1 -b master git@git.netops.charter.com:fsheiness/nso.git /nso && \
    rm -rf /tmp/id_rsa

FROM node:carbon-alpine as frontend

COPY --from=base /cbo-portal /cbo-portal

RUN cd /cbo-portal/frontend && \
    npm install && \
    npm run build

FROM python:3.6.9-slim-buster

COPY --from=base /cbo-portal /cbo-portal
COPY --from=base /nso /nso
COPY --from=frontend /cbo-portal/frontend/dist /cbo-portal/frontend/dist
COPY --from=frontend /cbo-portal/frontend/webpack-stats.json /cbo-portal/frontend/webpack-stats.json
COPY web-entrypoint.sh /usr/local/bin/
COPY task-entrypoint.sh /usr/local/bin/
COPY scheduler-entrypoint.sh /usr/local/bin/
COPY poller-entrypoint.sh /usr/local/bin/

RUN sed -i 's/main/main non-free/' /etc/apt/sources.list                    && \
    apt-get update && apt-get upgrade -y                                    && \
    apt-get install -y libmariadb-dev-compat build-essential libffi-dev        \
    libldap2-dev libsasl2-dev libsnmp-dev snmp-mibs-downloader              && \
    pip install --upgrade pip setuptools                                    && \
    pip install -r /cbo-portal/requirements.txt                             && \
    sed -i 's/mibs :/#mibs :/' /etc/snmp/snmp.conf                          && \
    cd /nso                                                                 && \
    pip install -e .                                                        && \
    apt-get autoremove -y build-essential                                   && \
    rm -rf /var/lib/apt/lists/*                                             && \
    mkdir -p /etc/openldap/cacerts                                          && \
    echo 'TLS_CACERTDIR /etc/openldap/cacerts' > /etc/ldap/ldap.conf        && \
    echo 'TLS_REQCERT allow' >> /etc/ldap/ldap.conf                         && \
    chmod a+rx /usr/local/bin/web-entrypoint.sh                             && \
    chmod a+rx /usr/local/bin/task-entrypoint.sh                            && \
    chmod a+rx /usr/local/bin/scheduler-entrypoint.sh                       && \
    chmod a+rx /usr/local/bin/poller-entrypoint.sh                          && \
    groupadd -r cbointake                                                   && \
    useradd -g cbointake -ms /bin/bash cbointake                            && \
    cd /cbo-portal                                                          && \
    mkdir log                                                               && \
    python manage.py collectstatic --no-input                               && \
    cd public                                                               && \
    tar czf static.tgz *                                                    && \
    chown -R cbointake:cbointake /cbo-portal                                && \
    mv static.tgz /

EXPOSE 8000
WORKDIR /cbo-portal

USER cbointake

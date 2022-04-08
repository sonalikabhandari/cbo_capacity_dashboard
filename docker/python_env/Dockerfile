FROM python:3.6.9-slim-buster

COPY requirements.txt /requirements.txt 

RUN sed -i 's/main/main non-free/' /etc/apt/sources.list                    && \
    apt-get update && apt-get upgrade -y                                    && \
    apt-get install -y libmariadb-dev-compat build-essential libffi-dev        \
    libldap2-dev libsasl2-dev libsnmp-dev snmp-mibs-downloader              && \
    pip install --upgrade pip setuptools                                    && \
    pip install -r /requirements.txt                             && \
    sed -i 's/mibs :/#mibs :/' /etc/snmp/snmp.conf                          && \
    apt-get autoremove -y build-essential                                   && \
    rm -rf /var/lib/apt/lists/*                                             && \
    mkdir -p /etc/openldap/cacerts                                          && \
    echo 'TLS_CACERTDIR /etc/openldap/cacerts' > /etc/ldap/ldap.conf        && \
    echo 'TLS_REQCERT allow' >> /etc/ldap/ldap.conf

#!/bin/bash

set -ex

if [ -z ${SECRET_KEY+x} ]; then SECRET_KEY=${SECRET_KEY}; fi
if [ -z ${DEBUG+x} ]; then DEBUG=${DEBUG}; fi
if [ -z ${ALLOWED_HOSTS+x} ]; then ALLOWED_HOSTS=${ALLOWED_HOSTS}; fi
if [ -z ${CSRF_TRUSTED_ORIGINS+x} ]; then CSRF_TRUSTED_ORIGINS=${CSRF_TRUSTED_ORIGINS}; fi
if [ -z ${MYSQL_DB+x} ]; then MYSQL_DB=${MYSQL_DB}; fi
if [ -z ${MYSQL_USER+x} ]; then MYSQL_USER=${MYSQL_USER}; fi
if [ -z ${MYSQL_PASS+x} ]; then MYSQL_PASS=${MYSQL_PASS}; fi
if [ -z ${MYSQL_HOST+x} ]; then MYSQL_HOST=${MYSQL_HOST}; fi
if [ -z ${BROKER+x} ]; then BROKER=${BROKER}; fi
if [ -z ${JIRA_USER+x} ]; then JIRA_USER=${JIRA_USER}; fi
if [ -z ${JIRA_PASS+x} ]; then JIRA_PASS=${JIRA_PASS}; fi
if [ -z ${JIRA_URL+x} ]; then JIRA_URL=${JIRA_URL}; fi
if [ -z ${EMAIL_BACKEND+x} ]; then EMAIL_BACKEND=${EMAIL_BACKEND}; fi
if [ -z ${MY_URL+x} ]; then MY_URL=${MY_URL}; fi
WORKERS=${GUNICORN_WORKERS:-4}

exec gunicorn --certfile=/etc/ssl/certs/_.netops.charter.com.crt \
     --keyfile=/etc/ssl/certs/_.netops.charter.com.key \
     --access-logfile /cbo-portal/log/intake-access.log \
     --error-logfile /cbo-portal/log/intake-error.log \
     --pid /cbo-portal/log/intake.pid \
     --timeout 60 \
     --workers $WORKERS \
     --bind 0.0.0.0:8000 \
     cboportal.wsgi:application

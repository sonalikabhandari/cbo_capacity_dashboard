#!/bin/bash

set -ex

exec celery -A cboportal worker -Q poller -P eventlet --concurrency 200 -l INFO -E

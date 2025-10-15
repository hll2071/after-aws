#!/bin/bash
set -e
export DEPLOY_TIME=$(date +%Y%m%d%H%M%S)
mkdir -p /home/ubuntu/flaskapp/releases/${DEPLOY_TIME}


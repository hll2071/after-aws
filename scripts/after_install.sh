#!/bin/bash
set -e
# 최신 릴리즈를 current로 연결
cd /home/ubuntu/flaskapp/releases
LATEST=$(ls -1dt */ | head -n1 | tr -d '/')
ln -sfn /home/ubuntu/flaskapp/releases/$LATEST /home/ubuntu/flaskapp/current

# venv 생성/업데이트 + 의존성 설치
python3 -m venv /home/ubuntu/flaskapp/venv || true
source /home/ubuntu/flaskapp/venv/bin/activate
pip install --upgrade pip
pip install --no-cache-dir -r /home/ubuntu/flaskapp/current/requirements.txt

# 권한 정리(실행 사용자 보장)
chown -R ubuntu:ubuntu /home/ubuntu/flaskapp


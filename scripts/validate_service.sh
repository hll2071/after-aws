#!/bin/bash
set -e
# /health 라우트가 있으면 우선 확인, 없으면 루트 시도
curl -fsS http://127.0.0.1:5000/health || curl -fsS http://127.0.0.1:5000/


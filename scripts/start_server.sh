#!/bin/bash
set -e
systemctl daemon-reload
systemctl restart flaskapp


#!/bin/bash
set -a
source .env || echo "No .env found, using no env"
python3 -u -m service.main
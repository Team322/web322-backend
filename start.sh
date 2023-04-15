#! /bin/bash
set -euxo pipefail
set -o allexport
source .env
set +o allexport
python3 -m flask run
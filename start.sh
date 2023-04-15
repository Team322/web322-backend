#! /bin/bash
set -euxo pipefail
source venv/bin/activate
pip install -r requirements.txt
set -o allexport
source .env
set +o allexport
flask run
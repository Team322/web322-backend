#! /bin/bash
set -euxo pipefail
source venv/bin/activate
set -o allexport
source .env
set +o allexport
python manage.py
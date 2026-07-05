#!/usr/bin/env bash
set -euo pipefail

KAJAX_PROD_SSH="${KAJAX_PROD_SSH:-root@159.69.153.24}"
KAJAX_PROD_DIR="${KAJAX_PROD_DIR:-/projects/kajax}"

ssh "$KAJAX_PROD_SSH" "cd '$KAJAX_PROD_DIR' && docker-compose exec -T web python manage.py shell" <<'PY'
from leads.smoke import smoke_cleanup_queryset

qs = smoke_cleanup_queryset()
count = qs.count()
deleted = qs.delete()[0] if count else 0
print({"matched": count, "deleted": deleted})
PY

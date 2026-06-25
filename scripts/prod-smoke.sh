#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  ./scripts/cleanup-prod-smoke-leads.sh
}

cleanup
trap cleanup EXIT

E2E_BASE_URL="${E2E_BASE_URL:-https://kajax.eu}" \
E2E_ALLOW_GTM="${E2E_ALLOW_GTM:-1}" \
npm run test:e2e -- --project=desktop --grep "home keeps the frontend payload lean|submits a qualified lead"

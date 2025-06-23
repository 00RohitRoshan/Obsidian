#!/bin/bash

# Exit on any error
set -euo pipefail

# Define array of Git repository URLs
REPO_URLS=(
    "https://gitlab.txninfra.com/camunda/camunda_product/billing_backend"
    # "https://gitlab.txninfra.com/camunda/bob/Camunda-7-Workflow"
    # "https://gitlab.txninfra.com/ManashiDas/camunda-7-workflow-engine"
    "https://gitlab.txninfra.com/soundbox/tms/device_inventory"
    "https://gitlab.txninfra.com/api-gateway/api-gateway-dev/extauth-istio"
    "https://gitlab.txninfra.com/api-gateway/api-gateway-dev/go-clientsecrets"
    # "https://gitlab.txninfra.com/los/los-workflow-process"
    "https://gitlab.txninfra.com/soundbox/mqtt_server_soundbox"
    "https://gitlab.txninfra.com/soundbox/tms/ota-management"
    "https://gitlab.txninfra.com/api-gateway/api-gateway-dev/redirect_application"
    "https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-activity-status-golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-inventory"
    "https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-mapping-admin-api-golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-mapping-internal-golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-registration-golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice_soundbox_mqttconfig_adm_api_golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice_soundbox_mqttconfig_internal_golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice_soundbox_otamgmt_adm_api_golang-service"
    "https://gitlab.txninfra.com/soundbox/slice/slice_soundbox_otamgmt_internal_golang-service"
    "https://gitlab.txninfra.com/pubsub/soundbox/canara_bank/soundbox_pg_datastore_subscriber"
    "https://gitlab.txninfra.com/soundbox/tms/tms_backend_internal"
    "https://gitlab.txninfra.com/soundbox/upload-file"
    # Add more repos as needed
)

# Loop over each repository
for REPO_URL in "${REPO_URLS[@]}"; do
  REPO_NAME=$(basename -s .git "$REPO_URL")
  OUTPUT_FILE="${REPO_NAME}_commits.md"

  # Create temp dir and ensure cleanup
  TMP_DIR=$(mktemp -d)
  trap 'rm -rf "$TMP_DIR"' EXIT

  echo "🔄 Processing: $REPO_URL"

  # Clone the repository
  git clone --no-checkout "$REPO_URL" "$TMP_DIR/repo" > /dev/null
  cd "$TMP_DIR/repo"

  # Get all remote branches (excluding HEAD)
  BRANCHES=$(git for-each-ref --format='%(refname:short)' refs/remotes/ | grep -v 'HEAD$')

  # Start output file in the original directory
  OUTPUT_PATH="$OLDPWD/$OUTPUT_FILE"
  echo "# Commit History for '$REPO_NAME'" > "$OUTPUT_PATH"

  for REMOTE_BRANCH in $BRANCHES; do
    # Create a local tracking branch
    LOCAL_BRANCH="temp_branch"
    git branch -f "$LOCAL_BRANCH" "$REMOTE_BRANCH" > /dev/null

    echo -e "\n## Branch: $REMOTE_BRANCH\n" >> "$OUTPUT_PATH"
    git log --pretty=format:'%B' --date=iso "$LOCAL_BRANCH" >> "$OUTPUT_PATH"
  done

  echo "✅ Commit log written to: $OUTPUT_PATH"
  cd "$OLDPWD"
  rm -rf "$TMP_DIR"
done

#!/bin/bash

# Exit on any error
set -euo pipefail

# Ensure a URL is provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <remote-repo-url>"
  exit 1
fi

REPO_URL="$1"
REPO_NAME=$(basename -s .git "$REPO_URL")
OUTPUT_FILE="${REPO_NAME}_commits.md"

# Create temp dir and ensure cleanup
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

# Clone the full repository (not mirror, so we can check out branches)
git clone --no-checkout "$REPO_URL" "$TMP_DIR/repo" > /dev/null

cd "$TMP_DIR/repo"

# Fetch all remote branches
# git fetch --all > /dev/null

# Get all remote branches (excluding HEAD pointers)
BRANCHES=$(git for-each-ref --format='%(refname:short)' refs/remotes/ | grep -v 'HEAD$')

# Start output file in the original directory
OUTPUT_PATH="$OLDPWD/$OUTPUT_FILE"
echo "# Commit History for '$REPO_NAME'" > "$OUTPUT_PATH"

for REMOTE_BRANCH in $BRANCHES; do
  # Create a local tracking branch for the remote
  LOCAL_BRANCH="temp_branch"
  git branch -f "$LOCAL_BRANCH" "$REMOTE_BRANCH" > /dev/null

  echo -e "\n## Branch: $REMOTE_BRANCH\n" >> "$OUTPUT_PATH"

#   git log --pretty=format:'%ad%n%B' --date=iso "$LOCAL_BRANCH" >> "$OUTPUT_PATH"
  git log --pretty=format:'%B' --date=iso "$LOCAL_BRANCH" >> "$OUTPUT_PATH"

done

echo "✅ Commit log written to: $OUTPUT_PATH"

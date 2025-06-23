#!/bin/bash

# Exit on any error
set -e

# Ensure a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <remote-repo-url>"
  exit 1
fi

REPO_URL="$1"
REPO_NAME=$(basename -s .git "$REPO_URL")
OUTPUT_FILE="${REPO_NAME}_commits.md"

# Create temp dir and ensure cleanup
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

# Clone repo as mirror to get all branches and history
git clone --mirror "$REPO_URL" "$TMP_DIR/repo" > /dev/null

cd "$TMP_DIR/repo"

# Get all remote branches
BRANCHES=$(git for-each-ref --format='%(refname:short)' refs/remotes/origin)

# Start output file
echo "# Commit History for '$REPO_NAME'" > "$OLDPWD/$OUTPUT_FILE"

for BRANCH in $BRANCHES; do
  BRANCH_NAME=${BRANCH#origin/}
  echo -e "\n## Branch: $BRANCH_NAME\n" >> "$OLDPWD/$OUTPUT_FILE"

  # Format: date, newline, full message
  git log --pretty=format:'%ad%n%n%B%n' --date=iso "$BRANCH" >> "$OLDPWD/$OUTPUT_FILE"
done

echo "✅ Commit log written to: $OUTPUT_FILE"

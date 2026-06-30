#!/usr/bin/env bash
# Mirror the evidence archive to remote servers via rsync/ssh.
#
# Usage:
#   bash scripts/mirror_sync.sh user@server1:/path/to/mirror [user@server2:/path/to/mirror ...]
#
# Prerequisites:
#   - rsync installed locally and on remote
#   - SSH key-based auth configured
#   - Remote directory exists
#
# Example:
#   bash scripts/mirror_sync.sh root@123.45.67.89:/var/www/takecanadaback

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
EVIDENCE_DIR="$REPO_ROOT/EVIDENCE_COLLECTED"
SEAL_FILES="$REPO_ROOT/MANIFEST.json $REPO_ROOT/MERKLE_ROOT.txt $REPO_ROOT/SEAL.json $REPO_ROOT/SIGNATURE.sig"
RSYNC_OPTS="-avz --delete --progress"

if [ $# -eq 0 ]; then
    echo "Usage: bash scripts/mirror_sync.sh user@server:/path [user@server2:/path ...]"
    echo ""
    echo "Mirrors EVIDENCE_COLLECTED/ and seal files to remote servers."
    exit 1
fi

# Ensure seal exists
if [ ! -f "$REPO_ROOT/MANIFEST.json" ]; then
    echo "Seal not found. Run: python3 scripts/seal_archive.py"
    exit 1
fi

# Verify integrity before mirroring
echo "=== Verifying local archive before mirror ==="
python3 "$SCRIPT_DIR/verify_integrity.py" --dir "$EVIDENCE_DIR" --manifest "$REPO_ROOT/MANIFEST.json"
if [ $? -ne 0 ]; then
    echo "Archive verification failed. Aborting mirror."
    exit 2
fi

for DEST in "$@"; do
    echo ""
    echo "=== Mirroring to: $DEST ==="

    # Sync evidence directory
    rsync $RSYNC_OPTS "$EVIDENCE_DIR/" "$DEST/EVIDENCE_COLLECTED/"

    # Sync seal files
    rsync $RSYNC_OPTS $SEAL_FILES "$DEST/"

    echo "Done: $DEST"
done

echo ""
echo "=== ALL MIRRORS COMPLETE ==="
echo "Active mirrors: $#"
echo "Merkle root: $(cat $REPO_ROOT/MERKLE_ROOT.txt)"

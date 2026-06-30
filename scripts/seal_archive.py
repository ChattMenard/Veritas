#!/usr/bin/env python3
"""Seal the evidence archive with SHA-256 hashes and a Merkle tree root.

Usage:
    python3 scripts/seal_archive.py [--dir EVIDENCE_COLLECTED/] [--output .]

Outputs:
    MANIFEST.json       - every file's hash, size, and mtime
    MERKLE_ROOT.txt     - the single root hash
    SIGNATURE.sig       - GPG signature of the root (if GPG available)
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def build_merkle_tree(hashes: List[str]) -> str:
    """Build a binary Merkle tree from a list of hex hashes.
    Returns the Merkle root as a hex string.
    """
    # Convert hex strings to bytes
    level = [bytes.fromhex(h) for h in hashes]

    if len(level) == 0:
        return hashlib.sha256(b"").hexdigest()

    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            next_level.append(hashlib.sha256(left + right).digest())
        level = next_level

    return level[0].hex()


def seal(directory: Path, output_dir: Path) -> Tuple[str, Path]:
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    manifest = {}
    file_hashes = []

    for root, _dirs, files in os.walk(directory):
        for filename in sorted(files):
            filepath = Path(root) / filename
            relpath = str(filepath.relative_to(directory))
            file_hash = sha256_file(filepath)
            stat = filepath.stat()
            manifest[relpath] = {
                "sha256": file_hash,
                "size": stat.st_size,
                "mtime": stat.st_mtime,
            }
            file_hashes.append(file_hash)

    # Sort hashes deterministically for consistent Merkle root
    file_hashes.sort()
    merkle_root = build_merkle_tree(file_hashes)

    # Write manifest
    manifest_path = output_dir / "MANIFEST.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
    manifest_hash = sha256_file(manifest_path)

    # Write Merkle root
    root_path = output_dir / "MERKLE_ROOT.txt"
    with open(root_path, "w") as f:
        f.write(f"{merkle_root}\n")

    # Write combined seal (root + manifest hash)
    seal_path = output_dir / "SEAL.json"
    seal_data = {
        "merkle_root": merkle_root,
        "manifest_sha256": manifest_hash,
        "file_count": len(file_hashes),
        "source_directory": str(directory),
    }
    with open(seal_path, "w") as f:
        json.dump(seal_data, f, indent=2)

    # Attempt GPG signature
    sig_path = output_dir / "SIGNATURE.sig"
    try:
        result = subprocess.run(
            ["gpg", "--detach-sign", "-a", "-o", str(sig_path), str(root_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"GPG signature written: {sig_path}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        sig_path.write_text(
            "# No GPG signature generated.\n"
            "# Install GPG and run: gpg --detach-sign -a -o SIGNATURE.sig MERKLE_ROOT.txt\n"
        )
        print("Note: GPG not available. Install gnupg to generate cryptographic signatures.")

    print(f"\n=== ARCHIVE SEALED ===")
    print(f"Files hashed:     {len(file_hashes)}")
    print(f"Manifest:         {manifest_path}")
    print(f"Merkle root:      {merkle_root}")
    print(f"Seal file:        {seal_path}")
    print(f"\nPublish this root anywhere:")
    print(f"  {merkle_root}")
    print(f"\nTo verify: python3 scripts/verify_integrity.py")

    return merkle_root, seal_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seal the evidence archive.")
    parser.add_argument("--dir", default="EVIDENCE_COLLECTED", help="Directory to seal")
    parser.add_argument("--output", default=".", help="Output directory for seal files")
    args = parser.parse_args()

    seal(Path(args.dir), Path(args.output))

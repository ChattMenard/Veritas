#!/usr/bin/env python3
"""Verify the evidence archive against its sealed manifest.

Usage:
    python3 scripts/verify_integrity.py [--dir EVIDENCE_COLLECTED/] [--manifest MANIFEST.json]

Reports:
    - OK: file matches hash
    - TAMPERED: file hash differs
    - MISSING: file in manifest but not on disk
    - EXTRA: file on disk but not in manifest
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def verify(directory: Path, manifest_path: Path):
    if not manifest_path.exists():
        print(f"Error: Manifest not found: {manifest_path}", file=sys.stderr)
        print("Run: python3 scripts/seal_archive.py", file=sys.stderr)
        sys.exit(1)

    with open(manifest_path) as f:
        manifest = json.load(f)

    tampered = 0
    missing = 0
    extra = 0
    ok = 0

    # Track files on disk
    disk_files = set()
    for root, _dirs, files in sorted(directory.walk()):
        for filename in files:
            relpath = str((root / filename).relative_to(directory))
            disk_files.add(relpath)

    manifest_files = set(manifest.keys())

    print(f"\n=== VERIFICATION REPORT ===")
    print(f"Manifest entries: {len(manifest_files)}")
    print(f"Files on disk:    {len(disk_files)}\n")

    # Check manifest files
    for relpath in sorted(manifest_files):
        expected = manifest[relpath]["sha256"]
        filepath = directory / relpath

        if not filepath.exists():
            print(f"  [MISSING]  {relpath}")
            missing += 1
            continue

        actual = sha256_file(filepath)
        if actual == expected:
            print(f"  [OK]       {relpath}")
            ok += 1
        else:
            print(f"  [TAMPERED] {relpath}")
            print(f"             Expected: {expected}")
            print(f"             Actual:   {actual}")
            tampered += 1

    # Check extra files
    for relpath in sorted(disk_files - manifest_files):
        print(f"  [EXTRA]    {relpath}")
        extra += 1

    print(f"\n=== SUMMARY ===")
    print(f"OK:       {ok}")
    print(f"TAMPERED: {tampered}")
    print(f"MISSING:  {missing}")
    print(f"EXTRA:    {extra}")

    if tampered or missing:
        print(f"\n*** ARCHIVE INTEGRITY COMPROMISED ***")
        sys.exit(2)
    else:
        print(f"\n*** ARCHIVE VERIFIED ***")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify archive integrity.")
    parser.add_argument("--dir", default="EVIDENCE_COLLECTED", help="Directory to verify")
    parser.add_argument("--manifest", default="MANIFEST.json", help="Manifest file path")
    args = parser.parse_args()

    verify(Path(args.dir), Path(args.manifest))

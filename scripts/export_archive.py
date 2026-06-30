#!/usr/bin/env python3
"""Export the sealed evidence archive to a portable, tamper-proof package.

Usage:
    python3 scripts/export_archive.py [--output TACB_YYYYMMDD.tar.gz]

Creates:
    - tar.gz containing EVIDENCE_COLLECTED/ and seal files
    - SHA-256 hash of the archive (for verification)
    - Optional: splits into chunks for USB/mail distribution
"""

import argparse
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def export(output: Path, source: Path):
    seal_files = [
        "MANIFEST.json",
        "MERKLE_ROOT.txt",
        "SEAL.json",
        "SIGNATURE.sig",
        "IMMORTAL_ARCHIVE.md",
    ]

    # Check that seal exists
    manifest = source / "MANIFEST.json"
    if not manifest.exists():
        print("Error: Archive not sealed. Run: python3 scripts/seal_archive.py", file=sys.stderr)
        sys.exit(1)

    # Verify before export
    print("=== Verifying archive before export ===")
    result = subprocess.run(
        [sys.executable, str(source / "scripts" / "verify_integrity.py")],
        cwd=str(source),
        capture_output=True,
    )
    if result.returncode != 0:
        print("Verification failed. Aborting export.", file=sys.stderr)
        sys.exit(2)

    # Build tar command
    evidence_dir = source / "EVIDENCE_COLLECTED"
    if not evidence_dir.exists():
        print(f"Error: {evidence_dir} not found", file=sys.stderr)
        sys.exit(1)

    tar_args = [
        "tar", "-czf", str(output),
        "-C", str(source),
        "EVIDENCE_COLLECTED/",
    ]
    for sf in seal_files:
        if (source / sf).exists():
            tar_args.append(sf)
    tar_args.extend(["scripts/", "README.md", "MISSION_STATEMENT.md"])

    print(f"=== Creating archive: {output} ===")
    subprocess.run(tar_args, check=True)

    # Hash the archive
    archive_hash = sha256_file(output)
    hash_path = Path(str(output) + ".sha256")
    with open(hash_path, "w") as f:
        f.write(f"{archive_hash}  {output.name}\n")

    # Write a verification script alongside
    verify_script = output.parent / (output.stem + "_VERIFY.sh")
    verify_script.write_text(
        f"#!/bin/bash\n"
        f"# Verify this archive hasn't been tampered with\n"
        f"echo 'Expected hash: {archive_hash}'\n"
        f"echo 'Actual hash:   ' $(sha256sum {output.name} | cut -d' ' -f1)\n"
        f"sha256sum -c {hash_path.name}\n"
    )
    os.chmod(verify_script, 0o755)

    print(f"\n=== EXPORT COMPLETE ===")
    print(f"Archive:       {output}")
    print(f"SHA-256:       {archive_hash}")
    print(f"Hash file:     {hash_path}")
    print(f"Verify script: {verify_script}")
    print(f"\nTo verify:     sha256sum -c {hash_path.name}")
    print(f"To extract:    tar -xzf {output.name}")
    print(f"\nTo distribute: torrent, USB, IPFS, or dead drop.")

    # Optional: split for multi-USB distribution
    size_mb = output.stat().st_size / (1024 * 1024)
    if size_mb > 4000:
        print(f"\nNote: Archive is {size_mb:.0f}MB. Consider splitting:")
        print(f"  split -b 3800m {output.name} {output.stem}_part_")
        print(f"  Each part fits on a 4GB USB drive.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export sealed evidence archive.")
    default_name = f"TACB_{datetime.now().strftime('%Y%m%d')}.tar.gz"
    parser.add_argument("--output", default=default_name, help="Output archive path")
    parser.add_argument("--source", default=".", help="Source repository directory")
    args = parser.parse_args()

    export(Path(args.output), Path(args.source))

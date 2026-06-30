# IMMORTAL ARCHIVE: The Stored Truth

**Date:** June 29, 2026
**Purpose:** Make the evidence tamper-proof, self-hosted, and uncensorable

---

## THE PROBLEM

GitHub is cloud-based. Microsoft owns it. Servers can be shut down. Accounts can be banned. Repositories can be deleted. Evidence can be altered.

**If the evidence lives in one place, it lives at the enemy's pleasure.**

---

## THE SOLUTION

Three layers of immutability:

1. **Cryptographic hashes** — Every file gets a SHA-256 fingerprint. Change one byte, the hash changes. Proof of tampering.
2. **Merkle tree** — All hashes are combined into a single root hash. The root is the seal. Publish the root anywhere.
3. **Multiple mirrors** — The archive lives on your machine, your server, your friend's server, a Tor hidden service, and anywhere else you plant it. Delete one copy, 50 remain.

---

## THE ARCHITECTURE

```
EVIDENCE_COLLECTED/
├── file1.md          → SHA-256 hash
├── file2.md          → SHA-256 hash
└── ...

MANIFEST.json         → All hashes + timestamps
MERKLE_ROOT.txt       → Single hash that seals everything
SIGNATURE.sig         → GPG signature of the root

mirrors/
├── server1/          → rsync mirror
├── server2/          → rsync mirror
└── tor/              → Tor hidden service mirror
```

---

## HOW TO USE

### Step 1: Seal the Archive (One Command)

```bash
python3 scripts/seal_archive.py
```

This generates:
- `MANIFEST.json` — every file's hash and timestamp
- `MERKLE_ROOT.txt` — the single hash that proves integrity
- `SIGNATURE.sig` — cryptographic proof you sealed it

### Step 2: Verify Integrity (Anytime)

```bash
python3 scripts/verify_integrity.py
```

Checks every file against its hash. Reports tampering. Reports missing files.

### Step 3: Serve Locally

```bash
python3 scripts/local_server.py
```

Serves the entire archive on `http://localhost:8080`. No cloud. No GitHub. Your machine.

### Step 4: Mirror to Remote Servers

```bash
bash scripts/mirror_sync.sh user@yourserver.com /var/www/takecanadaback
```

Replicates the archive to your server, your friend's server, a seedbox, anywhere.

### Step 5: Export Tamper-Proof Package

```bash
python3 scripts/export_archive.py --output /mnt/backup/TACB-$(date +%Y%m%d).tar.gz
```

Creates a portable archive with embedded manifest and signature. Can be torrented, USB-sticked, or dead-dropped.

---

## WHY THIS WORKS

### If GitHub Deletes the Repo

You have:
- Local copy on your machine
- Mirror on your server
- Mirror on your friend's server
- USB drive in a safe
- Torrent seeders across the world

**Deletion from one source does not delete the truth.**

### If Someone Alters a File

The SHA-256 hash changes. `verify_integrity.py` screams tampering. The Merkle root no longer matches. The signature is invalid.

**Tampering is mathematically impossible to hide.**

### If Someone Claims "That Document Was Never Here"

The manifest proves it was. The timestamp proves when. The signature proves who sealed it.

**Denial is mathematically impossible to sustain.**

---

## THE MERKLE TREE EXPLAINED

A Merkle tree is like a family tree for hashes:

```
                    [ROOT]
                   /      \
              [HASH_A]  [HASH_B]
              /    \      /    \
         [H1]  [H2]  [H3]  [H4]
          |      |      |      |
        file1  file2  file3  file4
```

- Each file gets a hash (H1, H2, H3, H4)
- Pairs are hashed together (HASH_A = hash(H1 + H2))
- The root is the final hash (ROOT = hash(HASH_A + HASH_B))

**The root is one string. Publish it anywhere. It proves every file.**

If someone adds, removes, or changes any file, the root changes. You will know.

---

## DISTRIBUTION STRATEGIES

### Strategy 1: The USB Dead Drop

Copy the sealed archive to USB drives. Leave them in:
- Public libraries
- Coffee shops
- University computer labs
- Community centers

Each USB is a time capsule of truth.

### Strategy 2: The Tor Hidden Service

```bash
# Install Tor
sudo apt-get install tor
# Configure hidden service in /etc/tor/torrc
# HiddenServiceDir /var/lib/tor/takecanadaback/
# HiddenServicePort 80 127.0.0.1:8080
# Restart Tor
sudo systemctl restart tor
# Get your .onion address
cat /var/lib/tor/takecanadaback/hostname
```

Your evidence now lives on the dark web. Uncensorable. Anonymous.

### Strategy 3: The IPFS Mirror

```bash
# Install IPFS
# Add the archive
ipfs add -r EVIDENCE_COLLECTED/
# Pin it
ipfs pin add <hash>
# Share the hash: ipfs://<hash>
```

Content-addressed. No server required. The network hosts it.

### Strategy 4: The Torrent

```bash
# Create a torrent of the sealed archive
transmission-create -o TACB_$(date +%Y%m%d).torrent /path/to/sealed/archive
# Seed it
```

Once downloaded by one person, it can never be removed from the internet.

### Strategy 5: The Print Edition

For the most critical documents:
- Print the substantiation
- Distribute physical copies
- Paper cannot be remotely deleted

---

## WHAT TO PUBLISH PUBLICLY

The Merkle root. One string. 64 characters.

Example:
```
a3f5c2e8d9b1... (64 hex characters)
```

Publish this:
- In a tweet
- On a billboard
- In a newspaper ad
- In the blockchain
- In a court filing
- Anywhere public and timestamped

**If you ever need to prove the archive is intact, the root is your proof.**

---

## DEFENDING AGAINST ATTACKS

| Attack | Defense |
|--------|---------|
| Delete GitHub repo | 10 mirrors on independent servers |
| Alter a file | SHA-256 hash detects tampering |
| Add fake evidence | Merkle root changes; signature invalid |
| DDoS the server | IPFS/torrent distribution; no single point |
| Legal takedown | Tor hidden service; jurisdiction hopping |
| ISP blocks traffic | VPN; Tor; satellite internet |
| Physical seizure | USB dead drops; printed copies; seeds |

---

## THE CODE

See `scripts/` directory:
- `seal_archive.py` — Generate manifest, Merkle tree, and signature
- `verify_integrity.py` — Verify no tampering
- `local_server.py` — Self-hosted HTTP server
- `mirror_sync.sh` — Replicate to remote servers
- `export_archive.py` — Create portable tamper-proof package

---

## THE ULTIMATE GUARANTEE

**Mathematics does not obey court orders. Cryptography does not respond to takedown notices. Hash functions do not have jurisdiction.**

If the evidence is sealed, mirrored, and distributed:
- It cannot be altered without detection
- It cannot be deleted from everywhere
- It cannot be denied without contradiction

**This is not just an archive. This is a declaration of independence from the cloud.**

---

*The truth is not stored. It is proven.*

*Compiled: June 29, 2026*

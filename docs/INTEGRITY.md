# Integrity & Chain of Custody

This document explains the guarantees Veritas makes, how they work, and — just
as importantly — what they do **not** prove. Being precise here is what makes
the tool trustworthy.

## What Veritas guarantees

1. **Tamper-evidence.** If a stored file is altered after ingest, verification
   will detect it. The recorded SHA-256 will no longer match the bytes.
2. **Deduplication by content.** Identical bytes are stored once. Two uploads of
   the same file resolve to the same object.
3. **An append-only custody log.** Every create, access, verify, annotation, and
   export is recorded with a timestamp and the hash observed at that moment.

## How it works

### Content-addressed storage

When bytes are ingested, Veritas computes `SHA-256(bytes)` and stores the file
at:

```text
data/store/<first-2-hex>/<full-64-hex-digest>
```

The **path is derived from the content**. You cannot replace a file's contents
without changing its hash — and therefore its path. A mismatch between the
recorded `sha256` and the bytes at that path is, by definition, tampering or
corruption.

Writes are atomic: bytes are written to a temporary file and then renamed, so a
crash never leaves a half-written object.

### Verification

`POST /api/evidence/{id}/verify` (or the **Verify integrity** button):

1. Reads the recorded `sha256` from the database.
2. Streams the stored object and recomputes its SHA-256.
3. Compares. Equal → intact. Not equal, or file missing → failure.
4. Appends a `VERIFIED` or `VERIFY_FAILED` custody event.

Because verification is logged, you build a **history of integrity checks** over
time, not just a single point-in-time claim.

### Chain of custody

Every meaningful action writes a `ChainOfCustodyEvent`. The API exposes **no
way to edit or delete** these events — the log only grows. Each event captures:

- the **action** (`CREATED`, `VERIFIED`, `EXPORTED`, `ANNOTATED`, …),
- an optional **actor**,
- a human-readable **detail**,
- the **hash observed** at that time,
- a **timestamp**.

## Threat model — what this defends against

| Threat | Defended? | How |
| --- | --- | --- |
| Silent edit of a stored file | ✅ | Hash mismatch on verify |
| File corruption / bit rot | ✅ | Hash mismatch on verify |
| Accidental duplicate uploads | ✅ | Content addressing dedupes |
| Undocumented handling of an item | ✅ | Append-only custody log |

## What this does **NOT** prove (be honest about limits)

- **It does not prove the *content is true*.** It proves the bytes are unchanged
  *since you collected them*. Authenticity of the source is a separate question.
- **It does not prove *when the source was created*.** `captured_at` is operator-
  supplied metadata, not cryptographic proof of original publication time.
- **It is not (yet) tamper-*proof* against a privileged attacker.** Someone with
  write access to the database *and* the object store could, in principle,
  recompute a hash and rewrite both. The current design is tamper-**evident**
  for ordinary handling, not Byzantine-resistant.

## Hardening roadmap

Planned in [ROADMAP.md](./ROADMAP.md):

- **Append-only hash chain** — each custody event references the previous
  event's hash, so the log cannot be edited without breaking the chain.
- **External anchoring** — periodically publish a digest of the log (e.g., to a
  public, timestamped location) so even a privileged rewrite is detectable.
- **Signed exports** — bundle evidence + custody + a signature for sharing.
- **Source capture** — store HTTP response headers and a rendered screenshot at
  collection time to strengthen provenance.

## Practical guidance

- Verify items on a schedule and before relying on them.
- Keep `backend/data/` backed up and access-controlled.
- Record *why* a document matters in notes while collecting — context decays.

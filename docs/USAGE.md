# Usage Guide

How to collect, inspect, verify, and export evidence — both through the UI and
the API.

## Prerequisites

Both servers running (see [DEPLOYMENT.md](./DEPLOYMENT.md)):

- Backend: `http://127.0.0.1:8000`
- Frontend: `http://localhost:5173`

## 1. Collect evidence (UI)

1. Open the UI and click **Preserve evidence**.
2. Drag a file into the drop zone (or click to browse).
3. Fill in provenance — at minimum a **title** and **source URL**. Add
   **captured at**, **collected by**, and **notes** for stronger records.
4. Click **Preserve & hash**. The file is hashed with SHA-256 and stored, and a
   `CREATED` custody event is logged.

Good provenance habits:

- **Always record the source URL** and the **capture date**.
- Put the *significance* of the document in **notes** while it's fresh.
- Use a consistent **collected by** handle so the custody log is attributable.

## 2. Collect evidence from a public URL (CLI, today)

Until the one-click URL collector ships, fetch + ingest in one step:

```bash
URL="https://example.gov/report.pdf"
curl -sL "$URL" -o /tmp/item
curl -s -X POST http://127.0.0.1:8000/api/evidence \
  -F "file=@/tmp/item;type=application/pdf;filename=report.pdf" \
  -F "title=Descriptive title" \
  -F "source_url=$URL" \
  -F "captured_at=2024-08-28T00:00:00" \
  -F "collected_by=YourHandle" \
  -F "notes=Why this matters."
```

This is exactly how the PBO Fiscal Sustainability Report 2024 was collected.

## 3. Inspect evidence

In the UI, click any item in the sidebar to open its detail view:

- **Provenance panel** — SHA-256, size, type, source, dates, collector, notes.
- **Chain of custody** — a timeline of every action taken on the item.

## 4. Verify integrity

Click **Verify integrity** (or `POST /api/evidence/{id}/verify`). Veritas
re-reads the stored bytes, recomputes the hash, and compares it to the recorded
value:

- ✅ **Intact** → a `VERIFIED` event is appended.
- ❌ **Altered/missing** → a `VERIFY_FAILED` event is appended and the UI shows a
  red warning.

Verify periodically and before relying on an item — every check is logged.

## 5. Add custody notes

Use the note box in the detail view to record actions or observations (e.g.,
"shared with counsel", "cross-checked against gazette"). Each note is an
immutable `ANNOTATED` custody event.

## 6. Export / download

Click **Download** (or `GET /api/evidence/{id}/download`). The original file is
returned and an `EXPORTED` event is logged, so exports are part of the audit
trail.

## 7. Search

Use the sidebar search box. It matches **title**, **source description**,
**notes**, and **source URL**.

## Tips for building a credible record

- **Preserve originals, not summaries.** Collect the source PDF/page itself.
- **One claim, many sources.** Stronger conclusions cite multiple documents.
- **Never alter stored files.** If you annotate, do it in notes/custody, not the
  bytes — that's what keeps verification meaningful.
- **Back up `backend/data/`.** That directory *is* your evidence.

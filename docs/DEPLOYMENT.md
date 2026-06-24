# Deployment & Running

Veritas runs as two processes: the **backend** (FastAPI on port 8000) and the
**frontend** (Vite dev server on port 5173). For local accountability work,
running both on your own machine is the recommended setup.

## Requirements

- Python 3.11+
- Node.js 18+ and npm

## Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- API: `http://127.0.0.1:8000`
- Interactive docs: `http://127.0.0.1:8000/docs`
- On first run, `data/veritas.db` and `data/store/` are created automatically.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

- UI: `http://localhost:5173`
- The Vite dev server proxies `/api` to `http://127.0.0.1:8000`
  (see `frontend/vite.config.js`), so no CORS config is needed in dev.

## Configuration

Override any setting with a `VERITAS_`-prefixed environment variable
(see `backend/app/config.py`):

| Variable | Default | Purpose |
| --- | --- | --- |
| `VERITAS_DATABASE_URL` | `sqlite:///…/data/veritas.db` | DB location / engine. |
| `VERITAS_STORAGE_DIR` | `…/data/store` | Object store path. |
| `VERITAS_MAX_UPLOAD_MB` | `512` | Max upload size. |
| `VERITAS_CORS_ORIGINS` | localhost:5173 | Allowed browser origins. |

A `.env` file in `backend/` is also read.

## Production build (frontend)

```bash
cd frontend
npm run build      # outputs static files to dist/
npm run preview    # serve the build locally to test
```

Serve `frontend/dist/` from any static host or reverse proxy, and run the
backend behind the same proxy so `/api` reaches port 8000.

## Backups — read this

**`backend/data/` is your evidence.** It contains the SQLite database (metadata
and custody log) plus the object store (the raw files). It is intentionally
git-ignored. Back it up regularly:

```bash
# Simple, consistent snapshot
tar czf veritas-backup-$(date +%F).tgz -C backend data
```

Store backups securely and off-machine. Losing this directory means losing the
vault.

## Security notes for any shared deployment

- There is **no authentication yet** — do not expose the backend to the open
  internet as-is. Put it behind a VPN, SSH tunnel, or an authenticating reverse
  proxy.
- Restrict filesystem permissions on `backend/data/`.
- See [SECURITY.md](./SECURITY.md) and [INTEGRITY.md](./INTEGRITY.md).

## Reproducible runs (planned)

A `Dockerfile` + `docker-compose.yml` for one-command startup is on the
[roadmap](./ROADMAP.md) (Track C).

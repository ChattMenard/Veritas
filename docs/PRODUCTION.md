# Production Deployment

## Live URLs

| Service | URL |
| ------- | --- |
| **Frontend** | <https://govtbs.netlify.app> |
| **Backend API** | <https://backend-production-cf1f.up.railway.app> |
| **Custom Domain** | <https://proofstacked.com> (Vercel alias — point DNS to Netlify to cut over) |

## Architecture

```text
Browser → Netlify (govtbs.netlify.app)
              │
              ├── /api/* → Railway backend (FastAPI)
              │                 │
              │                 └── /app/data (persistent volume, 5 GB)
              │                       ├── veritas.db  (SQLite)
              │                       └── store/      (content-addressed blobs)
              │
              └── /* → React SPA (dist/)
```

## Backend (Railway)

- **Project:** veritas
- **Service:** backend
- **Domain:** <https://backend-production-cf1f.up.railway.app>
- **Internal:** `backend.railway.internal`
- **Volume:** `backend-volume` mounted at `/app/data` (5 GB)
- **Builder:** Dockerfile (`backend/Dockerfile`)

### Environment Variables

| Variable | Value |
| -------- | ----- |
| `VERITAS_DATABASE_URL` | `sqlite:////app/data/veritas.db` |
| `VERITAS_STORAGE_DIR` | `/app/data/store` |
| `VERITAS_CORS_ORIGINS` | `["https://govtbs.netlify.app","https://proofstacked.com"]` |
| `VERITAS_MAX_UPLOAD_MB` | `512` |
| `VERITAS_TIMESTAMP_ENABLED` | `true` |
| `VERITAS_RFC3161_ENABLED` | `true` |

### Redeploy

```bash
cd /home/x99/Desktop/FUCK
railway up -y -m "description of change"
```

### Logs

```bash
railway logs --service backend --lines 200
```

## Frontend (Netlify)

- **Project:** govtbs
- **Site:** <https://govtbs.netlify.app>
- **Project ID:** 8fbdec35-bda6-4b22-9ec6-574311d9cf9b
- **Builder:** Vite (`npm run build` → `dist/`)

### Deploy Frontend

```bash
cd /home/x99/Desktop/FUCK/frontend
npm run build
netlify deploy --prod --dir=dist
```

### API Proxy

Configured in `frontend/netlify.toml`:

```toml
[[redirects]]
  from = "/api/*"
  to = "https://backend-production-cf1f.up.railway.app/api/:splat"
  status = 200
  force = true
```

## Custom Domain Cutover (proofstacked.com → Netlify)

1. Go to <https://app.netlify.com/projects/govtbs/domain-management>
2. Add custom domain `proofstacked.com`
3. Update DNS: point `proofstacked.com` CNAME/A record to Netlify
4. Update backend CORS: add `https://proofstacked.com` to `VERITAS_CORS_ORIGINS`
5. Remove Vercel alias once DNS propagates

## Verification

```bash
curl https://backend-production-cf1f.up.railway.app/api/health
curl https://govtbs.netlify.app/api/health
curl https://govtbs.netlify.app/api/stats
```

## Evidence Stats (as of deployment)

- Evidence items: 53
- Entities: 22
- Relationships: 14
- Timeline entries: 11
- Storage: ~14.8 MB

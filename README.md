## Flask Autocomplete Demo

A minimal Flask app that serves a front-end page and an autocomplete API over a mock dataset.

### Features
- Serves `index.html` via Flask
- `/api/autocomplete?query=...` returns filtered matches across multiple fields
- `/dashboard` page with filters, sorting, pagination, CSV export
- Donut chart (TM2 Share) that updates with filters

### Requirements
- Python 3.10+

### Setup (Windows PowerShell)
```powershell
cd D:\bhumi
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Run
```powershell
python app.py
```

- App: `http://localhost:5000/`
- API: `http://localhost:5000/api/autocomplete?query=jwara`
- Dashboard: `http://localhost:5000/dashboard`

### API Example
```bash
curl "http://localhost:5000/api/autocomplete?query=migraine"
```

Response (example):
```json
[
  {
    "namasteCode": "NAM018",
    "namasteTerm": "Shiroroga (Sarva Sadharan)",
    "icd11Tm2Code": "TM2-08",
    "icd11Tm2Term": "Headache",
    "icd11BiomedicineCode": "8A80",
    "icd11BiomedicineTerm": "Migraine"
  }
]
```

### Template location (important)
The app is initialized as:
```python
app = Flask(__name__, template_folder='.')
```
This looks for `index.html` in the repo root (same folder as `app.py`).

### Notes
- The server binds to `0.0.0.0` (configured in `app.py`), so it is reachable from your network using your machine's IP at port 5000 if your firewall permits.

### Deploy to Render
1. Push this repo to GitHub.
2. On Render: New → Blueprint → pick this repo (uses `render.yaml`).
3. Render sets:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Deploy. To redeploy after changes: push to `main` (auto-deploy) or use Manual Deploy.

### Update on GitHub
```powershell
cd D:\bhumi
git add -A
git commit -m "Dashboard + donut chart + fixes"
git push origin main
```

### Procfile (Heroku-compatible)
If using platforms that read `Procfile`, it's included:
```
web: gunicorn app:app
```



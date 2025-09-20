## Flask Autocomplete Demo

A minimal Flask app that serves a front-end page and an autocomplete API over a mock dataset.

### Features
- Serves `index.html` via Flask
- `/api/autocomplete?query=...` returns filtered matches across multiple fields

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
2. In Render, create a new Web Service from the repo.
3. It will detect `render.yaml` and auto-configure:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Once deployed, visit the generated URL.

### Procfile (Heroku-compatible)
If using platforms that read `Procfile`, it's included:
```
web: gunicorn app:app
```



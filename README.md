python -m venv .venv  
 .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

REST Based

uvicorn app.main:app --host 127.0.0.1 --port 9000 --reload

NON-REST Based
python -m app.main

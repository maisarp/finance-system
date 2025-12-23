# Copilot instructions (FinanceBackend)

## Chat instructions
Always answer the user in Portuguese (Brazilian Portuguese).
Always generate code in english.

## Big picture
- This repo is a small **FastAPI** backend with a single entrypoint: `FinanceBackend.py`.
- The API object is created as `app = FastAPI(...)` in `FinanceBackend.py` and the service is started via `uvicorn.run(...)` under `if __name__ == "__main__":`.
- Database access is Azure SQL via **SQLAlchemy Core + pyodbc**:
  - Connection string is built in `config/db_config.py` as `AZURE_DB_CONNECTION_STRING`.
  - Config is loaded from environment variables using `dotenv.load_dotenv()` (expects a local `.env`).

## Local dev workflow
- Create/activate the virtualenv (repo convention is `.venv/`):
  - Git-bash: `source .venv/Scripts/activate`
- Install deps: `pip install -r requirements.txt`
- Run the API (binds to `127.0.0.1:8000` by default):
  - `python FinanceBackend.py`
  - or (reload-friendly): `uvicorn FinanceBackend:app --reload --host 127.0.0.1 --port 8000`

## Required configuration
- `config/db_config.py` reads these env vars:
  - `AZURE_SQL_SERVER_DB`
  - `DATABASE_NAME`
  - `USERNAME_AZURE_DB_SERVER`
  - `PASSWORD_AZURE_DB_SERVER` (URL-encoded via `urllib.parse.quote_plus`)

## Code patterns to follow
- Routes are declared directly in `FinanceBackend.py` with `@app.get(...)` decorators (currently synchronous `def` handlers).
- DB queries follow this pattern:
  - `engine = create_engine(AZURE_DB_CONNECTION_STRING)`
  - `with engine.connect() as connection:`
  - `result = connection.execute(text(""" ... """))`
  - Map each row into JSON-ready dicts (e.g., decimals to `float`, dates to `str`) like the `/dividas-yasmin` endpoint.
- Error handling in endpoints currently returns `{"erro": str(e)}` from a broad `try/except`; preserve this response shape unless you intentionally change API behavior.

## Repo-specific constraints
- Prefer minimal, in-place changes consistent with the current “single-file API + config module” structure; don’t introduce routers/ORM layers unless explicitly requested.
- Keep secrets out of code: credentials are expected to live in `.env` and `.gitignore` is configured to ignore `.env` / `.env.*`.

# Shoppy

A small Django shop project. Products have a name and price and appear on the Products page.

## Run locally

```powershell
uv sync
uv run manage.py migrate
uv run manage.py runserver
```

Open the home page at `http://127.0.0.1:8000/`.

Pages: `/`, `/about/`, `/products/`, and `/products/add/`. Django admin is at `/admin/`.

For a local admin account, run `uv run manage.py createsuperuser`.

The local SQLite database is not committed. If you deploy the project, set `DJANGO_SECRET_KEY` to a private value and configure deployment settings separately.

# Affinity42

Backend service in Python to query the 42 API using OAuth2 client credentials.

## Requisitos

- Python 3.10+
- Una aplicación registrada en 42 con `client_id` y `client_secret`

## Configuración

1. Copia variables de entorno:

```bash
cp .env.example .env
```

2. Completa en `.env`:

- `FORTY_TWO_CLIENT_ID`
- `FORTY_TWO_CLIENT_SECRET`
- `FORTY_TWO_API_BASE_URL` (por defecto `https://api.intra.42.fr`)
- `REQUEST_TIMEOUT_SECONDS` (por defecto `15`)

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`: healthcheck
- `GET /42/{resource_path}`: proxy GET a `https://api.intra.42.fr/v2/{resource_path}`
  - acepta query params y los reenvía al API de 42
- `GET /42/users/{login}`: endpoint directo para obtener un usuario

## Referencias

- https://api.intra.42.fr/apidoc/guides/getting_started
- https://api.intra.42.fr/apidoc/guides/web_application_flow
- https://profile.intra.42.fr/legal/terms/33
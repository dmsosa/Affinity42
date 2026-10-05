from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.forty_two_client import FortyTwoApiError, forty_two_client

app = FastAPI(title="Affinity42 Backend", version="0.1.0")


def _validate_settings() -> None:
    if not settings.is_configured:
        raise HTTPException(
            status_code=500,
            detail="42 API credentials are missing. Set FORTY_TWO_CLIENT_ID and FORTY_TWO_CLIENT_SECRET.",
        )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/42/{resource_path:path}")
def proxy_get_resource(resource_path: str, request: Request) -> JSONResponse:
    _validate_settings()

    query_params = dict(request.query_params.items())
    try:
        response = forty_two_client.get(resource_path=resource_path, params=query_params)
    except FortyTwoApiError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error

    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type:
        payload = response.json()
    else:
        payload = {"raw_response": response.text}

    return JSONResponse(status_code=response.status_code, content=payload)


@app.get("/42/users/{login}")
def get_user_profile(login: str, campus_id: int | None = Query(default=None)) -> JSONResponse:
    _validate_settings()
    params: dict[str, str | int] = {}
    if campus_id is not None:
        params["campus_id"] = campus_id

    try:
        response = forty_two_client.get(resource_path=f"users/{login}", params=params)
    except FortyTwoApiError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error

    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type:
        payload = response.json()
    else:
        payload = {"raw_response": response.text}

    return JSONResponse(status_code=response.status_code, content=payload)

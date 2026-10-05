from __future__ import annotations

import time
from typing import Any

import requests

from app.config import settings


class FortyTwoApiError(Exception):
    pass


class FortyTwoClient:
    def __init__(self) -> None:
        self._access_token: str | None = None
        self._expires_at: float = 0

    def _token_is_valid(self) -> bool:
        return bool(self._access_token) and time.time() < self._expires_at

    def _fetch_access_token(self) -> str:
        response = requests.post(
            f"{settings.forty_two_api_base_url}/oauth/token",
            data={
                "grant_type": "client_credentials",
                "client_id": settings.forty_two_client_id,
                "client_secret": settings.forty_two_client_secret,
            },
            timeout=settings.request_timeout_seconds,
        )
        if not response.ok:
            raise FortyTwoApiError(
                f"Failed to authenticate with 42 API: {response.status_code} {response.text}"
            )

        payload = response.json()
        token = payload.get("access_token")
        expires_in = int(payload.get("expires_in", 0))
        if not token:
            raise FortyTwoApiError("42 API authentication succeeded but no access token was returned.")

        self._access_token = token
        self._expires_at = time.time() + max(expires_in - 30, 0)
        return token

    def _ensure_access_token(self) -> str:
        if self._token_is_valid():
            return self._access_token or ""
        return self._fetch_access_token()

    def get(self, resource_path: str, params: dict[str, Any] | None = None) -> requests.Response:
        token = self._ensure_access_token()
        response = requests.get(
            f"{settings.forty_two_api_base_url}/v2/{resource_path.lstrip('/')}",
            headers={"Authorization": "Bearer " + token},
            params=params,
            timeout=settings.request_timeout_seconds,
        )

        if response.status_code == 401:
            token = self._fetch_access_token()
            response = requests.get(
                f"{settings.forty_two_api_base_url}/v2/{resource_path.lstrip('/')}",
                headers={"Authorization": "Bearer " + token},
                params=params,
                timeout=settings.request_timeout_seconds,
            )

        return response


forty_two_client = FortyTwoClient()

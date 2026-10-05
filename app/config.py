from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.forty_two_client_id = os.getenv("FORTY_TWO_CLIENT_ID", "")
        self.forty_two_client_secret = os.getenv("FORTY_TWO_CLIENT_SECRET", "")
        self.forty_two_api_base_url = os.getenv(
            "FORTY_TWO_API_BASE_URL", "https://api.intra.42.fr"
        ).rstrip("/")
        self.request_timeout_seconds = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "15"))

    @property
    def is_configured(self) -> bool:
        return bool(self.forty_two_client_id and self.forty_two_client_secret)


settings = Settings()

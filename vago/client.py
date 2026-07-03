"""HTTP client for VAGO Cloud API."""

from __future__ import annotations

from typing import Any

import httpx

from .exceptions import VagoAPIError, VagoAuthError, VagoNotFoundError

DEFAULT_BASE_URL = "https://www.vagocloud.com"
DEFAULT_TIMEOUT = 60.0


class VagoClient:
    """Client for the VAGO Cloud API.

    Usage:
        client = VagoClient(token="vago_agt_...")
        me = client.me()
        jobs = client.jobs.list(tenant_id=1)
    """

    def __init__(
        self,
        token: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ):
        if not token:
            raise ValueError("token is required")
        self._token = token
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=self._timeout,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

        # Lazy resource accessors
        from .resources.analytics import AnalyticsResource
        from .resources.channels import ChannelsResource
        from .resources.jobs import JobsResource
        from .resources.products import ProductsResource
        from .resources.tenants import TenantsResource
        from .resources.users import UsersResource

        self.jobs = JobsResource(self)
        self.channels = ChannelsResource(self)
        self.tenants = TenantsResource(self)
        self.users = UsersResource(self)
        self.products = ProductsResource(self)
        self.analytics = AnalyticsResource(self)

    def _request(
        self,
        method: str,
        path: str,
        *,
        tenant_id: int | str | None = None,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if not path.startswith("/"):
            path = "/" + path
        headers: dict[str, str] = {}
        if tenant_id is not None:
            headers["X-Tenant-Id"] = str(tenant_id)

        response = self._client.request(
            method.upper(), path, headers=headers, json=json, params=params
        )

        if response.status_code == 401:
            raise VagoAuthError("Invalid or revoked token", status_code=401)
        if response.status_code == 404:
            raise VagoNotFoundError("Resource not found", status_code=404)
        if response.status_code >= 400:
            body = self._safe_json(response)
            raise VagoAPIError(
                f"API error {response.status_code}: {body}",
                status_code=response.status_code,
                body=body,
            )

        return self._safe_json(response)

    @staticmethod
    def _safe_json(response: httpx.Response) -> Any:
        try:
            return response.json()
        except Exception:
            return {"raw": response.text[:500]}

    def me(self) -> dict[str, Any]:
        """Return the current user/profile."""
        return self._request("GET", "/api/auth/me/")

    def platform_overview(self) -> dict[str, Any]:
        """Return platform-wide overview (superadmin)."""
        return self._request("GET", "/api/auth/platform-overview/")

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> VagoClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

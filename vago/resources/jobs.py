"""Jobs/sync operations resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class JobsResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def list(self, tenant_id: int | str) -> dict[str, Any]:
        """List recent sync jobs for a tenant."""
        return self._client._request("GET", "/api/jobs/", tenant_id=tenant_id)

    def get(self, tenant_id: int | str, job_id: int) -> dict[str, Any]:
        """Get a single job detail including log."""
        return self._client._request(
            "GET", f"/api/jobs/{job_id}/", tenant_id=tenant_id
        )

    def retry(self, tenant_id: int | str, job_id: int) -> dict[str, Any]:
        """Retry a failed or dead-letter job."""
        return self._client._request(
            "POST", f"/api/jobs/{job_id}/retry/", tenant_id=tenant_id
        )

    def sync(self, tenant_id: int | str, canal: str = "all") -> dict[str, Any]:
        """Trigger a stock sync. canal: 'all' or 'shopify'/'mercadolibre'/'falabella'/'ripley'/'mundotec'."""
        return self._client._request(
            "POST", "/api/jobs/sync/", tenant_id=tenant_id, json={"canal": canal}
        )

    def preview(self, tenant_id: int | str) -> dict[str, Any]:
        """Preview next sync changes without executing."""
        return self._client._request(
            "GET", "/api/jobs/preview/", tenant_id=tenant_id
        )

    def not_found(self, tenant_id: int | str) -> dict[str, Any]:
        """List SKUs not found per channel."""
        return self._client._request(
            "GET", "/api/jobs/not-found/", tenant_id=tenant_id
        )

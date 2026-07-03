"""Channels/stores resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class ChannelsResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def list(self, tenant_id: int | str) -> dict[str, Any]:
        """List configured channels for a tenant."""
        return self._client._request("GET", "/api/channels/", tenant_id=tenant_id)

    def maestro_status(self, tenant_id: int | str) -> dict[str, Any]:
        """Get master snapshot status."""
        return self._client._request(
            "GET", "/api/channels/maestro-status/", tenant_id=tenant_id
        )

    def refresh_maestro(self, tenant_id: int | str) -> dict[str, Any]:
        """Refresh master snapshot from OneDrive/Excel/Shopify."""
        return self._client._request(
            "POST", "/api/channels/maestro-refresh/", tenant_id=tenant_id
        )

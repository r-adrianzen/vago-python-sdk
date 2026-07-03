"""Analytics resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class AnalyticsResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def overview(
        self,
        tenant_id: int | str,
        month: str = "",
        lite: bool = True,
    ) -> dict[str, Any]:
        """Get analytics overview for a tenant.

        month: 'YYYY-MM' (empty = current month).
        lite: True uses cache for faster response.
        """
        params: dict[str, Any] = {}
        if month:
            params["month"] = month
        if lite:
            params["lite"] = "1"
        return self._client._request(
            "GET", "/api/channels/analytics-overview/", tenant_id=tenant_id, params=params
        )

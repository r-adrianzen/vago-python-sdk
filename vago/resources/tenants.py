"""Tenants/businesses resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class TenantsResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def list(self) -> dict[str, Any]:
        """List all tenants (superadmin)."""
        return self._client._request("GET", "/api/auth/tenants/")

    def create(
        self,
        nombre: str,
        plan: str = "trial",
        estado: str = "trial",
        fuente_tipo: str = "excel",
        notas: str = "",
    ) -> dict[str, Any]:
        """Create a new tenant."""
        return self._client._request(
            "POST",
            "/api/auth/tenants/",
            json={
                "nombre": nombre,
                "plan": plan,
                "estado": estado,
                "fuente_tipo": fuente_tipo,
                "notas": notas,
            },
        )

    def update(self, tenant_id: int | str, changes: dict[str, Any]) -> dict[str, Any]:
        """Partially update a tenant."""
        return self._client._request(
            "PATCH", f"/api/auth/tenants/{tenant_id}/", json=changes
        )

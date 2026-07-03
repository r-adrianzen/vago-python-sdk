"""Users resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class UsersResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def list(self) -> dict[str, Any]:
        """List all users (superadmin)."""
        return self._client._request("GET", "/api/auth/users/")

    def create(
        self,
        username: str,
        email: str,
        password: str,
        role: str = "analista",
        tenant_id: int | str | None = None,
        first_name: str = "",
        last_name: str = "",
    ) -> dict[str, Any]:
        """Create a user."""
        body: dict[str, Any] = {
            "username": username,
            "email": email,
            "password": password,
            "role": role,
            "first_name": first_name,
            "last_name": last_name,
        }
        if tenant_id is not None:
            body["tenant_id"] = tenant_id
        return self._client._request("POST", "/api/auth/users/", json=body)

    def update(self, user_id: int | str, changes: dict[str, Any]) -> dict[str, Any]:
        """Partially update a user."""
        return self._client._request(
            "PATCH", f"/api/auth/users/{user_id}/", json=changes
        )

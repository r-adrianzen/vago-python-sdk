"""Products resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..client import VagoClient


class ProductsResource:
    def __init__(self, client: VagoClient):
        self._client = client

    def create_shopify(
        self,
        tenant_id: int | str,
        skus: list[str],
        modo: str = "ingresos",
    ) -> dict[str, Any]:
        """Create products in Shopify from master. modo: 'ingresos' | 'preventa'."""
        return self._client._request(
            "POST",
            "/api/channels/product-create-shopify/",
            tenant_id=tenant_id,
            json={"modo": modo, "skus": skus},
        )

    def create_marketplace(
        self,
        tenant_id: int | str,
        canal: str,
        skus: list[str],
    ) -> dict[str, Any]:
        """Publish existing Shopify products to a marketplace.

        canal: mercadolibre | falabella | riley
        """
        return self._client._request(
            "POST",
            "/api/channels/product-create-mktp/",
            tenant_id=tenant_id,
            json={"canal": canal, "skus": skus},
        )

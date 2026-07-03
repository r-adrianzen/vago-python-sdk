# VAGO Cloud Python SDK

Official Python SDK for the **VAGO Cloud** API.

> **VAGO Cloud** syncs stock, pricing and products between a master catalog (Excel / OneDrive / Shopify) and marketplaces like Shopify, MercadoLibre, Falabella, Ripley and more.

## Installation

```bash
pip install git+https://github.com/r-adrianzen/vago-python-sdk.git
```

Or clone and install locally:

```bash
git clone https://github.com/r-adrianzen/vago-python-sdk.git
cd vago-python-sdk
pip install -e ".[dev]"
```

## Authentication

You need an **agent token** from VAGO Cloud (`vago_agt_...`).

1. Log in to VAGO Cloud as a superadmin.
2. Go to **Gestión de cuenta → Agentes IA → Crear token**.
3. Copy the token immediately (shown only once).

Set it as an environment variable:

```bash
export VAGO_AGENT_TOKEN="vago_agt_..."
```

## Usage

```python
from vago import VagoClient

client = VagoClient(token="vago_agt_...")

# Identity
print(client.me())
print(client.platform_overview())

# Jobs / sync (replace with your tenant id)
tenant_id = 1
print(client.jobs.list(tenant_id=tenant_id))
print(client.jobs.sync(tenant_id=tenant_id, canal="shopify"))

# Channels
print(client.channels.list(tenant_id=tenant_id))

# Analytics
print(client.analytics.overview(tenant_id=tenant_id))

client.close()
```

Or use the context manager:

```python
with VagoClient(token="vago_agt_...") as client:
    print(client.jobs.list(tenant_id=1))
```

## Resources

- `client.me()` / `client.platform_overview()`
- `client.tenants.list()` / `create()` / `update()`
- `client.users.list()` / `create()` / `update()`
- `client.jobs.list()` / `get()` / `retry()` / `sync()` / `preview()` / `not_found()`
- `client.channels.list()` / `maestro_status()` / `refresh_maestro()`
- `client.products.create_shopify()` / `create_marketplace()`
- `client.analytics.overview()`

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

## License

MIT — see [LICENSE](./LICENSE).

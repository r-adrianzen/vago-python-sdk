"""Basic usage example for the VAGO Cloud Python SDK."""

import os

from vago import VagoClient

TOKEN = os.environ.get("VAGO_AGENT_TOKEN", "vago_agt_...")
TENANT_ID = int(os.environ.get("VAGO_TENANT_ID", "1"))


def main():
    with VagoClient(token=TOKEN) as client:
        me = client.me()
        print("User:", me.get("username"), me.get("role"))

        jobs = client.jobs.list(tenant_id=TENANT_ID)
        print("Recent jobs:", jobs)


if __name__ == "__main__":
    main()

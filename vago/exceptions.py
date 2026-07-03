"""Exceptions raised by the VAGO Cloud SDK."""


class VagoError(Exception):
    """Base exception."""


class VagoAPIError(VagoError):
    """Raised when the API returns an error response."""

    def __init__(self, message: str, status_code: int | None = None, body: dict | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body or {}


class VagoAuthError(VagoAPIError):
    """Raised on 401/403 responses."""


class VagoNotFoundError(VagoAPIError):
    """Raised on 404 responses."""

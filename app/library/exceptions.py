class PlayerAPIError(Exception):
    """Base exception for CS2 API errors."""

    def __init__(self, message: str = "", details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

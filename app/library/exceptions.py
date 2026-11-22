"""Exceptions for CS2 API operations."""

from typing import Optional


class PlayerAPIError(Exception):
    """Base exception for CS2 API errors.

    Attributes:
        message: Human-readable error message.
        details: Optional dictionary with additional error information.
    """

    def __init__(self, message: str = "", details: Optional[dict] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

"""Placeholder utilities for Stripe billing integration."""

import logging

logger = logging.getLogger(__name__)


def process_stripe_event(event: dict) -> None:
    """Handle an incoming Stripe webhook event."""
    logger.info("Stripe event handling not yet implemented: %s", event.get("type"))
    raise NotImplementedError("Stripe billing integration is not implemented")

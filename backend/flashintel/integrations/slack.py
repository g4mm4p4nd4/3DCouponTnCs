import os
import logging
from typing import Optional

import requests

from ..celery_app import celery_app

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
logger = logging.getLogger(__name__)


def post_urgent_article(title: str, url: str) -> Optional[requests.Response]:
    """Post an urgent article notification to Slack if a webhook is configured."""
    if not SLACK_WEBHOOK_URL:
        logger.debug("Slack webhook not configured; skipping notification")
        return None

    payload = {"text": f"*Urgent*: <{url}|{title}>"}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=5)
        response.raise_for_status()
        logger.info("Posted urgent article to Slack: %s", title)
        return response
    except Exception as exc:
        logger.warning("Failed to post to Slack: %s", exc)
        return None


@celery_app.task(name="flashintel.post_urgent_slack")
def post_urgent_article_task(title: str, url: str) -> None:
    """Celery task wrapper for :func:`post_urgent_article`."""
    post_urgent_article(title, url)

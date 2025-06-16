"""Minimal FastAPI app with placeholder endpoints."""

from fastapi import FastAPI, Request, HTTPException

from .integrations import sso, stripe

app = FastAPI(title="FlashIntel API")


@app.post("/sso/saml/login")
async def saml_login():
    """Entry point for initiating SAML SSO login."""
    try:
        sso.initiate_saml_login()
    except NotImplementedError as exc:
        raise HTTPException(status_code=501, detail=str(exc))
    return {"detail": "SAML login initiated"}


@app.post("/billing/stripe/webhook")
async def stripe_webhook(request: Request):
    """Receive Stripe webhook events."""
    event = await request.json()
    try:
        stripe.process_stripe_event(event)
    except NotImplementedError as exc:
        raise HTTPException(status_code=501, detail=str(exc))
    return {"detail": "Event processed"}

from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping() -> dict:
    return {"message": "pong"}


def ingest_feed(items):
    """Return only feed items that contain an id field."""
    return [item for item in items if item.get("id")]

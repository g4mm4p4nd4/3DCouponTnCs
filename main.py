from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI(title="Article API")


class Article(BaseModel):
    title: str
    content: str
    category: str
    date: datetime
    urgency: str
    dedup_confidence: float
    score: float


# Example in-memory articles storage
articles_db: List[Article] = [
    Article(
        title="Sample Article 1",
        content="Content of article 1",
        category="general",
        date=datetime(2024, 1, 1),
        urgency="low",
        dedup_confidence=0.98,
        score=0.85,
    ),
    Article(
        title="Sample Article 2",
        content="Content of article 2",
        category="tech",
        date=datetime(2024, 1, 2),
        urgency="high",
        dedup_confidence=0.95,
        score=0.90,
    ),
]


@app.get("/api/articles", response_model=List[Article])
async def get_articles(
    category: Optional[str] = None,
    date: Optional[datetime] = None,
    urgency: Optional[str] = None,
):
    """Return articles filtered by optional category, date, and urgency."""
    results = articles_db
    if category:
        results = [a for a in results if a.category == category]
    if date:
        results = [a for a in results if a.date >= date]
    if urgency:
        results = [a for a in results if a.urgency == urgency]
    return results


# Simple subscribers list for websockets
subscribers: List[WebSocket] = []


@app.websocket("/ws/articles")
async def websocket_articles(ws: WebSocket):
    await ws.accept()
    subscribers.append(ws)
    try:
        while True:
            # keep connection open; send ping? We'll just await receive_text
            await ws.receive_text()
    except Exception:
        pass
    finally:
        subscribers.remove(ws)


async def broadcast_new_article(article: Article):
    for ws in list(subscribers):
        try:
            await ws.send_json(article.dict())
        except Exception:
            try:
                await ws.close()
            except Exception:
                pass
            if ws in subscribers:
                subscribers.remove(ws)


@app.post("/api/articles", response_model=Article)
async def add_article(article: Article):
    articles_db.append(article)
    await broadcast_new_article(article)
    return article


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

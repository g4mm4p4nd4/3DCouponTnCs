from flashintel.db import SessionLocal, Article, Base, engine

def main():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    if not session.query(Article).first():
        article = Article(
            title="Hello World",
            url="https://example.com",
            source="seed",
            content="Initial article",
            score=0.0,
        )
        session.add(article)
        session.commit()
    session.close()

if __name__ == "__main__":
    main()

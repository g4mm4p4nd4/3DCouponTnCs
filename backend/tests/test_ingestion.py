from backend.app.main import ingest_feed


def test_ingest_feed_filters_items_without_id():
    items = [{"id": 1, "title": "a"}, {"title": "b"}]
    result = ingest_feed(items)
    assert result == [{"id": 1, "title": "a"}]

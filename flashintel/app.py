from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .tasks import example_task

app = FastAPI(title="Flashintel")

# Initialize Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/add")
def add(x: int, y: int):
    task = example_task.delay(x, y)
    return {"task_id": task.id}

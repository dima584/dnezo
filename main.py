from fastapi import FastAPI

app = FastAPI(
    title="Lab 2 REST API",
    description="Базовий REST-сервіс для лабораторної роботи з Git. p.s оновлено для коміта",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello, Git!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

# Ендпоінт для перевірки статусу

@app.get("/status")
def get_status():
    return {"status": "ok"}
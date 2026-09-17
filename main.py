from fastapi import FastAPI

app = FastAPI(
    title="Lab 2 REST API",
    description="Базовий REST-сервіс для лабораторної роботи з Git",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello, Git!"}
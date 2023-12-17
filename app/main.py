from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "This is a sample Application"

@app.get("/greet/{name}")
async def greet(name):
    return f"Hello {name}" 
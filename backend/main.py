from fastapi import FastAPI

app = FastAPI(title="Smart Curriculum API")


@app.get("/")
def root():
    return {"message": "Smart Curriculum API is running"}
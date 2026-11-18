from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Task API")


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

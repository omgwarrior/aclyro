from fastapi import FastAPI

app = FastAPI(title="ACLYRO API")

@app.get("/")
def root():
    return {"platform": "aclyro"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}
from fastapi import FastAPI

app = FastAPI(
    title="ACLYRO API",
    description="Cloud, AI, DevOps, SRE, Cyber, and Platform Engineering API",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "platform": "aclyro",
        "message": "Welcome to ACLYRO",
        "mascot": "Rocco 🐕"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}

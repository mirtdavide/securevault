from fastapi import FastAPI

app = FastAPI(title = "SecureVault", 
              description="Your personal Password Manager",
              version="0.1.0")

@app.get("/")
def root():
    return {"message": "Wassup World"}

@app.get("/health")
def read_health():
    return {"status": "ok"}
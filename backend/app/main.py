from fastapi import FastAPI

app = FastAPI(
    title="ERYNDOX API",
    description="Cyber Intelligence & Digital Forensics Platform",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to ERYNDOX",
        "description": "Cyber Intelligence & Digital Forensics",
        "status": "Operational",
        "version": "1.0.0",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ERYNDOX Backend",
    }

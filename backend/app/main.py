from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import router as api_router
from app.core.logger import LoggingMiddleware

app = FastAPI(
    title="Business Advisor AI",
    description="An interactive Q&A system that provides business advice documentation requirements.",
    version="1.0.0"
)

# Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging
app.add_middleware(LoggingMiddleware)

@app.get("/", tags=["Root"])
async def root():
    return JSONResponse(
        content={"message": "Welcome to the Small Business Advisor AI API. POST to /api/v1/query to ask a business-related question."}
    )

# Add a prefix to the endpoints
app.include_router(api_router, prefix="/api/v1")

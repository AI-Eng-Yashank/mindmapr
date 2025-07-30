#app.py

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.api_v1 import api_v1
import uvicorn

# Root router
root_router = APIRouter()

@root_router.get("/")
def hello_world():
    return {"message": "Hello MindMapr 🌐"}

# FastAPI app
app = FastAPI(
    title="MindMapr API",
    description="Turns input text into a JSON-based mind map using Groq LLMs.",
    version="1.0.0"
)

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach routers
app.include_router(api_v1.route_v1)     # All versioned APIs (e.g. /api/v1/mindmap)
app.include_router(root_router)         # Default route ("/")

# Entry point
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

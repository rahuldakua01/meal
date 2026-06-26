from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.db.session import engine
from backend.db.base import Base
from backend.api.router import api_router
from sqlalchemy.orm import Session
from backend.core.dependency import get_db
# from services.user_service import verify_registered_user
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(current_dir, "upload")
os.makedirs(upload_dir, exist_ok=True)
app = FastAPI(title="Rahul")


allowed_origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]
prod_frontend = os.getenv("FRONTEND_URL")
if prod_frontend:
    allowed_origins.append(prod_frontend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.mount("/upload", StaticFiles(directory=upload_dir), name="upload")

Base.metadata.create_all(bind=engine)
app.include_router(api_router)


# @app.get("/verification", response_class=HTMLResponse)
# def email_verification(token: str, db: Session = Depends(get_db)):
#     try:
#         user = verify_registered_user(token, db)
#     except HTTPException as exc:
#         return HTMLResponse(f"<h1>{exc.detail}</h1>", status_code=exc.status_code)

#     return HTMLResponse(
#         f"<h1>Email verified successfully</h1><p>{user.mail} is now registered.</p>"
#     )


frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "dist")

@app.get("/{catchall:path}")
def serve_frontend(catchall: str):
    # Check if a specific file exists in the frontend dist directory (e.g. assets, favicon)
    if frontend_dir and os.path.exists(frontend_dir):
        file_path = os.path.join(frontend_dir, catchall)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        
        # Otherwise, fall back to index.html for React Router SPA routes
        index_path = os.path.join(frontend_dir, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)

    # Fallback if frontend dist is not built/found
    if catchall == "" or catchall == "/":
        return {"status": "backend is running (frontend build not found)"}
    raise HTTPException(status_code=404, detail="Not Found")

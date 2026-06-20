from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items

# init
app = FastAPI(
    title="Backend Practice API",
    description="Простое REST API приложение на FastAPI",
    version="1.0.0"
)

# grant access to outer corms 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(items.router)

@app.get("/", tags=["root"])
async def root():
    """Главная страница приложения"""
    return {
        "message": "Добро пожаловать!",
        "docs": "http://127.0.0.1:8000/docs",
        "redoc": "http://127.0.0.1:8000/redoc"
    }

@app.get("/health", tags=["health"])
async def health_check():
    return {
        "status": "healthy",
        "message": "Приложение работает normalno"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
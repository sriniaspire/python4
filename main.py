from fastapi import FastAPI
from database import engine, Base
from routers import expenses_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",  # Angular
    "http://127.0.0.1:4200",
    "http://localhost:8501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(expenses_router.router)

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8000)

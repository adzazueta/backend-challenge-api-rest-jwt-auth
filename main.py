from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.github_users import github_users

app = FastAPI()
app.include_router(auth_routes, prefix="/api")
app.include_router(github_users, prefix="/api")

load_dotenv()

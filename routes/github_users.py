from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from middlewares.verify_auth_route import VerifyAuthRoute

github_users = APIRouter(route_class=VerifyAuthRoute)

class GithubUser(BaseModel):
  country: str
  page: str

@github_users.post("/github-users")
def get_github_users(users: GithubUser):
  return get(f'https://api.github.com/search/users?q=location:"{users.country}"&page={users.page}').json()

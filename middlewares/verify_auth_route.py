from fastapi.routing import APIRoute
from requests import Request
from functions_jwt import validate_token

class VerifyAuthRoute(APIRoute):
  def get_route_handler(self):
    original_route = super().get_route_handler()

    async def verify_auth_middleware(request: Request):
      token = request.headers["Authorization"].split(" ")[1]
      validation_response = validate_token(token, output=False)

      if validation_response == None:
        return await original_route(request)
      else:
        return validation_response
    
    return verify_auth_middleware

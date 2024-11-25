import time
import httpx
import jwt
from datetime import datetime
from fastapi import HTTPException
from .cache import RedisCache
from .exceptions import JWTManagerError
from .config import Config

class AuthService:
    def __init__(self):
        self.http_client = httpx.Client(verify=False)
        self.cache = RedisCache(Config.REDIS_HOST, Config.REDIS_PORT)

    def get_access_token(self):
        if not Config.USERNAME or not Config.PASSWORD:
            raise HTTPException(status_code=400, detail="Missing credentials for access token")

        headers = {
            'host': 'api.be-ys.com',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-GeXRT-API-Key': Config.API_KEY,
        }
        data = {"login": Config.USERNAME, "password": Config.PASSWORD}
        response = self.http_client.post(Config.ACCESS_TOKEN_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_jwt_token(self, access_token: str):
        start_time = time.perf_counter()
        try:
            headers = {
                'host': 'api.al-in.fr',
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
            }
            data = {"access_token": access_token}
            response = self.http_client.post(Config.JWT_TOKEN_URL, headers=headers, json=data)
            response.raise_for_status()
            execution_time = time.perf_counter() - start_time
            print(f"Execution time: {execution_time} seconds")
            return response.json()["jwt_token"]
        except Exception as e:
            raise JWTManagerError(f"Failed to get JWT token. Error: {str(e)}")

    def decode_jwt(self, jwt_token: str):
        try:
            # Decode the JWT token without verification (for demonstration purposes)
            decoded_token = jwt.decode(jwt_token, options={"verify_signature": False})
            expiration_time = decoded_token.get("exp")
            if expiration_time:
                readable_expiration_time = datetime.fromtimestamp(expiration_time).strftime('%Y-%m-%d %H:%M:%S')
                decoded_token["readable_expiration_time"] = readable_expiration_time
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise JWTManagerError("Token has expired")
        except jwt.InvalidTokenError:
            raise JWTManagerError("Invalid token")

    def create_jwt_result(self, jwt_token: str, expiration_time: int, readable_expiration_time: str, start_time: float):
        execution_time = time.perf_counter() - start_time
        return {
            "jwt_token": jwt_token,
            "expiration_time": expiration_time,
            "readable_expiration_time": readable_expiration_time,
            "execution_time": execution_time
        }

    def get_jwt(self):
        start_time = time.perf_counter()
        try:
            access_token = self.get_access_token()
            jwt_token = self.get_jwt_token(access_token)
            decoded_jwt = self.decode_jwt(jwt_token)
            expiration_time = decoded_jwt["exp"] * 1000  # Convert seconds to milliseconds
            readable_expiration_time = decoded_jwt["readable_expiration_time"]
            return self.create_jwt_result(jwt_token, expiration_time, readable_expiration_time, start_time)
        except Exception as e:
            execution_time = time.perf_counter() - start_time
            raise JWTManagerError(f"Failed to obtain JWT. Execution time: {execution_time}. Error: {str(e)}")

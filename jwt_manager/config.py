import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")    
    ACCESS_TOKEN_URL = os.getenv("ACCESS_TOKEN_URL")
    JWT_TOKEN_URL = os.getenv("JWT_TOKEN_URL")
    API_KEY = os.getenv("API_KEY")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

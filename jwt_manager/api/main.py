from fastapi import FastAPI, HTTPException
from .jwt_service import JWTService

app = FastAPI()
auth_service = JWTService()

@app.get("/jwt")
async def get_jwt():
    try:
        jwt_result = auth_service.get_jwt()
        return jwt_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

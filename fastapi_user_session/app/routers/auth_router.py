from fastapi import APIRouter, Response, Cookie, HTTPException
from app.models.auth_models import LoginRequest, TokenResponse, RefreshResponse, MessageResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth",tags=["auth"])
auth_service = AuthService()
    
@router.post('/login',response_model=TokenResponse)
def login(data:LoginRequest, response= Response):
    access_token, refresh_token = auth_service.login(data.username, data.password)
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="lax",
        secure=False
    )
    return {"access_token":access_token}
        


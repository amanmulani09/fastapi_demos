from fastapi import HTTPException
from core.security import verify_password, create_access_token, create_refresh_token
from repository.auth_repository import AuthRepository

class AuthService:
    
    def __init__(self):
        self.repo = AuthRepository() # create a access instance of repository in contrst
    
    def login(self,username:str,password:str):
        
        user = self.repo.get_user_by_username(username)
        
        if not user:
            raise HTTPException(status_code=401,detail="invalid credentials")
        
        if not verify_password(password,user["password"]):
            raise HTTPException(status_code=401,detail="invalid credentials")
        
        access_token = create_access_token(user["id"])
        refresh_token = create_refresh_token(user["id"])
        
        return access_token, refresh_token
        
    def refresh(self,refresh_token:str):
        
        session  = self.repo.get_refresh_session(refresh_token)
        
        if not session:
            raise HTTPException(status_code=401,detail="invalid refresh token")
        
        return create_access_token(session["user_id"])
        
    def logout(self,refresh_token:str):
        self.repo.delete_refresh_session(refresh_token)
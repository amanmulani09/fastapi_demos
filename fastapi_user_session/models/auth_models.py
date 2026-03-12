from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str  = Field(min_length=3)
    password: str  = Field(min_length=6)
    
    
class TokenResponse(BaseModel):
    access_token : str
    token_type : str
    
class RefreshResponse(BaseModel):
    access_token : str
    
class MessageResponse(BaseModel):
    message : str
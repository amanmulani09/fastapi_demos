from app.store.auth_store import users_db,refresh_sessions

class AuthRepository:
    
    def get_user_by_username(self, username:str):
        return users_db.get(username)
    
    def get_refresh_session(self,token:str):
        return refresh_sessions.get(token)
    
    def delete_refresh_session(self,token:str):
        refresh_sessions.pop(token,None)
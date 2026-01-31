from app.models.user import User

# creating a in-memory data to store the user details 
user_db = {
    "aman":User(username="aman",password="amankapw"),
    "aashu":User(username="aashu",password="aashukapw")
}
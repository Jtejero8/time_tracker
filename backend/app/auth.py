from . import models, database, schemas
from sqlalchemy.orm import Session
import jwt

SECRET = "supersecretkey"
session = database.SessionLocal()

def register_user(user: schemas.UserCreate):
    hashed = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=hashed)
    session.add(db_user)
    session.commit()
    return {"message": "User registered"}

def login_user(user: schemas.UserLogin):
    db_user = session.query(models.User).filter_by(email=user.email).first()
    if db_user and db_user.hashed_password == user.password + "notreallyhashed":
        token = jwt.encode({"user_id": db_user.id}, SECRET, algorithm="HS256")
        return {"access_token": token}
    return {"error": "Invalid credentials"}

def get_user_by_token(token):
    data = jwt.decode(token, SECRET, algorithms=["HS256"])
    return session.query(models.User).get(data["user_id"])
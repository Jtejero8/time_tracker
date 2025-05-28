from fastapi import FastAPI
from . import models, database, crud, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.init_db()

@app.post("/register")
def register(user: auth.UserCreate):
    return auth.register_user(user)

@app.post("/login")
def login(user: auth.UserLogin):
    return auth.login_user(user)

@app.post("/clock-in")
def clock_in(token: str):
    return crud.clock_in(token)

@app.post("/clock-out")
def clock_out(token: str):
    return crud.clock_out(token)

@app.get("/summary")
def get_summary(token: str):
    return crud.get_summary(token)

@app.get("/export/csv")
def export_csv(token: str):
    return crud.export_csv(token)
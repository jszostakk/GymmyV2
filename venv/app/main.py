from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import socket

app = FastAPI()

# CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

class RegisterData(BaseModel):
    username: str
    password: str
    email: str

# Mock database
users_db = {}

@app.post("/register")
def register(data: RegisterData):
    if data.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[data.username] = {"password": data.password, "email": data.email}
    return {"message": "Registration successful"}

@app.post("/login")
def login(data: LoginData):
    user = users_db.get(data.username)
    if user and user["password"] == data.password:
        return {"message": "Login successful", "token": "mock-token"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.on_event("startup")
async def print_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Application is running on IP: {ip_address}")

@app.get("/")
def read_root():
    return {"message": "API test"}

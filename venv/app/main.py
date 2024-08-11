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

@app.post("/login")
def login(data: LoginData):
    # Mock validation (replace with actual validation logic)
    if data.username == "test" and data.password == "test":
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

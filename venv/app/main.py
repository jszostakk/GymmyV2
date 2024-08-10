from fastapi import FastAPI
import socket

app = FastAPI()

@app.on_event("startup")
async def print_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Application is running on IP: {ip_address}")

@app.get("/")
def read_root():
    return {"message": "API test"}
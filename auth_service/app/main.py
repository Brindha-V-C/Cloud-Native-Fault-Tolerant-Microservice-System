from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import UserCreate, UserLogin, Token
import uuid
import hashlib
import httpx
import time 

ANALYTICS_URL = "http://127.0.0.1:8001/events"

app = FastAPI(
    title="Auth Service",
    description="Authentication microservice for a cloud-native system",
    version="1.0.0",
)

# CORS (for future UIs or other services)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary in-memory user "database"
fake_users_db = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/register", response_model=Token)
def register(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.email] = hash_password(user.password)
    token = str(uuid.uuid4())
    return Token(access_token=token)

@app.post("/login", response_model=Token)
def login(user: UserLogin):
    hashed = fake_users_db.get(user.email)
    if not hashed or hashed != hash_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = str(uuid.uuid4())

    # Send event to analytics service
    event = {
        "user_id": user.email,  # using email as ID for now
        "action": "login",
        "timestamp": time.time()
    }

    try:
        response = httpx.post(ANALYTICS_URL, json=event, timeout=3.0)
        print("Analytics Event Response:", response.json())
    except Exception as e:
        print("Failed to send event to analytics:", e)

    return Token(access_token=token)

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI, HTTPException, Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import hashlib
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import jwt
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Bharat Heavy Drones API 🚀"}

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated user database (with verification)
users_db = {}

# Email Configuration (Replace with your SMTP details)

conf = ConnectionConfig(
    MAIL_USERNAME="bharatdronetech@gmail.com",  # ✅ Use your Gmail
    MAIL_PASSWORD="uirh ckys kqwz vtnm",  # ✅ Use your actual Gmail password
    MAIL_FROM="bharatdronetech@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)
# Secret Key for JWT Token
SECRET_KEY = "your_secret_key"

# User model
class User(BaseModel):
    email: EmailStr
    password: str

# ✅ User Signup with Email Verification
@app.post("/signup")
async def signup(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists!")

    # Hash password
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    users_db[user.email] = {"password": hashed_password, "verified": False}

    # Generate verification token
    verification_token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm="HS256")
    verification_link = f"http://127.0.0.1:8000/verify-email/{verification_token}"

    # Send verification email
    message = MessageSchema(
        subject="Verify Your Email - Bharat Heavy Drones",
        recipients=[user.email],
        body=f"Click the link to verify your email: {verification_link}",
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"success": True, "message": "Verification email sent! Check your inbox."}

# ✅ Email Verification Route
@app.get("/verify-email/{token}")
async def verify_email(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload.get("email")

        if email in users_db:
            users_db[email]["verified"] = True
            return {"success": True, "message": "Email verified successfully! You can now sign in."}
        else:
            raise HTTPException(status_code=400, detail="Invalid verification link!")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Verification link expired!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token!")

# ✅ User Login (Only if Email is Verified)
@app.post("/login")
async def login(user: User):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    if user.email not in users_db or users_db[user.email]["password"] != hashed_password:
        raise HTTPException(status_code=401, detail="Invalid email or password!")

    if not users_db[user.email]["verified"]:
        raise HTTPException(status_code=401, detail="Email not verified! Check your inbox.")

    # Send welcome email after login
    message = MessageSchema(
        subject="Welcome Back to Bharat Heavy Drones!",
        recipients=[user.email],
        body="Welcome back! You have successfully signed in.",
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"success": True, "message": "Login successful!"}

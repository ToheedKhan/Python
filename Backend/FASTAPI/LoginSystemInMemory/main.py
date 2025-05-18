from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext


app = FastAPI()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user "database"
users_db = {}

# Pydantic models
class User(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

# Helper to hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Helper to verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Register endpoint
@app.post("/register", response_model=UserOut)
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pwd = hash_password(user.password)
    users_db[user.username] = hashed_pwd
    return {"username": user.username}

# Login endpoint
@app.post("/login")
def login(user: User):
    stored_password = users_db.get(user.username)
    if not stored_password or not verify_password(user.password, stored_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": f"Welcome, {user.username}!"}



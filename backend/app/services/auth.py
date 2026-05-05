import uuid
from app.models.database import db
from app.core.security import hash_password, verify_password, create_access_token

users_collection = db["users"]


def register_user(name, email, password):
    existing = users_collection.find_one({"email": email})
    if existing:
        return None, "User already exists"

    user_id = str(uuid.uuid4())

    user = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "password": hash_password(password),
    }

    users_collection.insert_one(user)

    return user, None


def login_user(email, password):
    user = users_collection.find_one({"email": email})

    if not user or not verify_password(password, user["password"]):
        return None

    token = create_access_token({"user_id": user["user_id"]})

    return token
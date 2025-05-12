The Pydantic library in Python is used for data validation and settings management using Python type hints. It’s widely used in FastAPI and other modern Python applications for safely parsing and validating input data (like from JSON, APIs, etc.).

✅ Basic Usage:
1. Define a Data Model:
python
Copy
Edit
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
2. Create and Validate Data:
python
Copy
Edit
data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
user = User(**data)

print(user.name)      # Alice
print(user.dict())    # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
Automatically raises errors if data types are wrong or fields are missing.

Converts types when possible (e.g., "1" → 1 if id: int).

🔍 Example with Validation:
python
Copy
Edit
from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    name: str
    email: EmailStr  # Validates email format

try:
    user = User(name="Bob", email="invalid-email")
except ValidationError as e:
    print(e)
🔧 Real Use Cases:
Validating API input (e.g., with FastAPI).

Config management (with BaseSettings).

Data transformation (parse JSON into Python objects).

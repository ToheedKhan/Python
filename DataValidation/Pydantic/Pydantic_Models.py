from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr

class Department(Enum):
    HR = "HR"
    IT = "IT"
    SALES = "Sales"
    MARKETING = "Marketing"
    FINANCE = "Finance"
    ENGINEERING = "Engineering"

class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: datetime
    salary: float
    department: Department
    elected_benefits: bool


emp = Employee(
    name="John Doe",
    email="john@gmail.com",
    date_of_birth="1990-01-01",
    salary=50000.0,
    department="IT",
    elected_benefits=True)

print(emp)

# Instantiate Employee from dictionary
emp_dict = {
    "name": "Jane Doe",
    "email": "John@gmail.com",
    "date_of_birth": "1990-01-01",
    "salary": 60000.0,
    "department": "HR",
    "elected_benefits": True
}
emp_from_dict = Employee(**emp_dict)
#print(emp_from_dict)
emp_dict = emp_from_dict.__dict__  

# Convert object to dictionary

emp_frm_dict = Employee.model_validate(emp_dict)

# print(emp_frm_dict)

# Convert to JSON string
json_str = emp.model_dump_json()
print(json_str)
'''
# Convert to dictionary
dict_repr = emp.model_dump()
print(dict_repr)

# Convert from JSON string
emp_from_json = Employee.model_validate_json(json_str)
print(emp_from_json)
# Convert from dictionary
emp_from_dict = Employee.model_validate(dict_repr)
print(emp_from_dict)
'''

# Convert to JSON schema
json_schema = Employee.model_json_schema()

print(json_schema)

# Convert schema to JSON string
# json_schema_str = Employee.model_json_schema_json()

# print(json_schema_str)
# json_schema_str1 = Employee.dumps()
# print(json_schema_str1)
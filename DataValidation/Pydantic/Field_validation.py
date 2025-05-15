from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool


    
employee_data = {
     "name": "Clyde Harwell",
     "email": "charwell@example.com",
     "birth_date": "2000-06-12",
     "compensation": 100_000,
     "department": "ENGINEERING",
     "elected_benefits": True,
 }
    
employee = Employee.model_validate(employee_data)
print(employee)

print(employee.date_of_birth)
print(employee.salary)
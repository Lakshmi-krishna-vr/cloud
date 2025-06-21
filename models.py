from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    FirstName: str
    LastName: str
    MiddleName: Optional[str] = None
    Age: int
    City: str

class ClassInfo(BaseModel):
    ClassName: str
    Description: str
    StartDate: str
    EndDate: str
    Hours: int

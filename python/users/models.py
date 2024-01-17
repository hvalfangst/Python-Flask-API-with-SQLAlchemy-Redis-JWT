from common.models import AccessType
from typing import Dict, Optional
from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[str]
    address: Optional[str]
    email: EmailStr
    password: str
    ssn: str
    access: AccessType


class UpdateUserRequest(BaseModel):
    phone_number: Optional[str]
    address: Optional[str]


class User:
    def __init__(self, user_id, first_name, last_name, phone_number, address, email, password, ssn, access):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.password = password
        self.ssn = ssn
        self.access = access

    def to_dict(self) -> Dict[str, str]:
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "address": self.address,
            "email": self.email,
            "password": self.password,
            "ssn": self.ssn,
            "access": self.access
        }


class Claims:
    def __init__(self, email, access, exp):
        self.email = email
        self.access = access
        self.exp = exp

    def to_dict(self):
        return {
            "email": self.email,
            "access": self.access,
            "exp": self.exp
        }
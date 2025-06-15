from pydantic import BaseModel, Field
from typing import Optional

class BaseUserModel(BaseModel):
    id: Optional[int] = Field(default=None)
    username: str = Field(
        description='Unique username for the user',
        max_length=20,
        min_length=3
    )
    email: str = Field(
        description="Unique email of the user",
        max_length=50,
        min_length=5
    )
    is_staff: bool = False
    is_active: bool = False 
    description: Optional[str] = Field(default=None)


class UserSignupModel(BaseUserModel):
    password: str = Field(
        description='Password of the user',
        max_length=100,
        min_length=8,
    )

    class Config:
        orm_mode = True
        json_schema_extra = {
            'examples': [{
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": True,
                "is_active": True
            }]
        }
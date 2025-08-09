from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T') 

class ApiResponse(BaseModel, Generic[T]):
    data: T = Optional[T]
    is_success: bool = Field(alias="isSuccess")
    message: str
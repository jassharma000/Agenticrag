from pydantic import BaseModel, Field
from typing import List

class Plan(BaseModel):

    steps : List[str] = Field(
        description = " sequential steps to solve the task"
    )
from pydantic import BaseModel, Field
from typing import Literal

class AnsweValidator(BaseModel):

    verdict : Literal[
        "valid",
        "invalid"
    ]= Field(
        description = " Whether answer is grounded and correct"
    )

    reason : str = Field(
        description = "Reason for validation decision"
    )
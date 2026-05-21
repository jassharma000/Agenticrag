from pydantic import BaseModel, Field

class ReflectionOutput(BaseModel):

    critique: str = Field(
        description = "Critiue of the previous answer"

    )

    improvement_suggestions: str = Field(
        description= "Suggestions to improve the answer"
    )
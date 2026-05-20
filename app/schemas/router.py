from pydantic import BaseModel, Field
from typing import Literal


class QueryRouter(BaseModel):

    datasource : Literal[
        "vectorstore",
        "web_search",
        "direct_response"
    ] = Field(
        description=" Route user query to appropriate datascources "
    )
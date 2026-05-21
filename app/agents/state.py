from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list[dict], add_messages]
    
    summary : str
    
    route : str
    
    validation : str

    validation_reason : str

    retries : int

    critique : str

    improvement_suggestions : str

    plan : list

    current_step : int

    step_results : int
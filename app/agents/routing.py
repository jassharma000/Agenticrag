from langgraph.graph import END

def should_continue(state):

    messages = state["messages"]

    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools"
    
    if len(messages) >= 6:
        return "summarize"
    
    return END

def route_query(state) :

    route = state["route"]

    if route == "vectorstore" :
        return "retrieve"
    
    elif route == "web_search" :
        return "web_search"
    
    return "respond"


#validation routing
MAX_RETRIES = 2

def validate_response(state) :

    validation = state["validation"]

    retries = state.get("retries", 0)

    if validation == "valid":
        return END
    
    if retries >= MAX_RETRIES:
        return END
    
    return "assistant"


def should_continue_plan(state):

    current_step = state.get(
        "current_step",
        0
    )

    plan = state["plan"]

    if current_step >= len(plan):
        return END
    
    return "execu"
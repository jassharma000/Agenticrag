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

from langchain_core.messages import HumanMessage

def executor_node(state):

    plan = state["plan"]

    current_step = state.get(
        "current_step", 0)
    
    current_task = plan[current_step]

    execution_prompt = f"""
    you are executing step :

    {current_task}

    Focus only on this step.

    """
    return {
        "messages": [
            HumanMessage(
                content = execution_prompt
            )
        ]
    }
    
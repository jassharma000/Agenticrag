def step_tracker_node(state):

    current_step = state.get(
        "current_step",
        0
    )

    step_results = state.get(
        "step_results",
        []
    )

    latest_response = state["messages"][-1].content

    step_results.append(latest_response)

    return {
        "current_step" : current_step +1,
        "step_results": step_results
    }
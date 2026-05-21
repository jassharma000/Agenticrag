from langgraph.graph import StateGraph, START, END

from app.agents.state import AgentState
from app.agents.nodes import assisstant_node, summary_node, tool_node
from app.agents.routing import should_continue, route_query, validate_response, should_continue_plan
from app.agents.reflection_node import reflection_node
from app.agents.planner_node import planner_node
from app.agents.executor_node import executor_node
from app.agents.step_tracker import step_tracker_node
from langgraph.checkpoint.memory import MemorySaver
from app.agents.router_node import router_node
from langchain_core.messages import HumanMessage
from app.agents.validator_node import validator_node

builder = StateGraph(AgentState)

builder.add_node("assistant", assisstant_node)
builder.add_node("tools", tool_node)
builder.add_node("summarize", summary_node)
builder.add_node("router", router_node)
builder.add_node("validator", validator_node)
builder.add_node("reflection", reflection_node)
builder.add_node("planner", planner_node)
builder.add_node("executor", executor_node)
builder.add_node("step_tracker", step_tracker_node)

#start
builder.add_edge(START, "router")

#routing
builder.add_conditional_edges(
    "router",
    route_query,
    {
        "retrieve" : "tools",
        "web_search" : "assistant",
        "direct_response" : "assistant",
        "respond" : "assistant"
    }
)

#builder.add_edge("planner", "executor")
#builder.add_edge("executor", "assistant")
#builder.add_edge("reflection", "assistant")
'''builder.add_conditional_edges(
    "step_tracker",
    should_continue_plan,
    {
        "executor": "executor",
        END : END
    }
)'''
builder.add_conditional_edges(
    "assistant",
    should_continue,
    {
        "tools" : "tools",
        "summarize" : "summarize",
        END : "validator"
    }
    )

builder.add_edge("tools", "assistant")

builder.add_conditional_edges(
    "validator",
    validate_response,
    {
        "step_tracker": "step_tracker",
        "reflection": "reflection",
        "assistant": "assistant",
        END : END
    }
)


builder.add_edge("summarize", END)


memory = MemorySaver()

graph = builder.compile(checkpointer = memory)
'''
from IPython.display import Image

png_graph = graph.get_graph().draw_mermaid_png()

with open("agent_graph.png", "wb") as f:
    f.write(png_graph)

print("Graph image saved as agent_graph.png")

#testing

if __name__ == "__main__":

    config = {
        "configurable": {
            "thread_id": "12345",
        }
    }

    while True:
        
        query_input = input("User: ")

        if query_input.lower() == "exit":
            break

        response = graph.invoke(
            {
                "messages": [HumanMessage(content=query_input)]
            },
            config = config
        )
        print("\n- ------------------------------------\n")
        print("ROUTE: ", response.get("route"))
        print(" ----------------------------------")

        print("\n assistant response :  ", response["messages"][-1].content)

        print("\n")

'''
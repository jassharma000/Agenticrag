from langgraph.graph import StateGraph, START, END

from app.agents.state import AgentState
from app.agents.nodes import assisstant_node, summary_node, tool_node
from app.agents.routing import should_continue, route_query, validate_response
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

#start
builder.add_edge(START, "router")

#routing
builder.add_conditional_edges(
    "router",
    route_query,
    {
        "retrieve" : "assistant",
        "web_search" : "assistant",
        "direct_response" : "assistant",
        "respond" : "assistant"
    }
)

builder.add_conditional_edges(
    "assistant",
    should_continue,
    {
        "tools" : "tools",
        "summarize" : "summarize",
        END : "validator"
    }
    )

builder.add_node("tools", "assistant")

builder.add_conditional_edges(
    "validator",
    validate_response,
    (
        "assistant": "assistant",
        END : END
    )
)


builder.add_edge("summarize", END)


memory = MemorySaver()

graph = builder.compile(checkpointer = memory)

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


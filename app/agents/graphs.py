from langgraph.graph import StateGraph, START, END

from app.agents.state import AgentState
from app.agents.nodes import assisstant_node, summary_node, tool_node
from app.agents.routing import should_continue
from langgraph.checkpoint.memory import MemorySaver


builder = StateGraph(AgentState)

builder.add_node("assistant", assisstant_node)
builder.add_node("tools", tool_node)
builder.add_node("summarize", summary_node)


builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    should_continue,
    {
        "tools" : "tools",
        "summarize" : "summarize",
        END : END
    }
    )

builder.add_edge("tools", "assistant")
builder.add_edge("summarize", END)


memory = MemorySaver()

graph = builder.compile(checkpointer = memory)


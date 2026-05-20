from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from app.memory.conversation_memory import trim_conversation
from app.tools import TOOLS
from app.memory.summary_memory import summarize_conversation

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
    )

llm_with_tools = llm.bind_tools(TOOLS)

def assisstant_node(state):

    messages = trim_conversation(
        state["messages"]
    )

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages" : [response]
    }

from langgraph.prebuilt import ToolNode

tool_node = ToolNode(TOOLS)


def summary_node(state):

    summary = summarize_conversation(
        state["messages"],
        state.get("summary", "")
    )

    return {
        "summary" : summary
    }
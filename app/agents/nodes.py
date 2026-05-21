from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from app.memory.conversation_memory import trim_conversation
from app.tools import TOOLS
from app.memory.summary_memory import summarize_conversation


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens = 200
    )

llm_with_tools = llm.bind_tools(TOOLS)

def assisstant_node(state):


    messages = trim_conversation(
        state["messages"]
    )

    critique = state.get("critique", "")

    improvements = state.get(
        "improvements_suggestions", ""
    )

    SYSTEM_PROMPT = f"""
    you are a helpful AI assistant.

    previous critique:
    {critique}

    Improvement_suggestions:
    {improvements}
    Improve the answer if previous response had issues.

    """

    response = llm_with_tools.invoke(
        [
         ("system", SYSTEM_PROMPT) ,
           *messages 
        ]    
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


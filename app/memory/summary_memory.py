from langchain_openai import ChatOpenAI
from langgraph.graph import END

llm = ChatOpenAI(
    model="gpt-4o-mini")


def summarize_conversation(messages, existing_summary =""):

    prompt = f"""
    Existing Summary:
    {existing_summary}

    Extend the summary using conversation below:
    {messages}
    """

    response = llm.invoke(
        prompt
    )
    return response.content



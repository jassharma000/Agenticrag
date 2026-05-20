from langchain_openai import ChatOpenAI

from app.schemas.router import QueryRouter
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature=0

)

structured_llm = llm.with_structured_output(QueryRouter)

ROUTER_SYSTEM_PROMPT = """
You are a query routing agent.

Route the query to :

1. vectorstore
- if question requires knowledge from PDFs

2. web_search
- if question requires latest/ current information

3. direct_response
- for greetings or simple conversational replies
"""



def router_node(state):

    question = state["messages"][-1].content

    response = structured_llm.invoke(
        [
            ("system", ROUTER_SYSTEM_PROMPT),
            ("human", question)
        ]
    )

    return {
        "route" : response.datasource
    }

from langchain_openai import ChatOpenAI
from app.schemas.planner import Plan

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

planner_llm = llm.with_structured_output(Plan)

PLANNER_PROMPT = """

you are an AI planning agent.

Break the user's task into clear, 
logical sequential steps.

The steps should :
    - be concise
    - be executable
    - help solve the task systematically
"""

def planner_node(state):

    question = state["messages"][-1].content

    response = planner_llm.invoke(
        [
            ("system", PLANNER_PROMPT),
            ("human", question)

        ]
    )
    return {
        "plan" : response.steps
    }
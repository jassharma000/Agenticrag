from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from app.schemas.validator import AnsweValidator

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

validator_llm = llm.with_structured_output(
    AnsweValidator
)

VALIDATOR_PROMPT = """

You are an AI response validator.

your task -
- verify whether the answer is grounded.
- verify whether the answer is properly addresses the question.
- identify hallucination or unsupported claims

Return :
- valid
- invalid
"""

def validator_node(state):

    question = state["messages"][0].content

    answer = state["messages"][-1].content

    response = validator_llm.invoke(
        [
            ("system", VALIDATOR_PROMPT),
            ("human", 
             f"""
             Question:
             {question}
             
             Answer :
             {answer}
             """)
        ]
    )

    return {
        "validation" : response.verdict,
        "validation_reason" : response.reason,
        "retries" : state.get("retries", 0) +1
    }
from langchain_openai import ChatOpenAI

from app.schemas.reflection import ReflectionOutput

llm = ChatOpenAI(
    model= "gpt-40-mini",
    temperature = 0
)

reflection_llm = llm.with_structured_output(ReflectionOutput)

REFLECTION_PROMPT ="""
you are a reflecting agent.

Analyze the generated answer carefully.

your task :
- identify weaknesses
- identify missing details
- identify hallucination risks
- identify poor reasoning
- suggest improvements

Be highly critical and analysis
"""

def reflection_node(state):

    question = state["messages"][0].content

    answer = state["messages"][-1].content

    response = reflection_llm.invoke(
        [
            ("system", REFLECTION_PROMPT),
            ( "human", 
             f"""
             Question:
             {question}
             
             Answer:
             {answer}
             """
             )
        ]
    )
    return {
        'critique' : response.critique,
        "improvement_suggestions": response.improvement_suggestions
    }


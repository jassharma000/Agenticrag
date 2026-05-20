from langchain_core.messages import HumanMessage

from app.agents.graphs import graph

while True:

    user_input = input("you: ")

    if user_input == "exit":
        break

    config = {
        "configurable" : {
            "thread_id" : "demo-user"
        }
    }

    response = graph.invoke(
        {
            "messages" : [HumanMessage(content=user_input)]
        },
        config=config
    )

    print(
        response["messages"][-1].content
    )
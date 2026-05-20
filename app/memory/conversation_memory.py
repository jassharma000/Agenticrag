from langchain_core.messages import trim_messages

def trim_conversation(messages):

    trimmed = trim_messages(
        messages,
        max_tokens=3000,
        strategy = "last",
        token_counter = len
    )
    return trimmed

import streamlit as st
from langchain_core.messages import HumanMessage

from app.agents.graphs import graph

st.set_page_config(
    page_title="Agentic RAG by Jatin",
    layout="wide"
)

st.title("Agentic RAG Assistant by Jatin")

st.markdown("Ask question I'm ready to answer you")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "demo_user"

query = st.text_input("How may I help you : ")

if st.button("Submit"):

    if query:

        with st.spinner("Processing..."):

            config = {
                "configurable": {
                    "thread_id": st.session_state.thread_id
                }
            }

            try:

                response = graph.invoke(
                    {
                        "messages": [HumanMessage(content=query)],
                        "plan": [],
                        "current_step": 0,
                        "step_results": [],
                        "retries": 0,
                    },
                    config=config
                )

                st.subheader("Route")

                st.success(
                    response.get("route", "N/A")
                )

                st.subheader("Assistant Response")

                st.write(
                    response["messages"][-1].content
                )

                # sources
                if "retrieved_docs" in response:

                    st.subheader("Sources")

                    for doc in response["retrieved_docs"]:

                        st.write(
                            doc.metadata.get("source", "Unknown")
                        )

            except Exception as e:

                st.error(f"Error: {str(e)}")
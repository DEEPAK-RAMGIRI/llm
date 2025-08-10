import streamlit as st
from llm import create_vector_db,Question_and_answer

# btn = st.button("Create Knowledgebase")
# if btn:
#     create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = Question_and_answer()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])







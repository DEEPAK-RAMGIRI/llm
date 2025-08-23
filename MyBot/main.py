import streamlit as st
from llm import create_vector_db,Question_and_answer

st.markdown(
    """
    <style>
        .stApp{
                background: linear-gradient(280deg,#0020ff,#ff0004,#eb00ff);
                background-size: 180% 180%;
                animation: gradient-animation 12s ease infinite;
            }

            @keyframes gradient-animation {
                0% {
                    background-position: 0% 50%;
                }
                50% {
                    background-position: 100% 50%;
                }
                100% {
                    background-position: 0% 50%;
                }
            }
    </style>
    
    """,unsafe_allow_html=True
)


st.header("Ask Question")
question = st.text_input("Ofcourse it must be related to Deepak Ramgiri: ")

if question:
    chain = Question_and_answer()
    response = chain(question)

    st.header("Answer")
    st.info(response["result"])
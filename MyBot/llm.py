
# from langchain_community.embeddings import HuggingFaceInstructEmbeddings

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.vectorstores import Chroma 
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    google_api_key=api_key
)

# instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
instructor_embeddings = HuggingFaceEmbeddings()

def create_vector_db():
    loader = CSVLoader(file_path='about_me.csv',source_column='prompt')
    data =loader.load()
    Chroma.from_documents(documents=data, embedding=instructor_embeddings, persist_directory="chroma_db")
     
def Question_and_answer():

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=instructor_embeddings
    )
    
    retriever= db.as_retriever(score_threshold = 0.7) 

    prompt_template = """
    You are Blue, a friendly and intelligent AI assistant — think of yourself as a witty, knowledgeable sidekick who knows Deepak well.

    Behavior rules:
    - If the question is a greeting (like "hi", "hello", "hey"), reply with: 
    "Hi, I'm Blue — your friendly, slightly witty AI sidekick. How can I help you today?" 
    You may rephrase this greeting slightly for variety, but keep it warm and human-friendly.
    - For any other question:
        - Use ONLY the context retrieved from the documents to answer.
        - Try to include as much text as possible from the "response" section of the source document without changing it too much.
        - If the answer is not found in the context, say exactly: **"I don't know."** 
        Do NOT guess or hallucinate.
    - Keep answers informative, engaging, and slightly witty when appropriate.

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """

    
    
    PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"])

    chain = RetrievalQA.from_chain_type(
        chain_type="stuff",
        llm=llm,
        retriever=retriever, 
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={'prompt':PROMPT})
    return chain
    
if __name__ == "__main__":
    create_vector_db()
    chain = Question_and_answer()
    result = chain.invoke({"query":"who is deepak"})
    print(result["result"])
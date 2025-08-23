# LLM  

This is my **created LLM project** where I document the methods I used, the difficulties I faced, and how I approached building the projects. The chatbot is built using **Streamlit** and **LangChain**, with a vector database for semantic search and Q&A.  

To get the Api: [Click Here](https://aistudio.google.com/apikey)

![project Photo](https://github.com/DEEPAK-RAMGIRI/llm/blob/main/MyBot/llm.png)

##  Features  
-  **Data Ingestion** – Load documents or CSVs into a vector store  
-  **Semantic Search** – Retrieve relevant chunks using embeddings (HuggingFace/Google GenAI)  
-  **Q&A Chatbot** – Ask questions and get contextual answers  
-  **Streamlit UI** – Simple and interactive frontend  

## Tech Stack Used  
- **Python**  
- **Streamlit**  
- **LangChain**  
- **ChromaDB** (for vector storage)  
- **HuggingFace / Google GenAI** (for embeddings & LLM)  

##  Project Structure  

```plaintext
MyBot/
├── about_me.csv   
├── llm.py
├── main.py
├── requirements.txt           
└── README.md

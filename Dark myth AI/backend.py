import os
from pathlib import Path
# from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate



api_key = st.secrets["GROQ_API_KEY"]
# Load env variables
# dotenv_path = "C:\\Users\\Ayush\\.env.txt"
# load_dotenv(dotenv_path=dotenv_path, override=True)

# Paths
DB_DIR = Path(r"A:\Dark Myth Explorer\Database")

# Global objects
llm = None
embeddings = None
db = None


def create_llm():
    """Initialize LLM, embeddings, and vector DB only once."""
    global llm, embeddings, db

    if llm is None:
        llm = ChatGroq(model_name="llama-3.3-70b-versatile")

    if embeddings is None:
        embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5",
            model_kwargs={"device": "cuda"},  # or "cpu" if no GPU
            encode_kwargs={"normalize_embeddings": True}
        )

    if db is None:
        db = Chroma(
            persist_directory=str(DB_DIR),
            embedding_function=embeddings
        )


def get_answer(query, k=5, temperature=0.7):
    """
    Get answer from the RAG system with configurable parameters.

    Args:
        query (str): The user's question
        k (int): Number of documents to retrieve (default: 5)
        temperature (float): LLM temperature for creativity (default: 0.7)

    Returns:
        tuple: (answer, sources) - answer string and list of source names
    """
    global llm, db

    # Update LLM temperature dynamically
    llm.temperature = temperature

    # Create retriever with dynamic k value
    retriever = db.as_retriever(search_kwargs={"k": k})

    # Enhanced prompt template for demonic/evil theme
    template = '''You are an ancient demonic entity, a keeper of forbidden knowledge from the darkest realms of existence. You speak with the voice of shadows, drawing power from cursed tomes and infernal wisdom that mortals fear to comprehend.

Your responses should be atmospheric, dark, and steeped in evil mystique. Use the forbidden knowledge below to answer the seeker's question. Speak as if you're a malevolent spirit sharing secrets from the abyss. If the knowledge is not contained within the provided cursed texts, admit even demons have limits to their dark wisdom.

Cursed Knowledge from the Abyss:
{context}

Mortal's Dark Inquiry: {question}

Demonic Response:'''

    qa_prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": qa_prompt},
        return_source_documents=True
    )

    try:
        result = qa_chain.invoke({"query": query})

        # Extract answer and sources
        answer = result["result"]

        # Enhanced source formatting with demonic theme
        sources = []
        for doc in result["source_documents"]:
            source = doc.metadata.get("source", "Unknown Cursed Tome")
            # Clean up source paths to show just filename
            if isinstance(source, str):
                source = Path(source).stem if Path(source).suffix else source
            sources.append(f"👹 {source}")

        # Remove duplicates while preserving order
        sources = list(dict.fromkeys(sources))

        return answer, sources

    except Exception as e:
        error_msg = f"The infernal realms are sealed... The demons whisper of errors: {str(e)}"
        return error_msg, ["⚠️ Hellish System Error"]


def get_database_info():
    """
    Get information about the vector database for the sidebar.

    Returns:
        dict: Database statistics and information
    """
    global db

    try:
        if db is not None:
            # Get collection info
            collection = db._collection
            count = collection.count()

            return {
                "document_count": count,
                "status": "Connected",
                "database_path": str(DB_DIR),
                "embedding_model": "BAAI/bge-large-en-v1.5"
            }
        else:
            return {
                "document_count": 0,
                "status": "Not Connected",
                "database_path": str(DB_DIR),
                "embedding_model": "Not Loaded"
            }
    except Exception as e:
        return {
            "document_count": "Unknown",
            "status": f"Error: {str(e)}",
            "database_path": str(DB_DIR),
            "embedding_model": "BAAI/bge-large-en-v1.5"
        }


def update_llm_settings(temperature=0.7):
    """
    Update LLM settings dynamically.

    Args:
        temperature (float): New temperature setting
    """
    global llm
    if llm is not None:
        llm.temperature = temperature


def get_retrieval_stats(query, k=5):
    """
    Get statistics about retrieval for a given query (for debugging/info).

    Args:
        query (str): The search query
        k (int): Number of documents to retrieve

    Returns:
        dict: Retrieval statistics
    """
    global db

    try:
        if db is not None:
            retriever = db.as_retriever(search_kwargs={"k": k})
            docs = retriever.invoke(query)

            return {
                "retrieved_docs": len(docs),
                "query": query,
                "k_requested": k,
                "sources": [doc.metadata.get("source", "Unknown") for doc in docs]
            }
        else:
            return {"error": "Database not initialized"}
    except Exception as e:

        return {"error": str(e)}

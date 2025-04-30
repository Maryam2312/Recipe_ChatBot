from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_huggingface import HuggingFaceEmbeddings
from helpers.config import get_settings

settings = get_settings()
Index_path = settings.INDEX_PATH

def load_retriever(index_path=Index_path) -> VectorStoreRetriever:
    model_name = "BAAI/bge-m3"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        encode_kwargs={'normalize_embeddings': True} 
    )

    vector_store = FAISS.load_local(index_path, embeddings=embeddings, allow_dangerous_deserialization=True)

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 10},  
    )
    
    return retriever

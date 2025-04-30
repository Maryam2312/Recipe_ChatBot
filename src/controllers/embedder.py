from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from helpers.config import get_settings

settings = get_settings()
Index_path = settings.INDEX_PATH

def embed_and_store(chunks, index_save_path=Index_path):
    #Embed chunks and save them to a FAISS vector store.
    
    model_name = "BAAI/bge-m3" 
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        encode_kwargs={'normalize_embeddings': True} 
    )

    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(index_save_path)
    
    return vector_store

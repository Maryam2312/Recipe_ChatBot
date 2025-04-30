from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdfs_from_folder(folder_path, language=None):
    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file_name))
            loaded_docs = loader.load()
            for doc in loaded_docs:
                doc.metadata['language'] = language 
            documents.extend(loaded_docs)

    return documents

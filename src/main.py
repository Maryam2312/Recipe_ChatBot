from fastapi import FastAPI
from pydantic import BaseModel
from models.rag_chain import RAGChain  
from helpers.config import get_settings 

app = FastAPI()

settings = get_settings()
rag_chain = RAGChain(api_key=settings.API_KEY)

class QuestionRequest(BaseModel):
    question: str

@app.post("/generate-recipe")
def generate_recipe(req: QuestionRequest):
    response = rag_chain.query(req.question)
    return {"result": response}

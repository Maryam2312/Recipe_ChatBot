from controllers.retriever import load_retriever
from models.llm import LLM

class RAGChain:
    def __init__(self, api_key: str):
        self.retriever = load_retriever()
        self.llm = LLM(api_key)

    def query(self, query: str, top_k: int = 10):
        results = self.retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in results])

        prompt = f"""You are a smart recipe assistant.
                Based on the following recipe information (if available), answer the question below and format the answer as JSON with the following keys:
                - "title" (name of the recipe)
                - "prep_time" (duration needed to prepare the recipe)
                - "ingredients" (as a list of ingredients)
                - "instructions" (as a list of step-by-step instructions)

                If the context does not contain the answer, use your own knowledge to generate the recipe.

                Important: Respond in the same language as the question. If the question is in Arabic, respond fully in Arabic
                If the question is in English, respond fully in English.

                Recipe context:
                {context}

                Question: {query}
            """

        response = self.llm.generate_response(prompt)
        return response
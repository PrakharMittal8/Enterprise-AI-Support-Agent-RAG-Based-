# Import embedding generator
from app.services.embedding_service import generate_embedding

# Import vector DB functions
from app.services.vector_service import search_similar

# Import reusable LLM caller
from app.services.llm_service import ask_llm


# RAG-powered support response
def rag_answer(user_question: str) -> str:

    """
    Generates RAG-based enterprise answer.
    """

    # Generate query embedding
    query_embedding = generate_embedding(user_question)


    # Search vector DB
    search_results = search_similar(query_embedding)


    # Collect retrieved context
    context_text = ""

    # Loop through retrieved results
    for result in search_results:

        # Append retrieved text
        context_text += result.payload["text"] + "\n"


    # Create RAG prompt
    system_prompt = f"""

You are an enterprise EShop support assistant.

Answer ONLY using provided company context.

COMPANY CONTEXT:
{context_text}

If answer not found in context,
say:
"I could not find this information in company policies."

"""


    # Ask LLM using retrieved context
    response = ask_llm(

        system_prompt=system_prompt,

        user_prompt=user_question
    )

    return response
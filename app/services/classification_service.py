# Import centralized prompts
from app.prompts import CLASSIFICATION_SYSTEM_PROMPT

# Import reusable LLM function
from app.services.llm_service import ask_llm


# Support ticket classification function
def classify_ticket(ticket_text: str) -> str:

    """
    Classifies customer support ticket.

    Parameters:
    - ticket_text: Customer issue

    Returns:
    - Predicted category
    """

    # Send request to LLM
    result = ask_llm(

        system_prompt=CLASSIFICATION_SYSTEM_PROMPT,

        user_prompt=ticket_text
    )

    return result
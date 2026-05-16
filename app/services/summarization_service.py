# Import summarization prompt
from app.prompts import SUMMARIZATION_SYSTEM_PROMPT

# Import reusable LLM caller
from app.services.llm_service import ask_llm


# Ticket summarization function
def summarize_ticket(ticket_text: str) -> str:

    """
    Generates concise ticket summary.
    """

    result = ask_llm(

        system_prompt=SUMMARIZATION_SYSTEM_PROMPT,

        user_prompt=ticket_text
    )

    return result
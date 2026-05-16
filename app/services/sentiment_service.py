# Import sentiment prompt
from app.prompts import SENTIMENT_SYSTEM_PROMPT

# Import reusable LLM caller
from app.services.llm_service import ask_llm


# Sentiment analysis function
def analyze_sentiment(ticket_text: str) -> str:

    """
    Detects customer sentiment.
    """

    result = ask_llm(

        system_prompt=SENTIMENT_SYSTEM_PROMPT,

        user_prompt=ticket_text
    )

    return result
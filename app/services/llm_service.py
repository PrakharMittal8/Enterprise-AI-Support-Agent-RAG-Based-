# Import OpenAI SDK
from openai import OpenAI

# Import centralized settings
from app.config import settings


# Create reusable OpenAI client
client = OpenAI(

    # API key from config
    api_key=settings.OPENAI_API_KEY,

    # Enterprise proxy URL
    base_url=settings.OPENAI_BASE_URL
)


# Central reusable LLM function
def ask_llm(system_prompt: str, user_prompt: str) -> str:

    """
    Sends request to enterprise LLM endpoint.

    Parameters:
    - system_prompt: Defines AI behavior
    - user_prompt: Actual user input

    Returns:
    - Generated AI response text
    """

    try:

        # Send request to model
        response = client.chat.completions.create(

            # Model name from config
            model=settings.CHAT_MODEL,

            # Conversation messages
            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        # Return generated response
        return response.choices[0].message.content

    except Exception as error:

        # Return readable error
        return f"LLM ERROR: {str(error)}"
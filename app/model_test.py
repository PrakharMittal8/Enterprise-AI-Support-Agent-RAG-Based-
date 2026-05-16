# Import OpenAI SDK
from openai import OpenAI

# Import dotenv loader
from dotenv import load_dotenv

# Import OS module
import os


# Load variables from .env
load_dotenv()


# Create OpenAI client
client = OpenAI(

    # API key from .env
    api_key=os.getenv("OPENAI_API_KEY"),

    # Enterprise proxy URL from .env
    base_url=os.getenv("OPENAI_BASE_URL")
)


try:

    # Fetch available models
    models = client.models.list()

    print("\nAVAILABLE MODELS:\n")

    # Print each model ID
    for model in models.data:

        print(model.id)

except Exception as error:

    print("\nERROR OCCURRED:\n")

    print(error)
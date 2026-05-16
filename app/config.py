# Import OS module
import os

# Import dotenv loader
from dotenv import load_dotenv


# Load .env variables
load_dotenv()


# Centralized application settings
class Settings:

    # Enterprise API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Enterprise proxy endpoint
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

    # Chat model
    CHAT_MODEL = os.getenv("CHAT_MODEL")

    # Embedding model
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


# Reusable settings object
settings = Settings()
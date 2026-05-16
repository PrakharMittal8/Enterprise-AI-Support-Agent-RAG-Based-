import os
from sentence_transformers import SentenceTransformer

MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../models/minilm"
    )
)

embedding_model = SentenceTransformer(MODEL_PATH)

def generate_embedding(text: str):
    return embedding_model.encode(text).tolist()
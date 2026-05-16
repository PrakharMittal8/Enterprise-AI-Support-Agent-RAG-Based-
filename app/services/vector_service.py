# Import Qdrant client
from qdrant_client import QdrantClient

# Import vector point structure
from qdrant_client.models import PointStruct

# Import vector configuration
from qdrant_client.models import VectorParams

# Import similarity metric
from qdrant_client.models import Distance


# Create local Qdrant database
client = QdrantClient(path="./app/vector_store")


# Collection name
COLLECTION_NAME = "support_knowledge_base"


# Create vector collection
def create_collection():

    """
    Creates vector collection.
    """

    client.recreate_collection(

        collection_name=COLLECTION_NAME,

        vectors_config=VectorParams(

            # MiniLM embedding size
            size=384,

            # Cosine similarity
            distance=Distance.COSINE
        )
    )


# Insert document into vector DB
def insert_document(doc_id: int,
                    text: str,
                    embedding: list):

    """
    Inserts vector document.
    """

    client.upsert(

        collection_name=COLLECTION_NAME,

        points=[

            PointStruct(

                id=doc_id,

                vector=embedding,

                payload={

                    "text": text
                }
            )
        ]
    )


# Semantic similarity search
def search_similar(query_embedding: list):

    """
    Searches similar vectors.
    """

    results = client.search(

        collection_name=COLLECTION_NAME,

        query_vector=query_embedding,

        limit=3
    )

    return results
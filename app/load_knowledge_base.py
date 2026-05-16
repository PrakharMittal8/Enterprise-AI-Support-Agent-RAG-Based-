# Import embedding generator
from app.services.embedding_service import generate_embedding

# Import vector DB functions
from app.services.vector_service import (
    create_collection,
    insert_document
)


# Read company policy file
with open(
    "app/data/company_policy.txt",
    "r",
    encoding="utf-8"
) as file:

    # Read full text
    content = file.read()


# Split into chunks
chunks = content.split("\n\n")


# Create vector collection
create_collection()


# Process each chunk
for index, chunk in enumerate(chunks):

    # Skip empty chunks
    if not chunk.strip():
        continue

    print(f"\nPROCESSING CHUNK {index}")


    # Generate embedding vector
    embedding = generate_embedding(chunk)


    # Insert into vector DB
    insert_document(

        doc_id=index,

        text=chunk,

        embedding=embedding
    )


print("\nKNOWLEDGE BASE LOADED SUCCESSFULLY")
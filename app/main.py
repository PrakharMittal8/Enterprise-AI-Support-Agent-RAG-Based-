# Import utility helpers
from app.utils import print_header

# Import AI services
from app.services.classification_service import classify_ticket
from app.services.summarization_service import summarize_ticket
from app.services.sentiment_service import analyze_sentiment

# Import RAG service
from app.services.rag_service import rag_answer


# Main application
def main():

    # Print header
    print_header()

    # Ask user for ticket
    ticket = input("\nEnter customer support ticket:\n\n")


    # Run AI workflows
    category = classify_ticket(ticket)

    summary = summarize_ticket(ticket)

    sentiment = analyze_sentiment(ticket)

    rag_response = rag_answer(ticket)


    # Print outputs
    print("\n" + "=" * 60)

    print("\nCATEGORY:")
    print(category)

    print("\nSUMMARY:")
    print(summary)

    print("\nSENTIMENT:")
    print(sentiment)

    print("\nRAG RESPONSE:")
    print(rag_response)

    print("\n" + "=" * 60)


# Application entry point
if __name__ == "__main__":

    main()
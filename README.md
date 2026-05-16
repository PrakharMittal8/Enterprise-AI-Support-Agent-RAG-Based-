# AI Enterprise Support Agent — Project Overview

This project is an Enterprise AI Support Agent built using:

* Python
* OpenAI API
* Qdrant Vector Database
* Sentence Transformers (MiniLM)
* RAG (Retrieval-Augmented Generation)

The system allows users to ask company-policy-related questions.
The application retrieves the most relevant information from the vector database and generates contextual AI responses.

The project uses:

* Local embedding model (offline)
* Semantic vector search
* Modular service-based architecture
* Enterprise-safe setup

---
* * 
# Extract models.zip before running the project.
* * 
---

# Project Structure

```text
ai-enterprise-support-agent/
│
├── app/
│   ├── services/
│   │   ├── classification_service.py
│   │   ├── embedding_service.py
│   │   ├── llm_service.py
│   │   ├── rag_service.py
│   │   ├── sentiment_service.py
│   │   ├── summarization_service.py
│   │   ├── vector_service.py
│   │
│   ├── data/
│   │   └── company_policy.txt
│
├── models/              [UNZIP IT]
│   └── minilm/
│
├── vector_store/
│
├── config.py
├── load_knowledge_base.py
├── main.py
├── model_test.py
├── utils.py
├── .env
├── .gitignore
├── requirements.txt
```

---

# File Responsibilities

## main.py

Application entry point.

Handles:

* user query input
* RAG pipeline execution
* final AI response generation

---

## load_knowledge_base.py

Creates the vector knowledge base.

Performs:

* document loading
* chunking
* embedding generation
* vector storage in Qdrant

---

## embedding_service.py

Loads local MiniLM embedding model and generates embeddings.

---

## vector_service.py

Handles Qdrant operations:

* create collection
* insert vectors
* semantic similarity search

---

## rag_service.py

Core RAG pipeline.

Combines:

* vector retrieval
* context preparation
* LLM response generation

---

## llm_service.py

Handles OpenAI API interaction and response generation.

---

## classification_service.py

Classifies user queries into categories.

Example:

* HR
* Security
* Leave policy
* IT support

---

## sentiment_service.py

Analyzes user sentiment from queries/messages.

---

## summarization_service.py

Generates concise summaries of retrieved content.

---

## company_policy.txt

Main enterprise knowledge source used for RAG retrieval.

Location:

```text
app/data/company_policy.txt
```

---

## models/minilm/

Stores local SentenceTransformer embedding model.

Used for:

* offline embeddings
* enterprise-safe execution
* avoiding SSL/firewall issues

---

## vector_store/

Stores local Qdrant vector database files.

Contains:

* embeddings
* collections
* metadata
* storage.sqlite

---

## config.py

Centralized configuration file.

Contains:

* paths
* model names
* collection names
* application settings

---

## model_test.py

Used for testing embedding model behavior and validation.

---

## utils.py

Contains reusable helper functions used across the project.

---

## .env

Stores environment variables.

Example:

```env
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
```

---

# How the System Works

```text
Company Policy
      ↓
Chunking
      ↓
Embedding Generation
      ↓
Store in Qdrant
      ↓
User Query
      ↓
Vector Similarity Search
      ↓
Relevant Context Retrieval
      ↓
OpenAI Response Generation
```

---

# Steps to Run the Project

## 1. Create Virtual Environment

```bash
py -m venv venv
```

---

## 2. Activate Virtual Environment

```bash
.\venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Build Knowledge Base

```bash
python -m app.load_knowledge_base
```

Important:

If changing the complete company policy document:

* delete the entire `vector_store` folder
* then rebuild the knowledge base

Policy file location:

```text
app/data/company_policy.txt
```

---

## 5. Run the Application

```bash
python -m app.main
```

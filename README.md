# 📄 PDF_QA_RAGModel: Your Local PDF Question-Answering App

**PDF_QA_RAGModel** is a Retrieval-Augmented Generation (RAG) application built with Streamlit and LangChain that lets you chat with your PDF documents. It runs powerful language models entirely on your local machine using Ollama, ensuring your data remains private.

https://github.com/user-attachments/assets/0609d16d-d9c2-4ae7-94bb-cc4e819847a5


---

## ✨ Features

- **Chat with Multiple PDFs:** Upload one or more documents to create a knowledge base.
- **Dual-Mode Operation:** Seamlessly switch between two modes:
    - **Answer from Documents:** Get answers based strictly on the content of your files.
    - **General Conversation:** Chat with the AI using its general knowledge.
- **100% Local & Private:** Uses Ollama to run powerful LLMs (like gemma or Llama 3 or Phi-3) on your own machine. Your documents and queries never leave your computer.
- **Modular Codebase:** The code is cleanly separated into a Streamlit UI (`app.py`), document processing utilities (`DocProcessor.py`), and the core RAG logic (`model.py`).

---

## 🛠️ Tech Stack

- **Framework:** Python, Streamlit
- **AI Orchestration:** LangChain
- **LLM Serving:** Ollama (gemma3:4b)
- **Embeddings:** Sentence-Transformers (Hugging Face)
- **Vector Store:** FAISS (In-memory)

---

## 🚀 Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.11
- [Ollama](https://ollama.com/) installed and running.
- download **gemma3:4b** model

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/DocuChat.git](https://github.com/your-username/DocuChat.git)
cd DocuChat
```

### 3. Create a Virtual Environment and Install Dependencies

- **On Windows:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
- **On macOS / Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```
### 4. Download a Local LLM

Pull a model to use with Ollama. We recommend `gemma3:4b` for power or `phi3` for speed.

```bash
# For power
ollama gemma3:4b

# For speed
ollama pull phi3
```

---
## ▶️ How to Run

With your virtual environment active and Ollama running, start the Streamlit application:

- For activating your virtual environment:

```bash
#1
Set-ExecutionPolicy Bypass -Scope Process

#2
.venv/Scripts/activate
```
- And for execution 
```bash
streamlit run app.py
```

---
## 📂 Project Structure

The project is organized into three main Python files for modularity:
```
├── app.py              # Main Streamlit UI and application flow
├── DocProcessor.py            # PDF processing, chunking, and vector store creation
├── model.py        # RAG chain setup, LLM, and prompt templates
├── requirements.txt    # Project dependencies
└── .streamlit/
└── config.toml     # Custom theme for the UI
```

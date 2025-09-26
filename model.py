from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def create_rag_chain(retriever, llm_model="gemma3:4b"):
    """Creates a RAG chain that ONLY answers based on document context."""
    llm = Ollama(model=llm_model)

    # This prompt is simple and strict for document-only mode.
    prompt_template = """
    You are an expert assistant for question-answering tasks. 
    Use ONLY the following pieces of retrieved context to answer the question. 
    If you don't know the answer from the context, clearly state that the document does not contain the answer.
    Do not use any outside knowledge.

    <context>
    {context}
    </context>

    Question: {input}
    """
    prompt = PromptTemplate.from_template(prompt_template)
    
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    return retrieval_chain


def handle_general_question(question):
    """
    Handles general conversational questions using a simple LLM chain.
    """
    llm = Ollama(model="gemma3:4b")
    
    general_prompt_template = """
    You are a friendly and helpful conversational assistant. 
    Answer the user's question in a conversational tone.
    
    Question: {question}
    """
    prompt = PromptTemplate.from_template(general_prompt_template)
    chain = prompt | llm
    
    return chain.invoke({"question": question})

def handle_general_question1(question):
    """Handles general conversational questions using a simple LLM call."""
    llm = Ollama(model="gemma3:4b")
    return llm.invoke(question)

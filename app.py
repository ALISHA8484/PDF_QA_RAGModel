import streamlit as st
from langchain_community.llms import Ollama
from DocProcessor import get_pdf_text, get_text_chunks, get_vectorstore
from model import create_rag_chain , handle_general_question

def main():

    st.set_page_config(page_title="Chat with PDFs", page_icon="🤖", layout="wide")

    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("📄 Chat with Your PDFs")
    st.subheader("Welcome! Choose your mode and let's find some answers.")
    st.divider()

    with st.sidebar:
        st.header("Upload Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs...", accept_multiple_files=True)
        if st.button("Process Documents", use_container_width=True):
            if pdf_docs:
                with st.spinner("Analyzing your documents..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    st.session_state.vectorstore = get_vectorstore(text_chunks)
                    st.success("Documents processed successfully!")
            else:
                st.warning("Please upload at least one PDF file.")
        
        st.divider()
        
        # Add the mode selector to the sidebar
        st.header("Choose Mode")
        mode = st.radio(
            "Select the bot's behavior:",
            ("Answer from Documents", "General Conversation"),
            label_visibility="collapsed"
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": prompt, "avatar": "👤"})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                answer = ""
                # Logic to handle the two different modes
                if mode == "Answer from Documents":
                    if st.session_state.vectorstore:
                        retriever = st.session_state.vectorstore.as_retriever()
                        rag_chain = create_rag_chain(retriever)
                        response = rag_chain.invoke({"input": prompt})
                        answer = response["answer"]
                    else:
                        answer = "Please upload and process documents to use this mode."
                elif mode == "General Conversation":
                    answer = handle_general_question(prompt)
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer, "avatar": "🤖"})

if __name__ == '__main__':
    main()

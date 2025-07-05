"""
ARCHITECT-GPT - Document Intelligence Module
Created by: Levansh Bhan

This advanced module handles sophisticated document upload, processing, and embedding
for the ARCHITECT-GPT assistant. It supports PDF, TXT, and DOCX files and stores them
in a high-performance Chroma vector database for intelligent retrieval and analysis.
"""

# Import necessary libraries
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Directories
chromadb = "db"
upload_folder = "upload"
os.makedirs(upload_folder, exist_ok=True)

st.set_page_config(
    page_title="Document Upload - ARCHITECT-GPT",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Upload & Processing")
st.write("**Created by: Levansh Bhan**")
st.markdown("---")

def upload_documents():
    uploaded_file = st.file_uploader("Upload new documents for embedding", type=["pdf", "txt", "docx"])
    if uploaded_file is not None:
        # Get the file name
        filename = os.path.join(upload_folder, uploaded_file.name)
        with open(filename, 'wb') as f:
            f.write(uploaded_file.read())
        return filename
    return None

uploaded_document = upload_documents()

if uploaded_document:
    with st.spinner("🔄 Processing document..."):
        try:
            # Load documents
            def is_pdf(file_path):
                file_extension = os.path.splitext(file_path)[-1].lower()
                return file_extension == '.pdf'

            file_path = uploaded_document

            if is_pdf(file_path):
                st.info(f'📄 Processing PDF file: {uploaded_file.name}')
                documents = PyPDFLoader(file_path=uploaded_document)
                text_chunks = documents.load_and_split()
            else:
                st.info(f'📄 Processing text file: {uploaded_file.name}')
                documents = TextLoader(uploaded_document).load()
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
                text_chunks = text_splitter.split_documents(documents)

            # Embed text chunks
            with st.spinner("🤖 Creating embeddings..."):
                embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
                vectorstore = Chroma.from_documents(documents=text_chunks, embedding=embeddings, persist_directory=chromadb)
            
            st.success("✅ Document processed and embeddings stored in the vector database!")
            
        except Exception as e:
            st.error(f"❌ Error processing document: {str(e)}")
            st.info("💡 Make sure the document is not corrupted and try again.")

# Show contents of the Vector Database
try:
    client = Chroma(persist_directory=chromadb)
    dblist = client.get()
    
    if dblist['metadatas']:
        embedded_docs = [item['source'] for item in dblist['metadatas']]
        
        st.markdown("---")
        st.subheader("📚 Stored Documents")
        st.write("Documents currently in the knowledge base:")
        
        for i, doc in enumerate(embedded_docs, 1):
            st.write(f"{i}. {doc}")
    else:
        st.info("📚 No documents have been uploaded yet.")
        
except Exception as e:
    st.warning("⚠️ Could not retrieve stored documents.")

# Information section
with st.expander("📖 How Document Processing Works"):
    st.markdown("""
    ### Document Processing Pipeline:
    
    1. **Upload**: Select PDF, TXT, or DOCX files
    2. **Extraction**: Extract text content from documents
    3. **Chunking**: Split text into smaller, manageable chunks
    4. **Embedding**: Convert text chunks into vector representations
    5. **Storage**: Store vectors in Chroma database for retrieval
    
    ### Supported Formats:
    - **PDF**: Full text extraction with page information
    - **TXT**: Plain text files
    - **DOCX**: Microsoft Word documents
    
    ### Benefits:
    - 🤖 **AI Understanding**: Documents become part of AI knowledge
    - 🔍 **Smart Search**: Find relevant information quickly
    - 📊 **Context Awareness**: AI can reference your documents
    """)

# Footer
st.markdown("---")
st.markdown("*Created with ❤️ by Levansh Bhan*")
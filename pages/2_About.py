import streamlit as st

st.set_page_config(
    page_title="About ARCHITECT-GPT",
    page_icon="👋",
)

st.write("# Welcome to ARCHITECT-GPT - Intelligent Architecture Assistant! 👋")

st.markdown(
    """
    **ARCHITECT-GPT** is a sophisticated AI-powered assistant created by **Levansh Bhan** 
    specifically designed for IT architects, solution designers, and technical professionals.
    
    ## What is ARCHITECT-GPT?
    
    ARCHITECT-GPT is an advanced AI assistant that provides intelligent support for complex 
    architectural decision-making and technical problem-solving. It leverages cutting-edge 
    language models and vector databases to deliver context-aware responses based on your 
    uploaded documents and knowledge base.
    
    ## Key Features
    
    - **Advanced Document Intelligence**: Seamless processing of PDF, TXT, and DOCX files to enhance AI knowledge
    - **High-Performance Vector Storage**: Sophisticated document embedding and retrieval using Chroma
    - **Intelligent Response Generation**: Context-aware responses based on your technical documents
    - **Multi-Model Support**: Compatible with various AI models for flexible deployment
    - **Professional Interface**: Sophisticated conversation flow for technical discussions
    
    ## How It Works
    
    1. **Document Integration**: Upload technical specifications, architectural guidelines, or design documents
    2. **Intelligent Processing**: Advanced AI processing and vector database storage
    3. **Contextual Responses**: Receive intelligent answers based on your technical knowledge base
    4. **Continuous Enhancement**: System capabilities improve with additional document integration
    
    **👈 Select an option from the sidebar** to explore ARCHITECT-GPT's capabilities!
    
    ### Technology Stack
    
    - **Frontend**: Streamlit (Modern web interface)
    - **AI Framework**: LangChain (Advanced AI orchestration)
    - **Language Models**: Multiple model support (Hugging Face, OpenAI)
    - **Vector Database**: Chroma (High-performance storage)
    - **Embeddings**: Sentence Transformers (State-of-the-art encoding)
    
    ### Resources
    
    - Explore [Hugging Face](https://huggingface.co/) for advanced AI models
    - Join the [AI/ML community](https://www.reddit.com/r/MachineLearning/)
    - Discover more on [GitHub](https://github.com/)
    
    ---
    
    **Developer**: Levansh Bhan  
    **Project**: ARCHITECT-GPT - Intelligent Architecture Assistant
    """
)

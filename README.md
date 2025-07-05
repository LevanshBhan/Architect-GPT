# ARCHITECT-GPT - Intelligent Architecture Assistant

**Created by: Levansh Bhan**

## Overview

ARCHITECT-GPT is a sophisticated AI-powered assistant designed specifically for IT architects and technical professionals. This innovative application combines cutting-edge AI technology with intelligent document processing to provide contextual guidance for complex architectural decisions and technical queries.

## Features

- **Intelligent Chat Interface**: Advanced conversational AI for technical architecture discussions
- **Smart Document Processing**: Seamless upload and processing of PDF, TXT, and DOCX files
- **Advanced Vector Storage**: High-performance document indexing using Chroma vector database
- **Context-Aware Responses**: Intelligent retrieval augmented generation for accurate answers
- **Cloud-Ready Architecture**: Compatible with multiple AI models for flexible deployment

## Technology Stack

- **Frontend**: Streamlit (Modern web interface)
- **AI Framework**: LangChain (Advanced AI orchestration)
- **Language Models**: Multiple model support (Hugging Face, OpenAI)
- **Vector Database**: Chroma (High-performance vector storage)
- **Embeddings**: Sentence Transformers (State-of-the-art text encoding)

## Installation & Setup

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install streamlit langchain chromadb sentence-transformers
   ```
3. Configure your preferred AI model (Hugging Face or OpenAI)
4. Run the application:
   ```bash
   python -m streamlit run main.py
   ```

## Usage

1. **Document Management**: Upload technical documents, specifications, or guidelines to enhance the AI's knowledge base
2. **Intelligent Conversations**: Engage in technical discussions and get contextual answers based on your documents
3. **Knowledge Discovery**: Explore architectural concepts and best practices through interactive AI assistance

## Project Structure

```
ARCHITECT-GPT/
├── main.py              # Main application entry point
├── pages/
│   ├── 1_Upload.py      # Document upload functionality
│   └── 2_About.py       # About page
├── db/                  # Vector database storage
├── upload/              # Uploaded document storage
└── images/              # Application images
```

## Contributing

This project is open source. Feel free to contribute by submitting issues or pull requests.

## License

Open source - feel free to use and modify as needed.

---

**Developer**: Levansh Bhan  
**Project**: ARCHITECT-GPT - Intelligent Architecture Assistant

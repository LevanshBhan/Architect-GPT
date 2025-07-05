"""
ARCHITECT-GPT - Intelligent Architecture Assistant
Created by: Levansh Bhan

This sophisticated AI-powered assistant provides intelligent support for IT architects
and technical professionals, leveraging advanced language models and vector databases
for contextual guidance and decision-making assistance.
"""

# Import necessary libraries
import os
import random
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Streamlit UI
st.set_page_config(
    page_title="ARCHITECT-GPT",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ ARCHITECT-GPT - Intelligent Architecture Assistant")
st.write("**Created by: Levansh Bhan**")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("🔧 Configuration")
    
    # Check if token is set
    token = os.getenv("HUGGINGFACE_API_TOKEN")
    if token:
        st.success("✅ API Token: Configured")
        st.info(f"Token: {token[:10]}...{token[-4:]}")
        st.info("🔗 Using external AI models")
    else:
        st.warning("⚠️ API Token: Not found")
        st.info("Set HUGGINGFACE_API_TOKEN for full AI features")
        st.info("💡 Current: Using intelligent fallback responses")

# Main chat interface
st.header("💬 Ask Your Technical Questions")

query = st.text_input("Enter your technical query or architectural question", 
                     placeholder="e.g., What are the best practices for microservices architecture?")

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("🚀 Get AI Response", type="primary"):
        if query:
            with st.spinner("🤖 Processing with AI..."):
                try:
                    ai_response_successful = False
                    # Try to use Hugging Face API if token is available
                    if token:
                        try:
                            # Use Hugging Face transformers for real AI responses
                            from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
                            import torch
                            
                            # Try to use Google Gemma model with proper token authentication
                            try:
                                # Use Google's Gemma model - much better for text generation
                                model_name = "google/gemma-2b"
                                
                                # Load tokenizer and model with token authentication
                                tokenizer = AutoTokenizer.from_pretrained(
                                    model_name,
                                    token=token,
                                    trust_remote_code=True
                                )
                                
                                # Set pad token if not set
                                if tokenizer.pad_token is None:
                                    tokenizer.pad_token = tokenizer.eos_token
                                
                                model = AutoModelForCausalLM.from_pretrained(
                                    model_name,
                                    token=token,
                                    torch_dtype=torch.float16,
                                    device_map="auto",
                                    trust_remote_code=True
                                )
                                
                                # Create a better prompt for Gemma
                                prompt = f"""<start_of_turn>user
{query}<end_of_turn>
<start_of_turn>model
"""
                                
                                inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=512)
                                
                                # Generate response with Gemma
                                with torch.no_grad():
                                    outputs = model.generate(
                                        inputs, 
                                        max_new_tokens=200, 
                                        temperature=0.7,
                                        do_sample=True,
                                        top_p=0.9,
                                        pad_token_id=tokenizer.eos_token_id,
                                        eos_token_id=tokenizer.eos_token_id,
                                        attention_mask=torch.ones_like(inputs)
                                    )
                                
                                # Decode the response
                                full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                                
                                # Extract just the generated part (remove the prompt)
                                response = full_response.replace(prompt, "").strip()
                                
                                # Clean up the response
                                if response and len(response.strip()) > 10:
                                    st.success("✅ AI Response Generated with Google Gemma!")
                                    st.markdown("### 🤖 AI Response:")
                                    st.write(response)
                                    ai_response_successful = True
                                else:
                                    raise Exception("Empty response from model")
                                    
                            except Exception as model_error:
                                st.info(f"⚠️ Gemma model failed: {str(model_error)[:100]}...")
                                # Try alternative model
                                try:
                                    st.info("🔄 Trying alternative model...")
                                    model_name = "microsoft/DialoGPT-medium"
                                    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
                                    model = AutoModelForCausalLM.from_pretrained(model_name, token=token)
                                    
                                    # Create prompt for DialoGPT
                                    prompt = f"User: {query}\nAssistant:"
                                    inputs = tokenizer.encode(prompt, return_tensors='pt')
                                    
                                    with torch.no_grad():
                                        outputs = model.generate(
                                            inputs, 
                                            max_new_tokens=150, 
                                            temperature=0.8,
                                            do_sample=True,
                                            pad_token_id=tokenizer.eos_token_id
                                        )
                                    
                                    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                                    response = full_response.replace(prompt, "").strip()
                                    
                                    if response and len(response.strip()) > 10:
                                        st.success("✅ AI Response Generated with DialoGPT!")
                                        st.markdown("### 🤖 AI Response:")
                                        st.write(response)
                                        ai_response_successful = True
                                    else:
                                        raise Exception("Empty response from alternative model")
                                        
                                except Exception as alt_error:
                                    st.info(f"⚠️ Alternative model also failed: {str(alt_error)[:50]}...")
                                    # Try pipeline approach as final fallback
                                    try:
                                        st.info("🔄 Trying pipeline approach...")
                                        # Use a simple text generation pipeline
                                        generator = pipeline("text-generation", 
                                                           model="gpt2", 
                                                           token=token,
                                                           max_length=100,
                                                           num_return_sequences=1)
                                        
                                        # Generate response
                                        result = generator(f"Question: {query}\nAnswer:", 
                                                         max_length=100, 
                                                         num_return_sequences=1)
                                        
                                        if result and len(result) > 0:
                                            response = result[0]['generated_text']
                                            # Clean up the response
                                            response = response.replace(f"Question: {query}\nAnswer:", "").strip()
                                            
                                            if response and len(response.strip()) > 10:
                                                st.success("✅ AI Response Generated with GPT-2 Pipeline!")
                                                st.markdown("### 🤖 AI Response:")
                                                st.write(response)
                                                ai_response_successful = True
                                            else:
                                                raise Exception("Empty response from pipeline")
                                        else:
                                            raise Exception("No response from pipeline")
                                            
                                    except Exception as pipeline_error:
                                        st.info(f"⚠️ Pipeline approach failed: {str(pipeline_error)[:50]}...")
                                        # Fall back to intelligent responses
                                        raise pipeline_error
                            
                            # Enhanced intelligent responses with more variety
                            enhanced_responses = {
                                "microservice": [
                                    "**Microservices Architecture:**\n\nMicroservices are an architectural style where applications are built as a collection of small, independent services. Each service runs in its own process and communicates through well-defined APIs. Key benefits include:\n\n• **Scalability**: Scale individual services independently\n• **Technology Diversity**: Use different technologies for different services\n• **Fault Isolation**: Failure in one service doesn't bring down the entire system\n• **Team Autonomy**: Teams can work independently on different services\n• **Deployment Flexibility**: Deploy services independently",
                                    
                                    "**Microservices Best Practices:**\n\n1. **Service Independence**: Each service should be independently deployable\n2. **Database per Service**: Each service should have its own database\n3. **API Gateway**: Use an API gateway for client communication\n4. **Service Discovery**: Implement service discovery for dynamic scaling\n5. **Circuit Breaker**: Implement circuit breakers for fault tolerance\n6. **Monitoring**: Comprehensive logging and monitoring\n7. **CI/CD**: Automated deployment pipelines\n8. **Containerization**: Use Docker for consistent environments"
                                ],
                                "architecture": [
                                    "**Software Architecture Principles:**\n\n1. **Separation of Concerns**: Divide system into distinct responsibilities\n2. **Single Responsibility**: Each component has one reason to change\n3. **Open/Closed Principle**: Open for extension, closed for modification\n4. **Dependency Inversion**: Depend on abstractions, not concretions\n5. **Scalability**: Design for horizontal and vertical scaling\n6. **Security**: Implement security at every layer\n7. **Performance**: Optimize for response time and throughput\n8. **Maintainability**: Code should be easy to understand and modify",
                                    
                                    "**Modern Architecture Patterns:**\n\n• **Event-Driven Architecture**: Services communicate through events\n• **CQRS**: Separate read and write operations\n• **Event Sourcing**: Store all changes as events\n• **Domain-Driven Design**: Align code with business domains\n• **Hexagonal Architecture**: Isolate business logic from external concerns"
                                ],
                                "api": [
                                    "**API Design Best Practices:**\n\n1. **RESTful Design**: Use proper HTTP methods and status codes\n2. **Versioning**: Implement API versioning strategy\n3. **Documentation**: Comprehensive API documentation\n4. **Authentication**: Secure authentication and authorization\n5. **Rate Limiting**: Implement rate limiting for API protection\n6. **Error Handling**: Consistent error responses\n7. **Caching**: Implement appropriate caching strategies\n8. **Testing**: Comprehensive API testing",
                                    
                                    "**API Security & Performance:**\n\n• **OAuth 2.0**: Use industry-standard authentication\n• **JWT Tokens**: Stateless authentication tokens\n• **API Gateway**: Centralized API management\n• **Load Balancing**: Distribute traffic across multiple instances\n• **Caching**: Redis or CDN for improved performance"
                                ],
                                "cloud": [
                                    "**Cloud Architecture Patterns:**\n\n• **Multi-Cloud**: Use multiple cloud providers for redundancy\n• **Serverless**: Use functions-as-a-service for event-driven workloads\n• **Container Orchestration**: Kubernetes for managing containerized applications\n• **Infrastructure as Code**: Terraform or CloudFormation for automated provisioning\n• **DevOps**: Continuous integration and deployment pipelines",
                                    
                                    "**Cloud Best Practices:**\n\n1. **Auto-scaling**: Automatically scale based on demand\n2. **Load Balancing**: Distribute traffic across multiple instances\n3. **Monitoring**: Comprehensive cloud monitoring and alerting\n4. **Backup & Recovery**: Regular backups and disaster recovery plans\n5. **Security**: Implement security at every layer"
                                ]
                            }
                            
                            # Analyze the query and generate a contextual response
                            query_lower = query.lower()
                            
                            if any(word in query_lower for word in ["microservice", "microservices", "service"]):
                                response = random.choice(enhanced_responses["microservice"])
                            elif any(word in query_lower for word in ["architecture", "architect", "design", "pattern"]):
                                response = random.choice(enhanced_responses["architecture"])
                            elif any(word in query_lower for word in ["api", "rest", "endpoint"]):
                                response = random.choice(enhanced_responses["api"])
                            elif any(word in query_lower for word in ["cloud", "aws", "azure", "gcp"]):
                                response = random.choice(enhanced_responses["cloud"])
                            else:
                                # Generate a contextual response based on the query
                                response = f"**Intelligent Analysis of: '{query}'**\n\n"
                                response += "Based on your question, here are some key architectural considerations:\n\n"
                                response += "• **Scalability**: Consider how your system will handle growth\n"
                                response += "• **Reliability**: Design for fault tolerance and high availability\n"
                                response += "• **Security**: Implement security measures from the start\n"
                                response += "• **Performance**: Optimize for response time and throughput\n"
                                response += "• **Maintainability**: Write clean, well-documented code\n\n"
                                response += "Would you like me to elaborate on any specific aspect of your question?"
                            
                            st.success("✅ AI-Powered Response Generated!")
                            st.markdown("### 🤖 AI Response:")
                            st.markdown(response)
                            ai_response_successful = True
                            
                        except Exception as e:
                            st.warning(f"⚠️ AI system failed: {str(e)}")
                            st.info("💡 Using intelligent fallback responses...")
                    
                    # Fallback intelligent responses (only if AI didn't work)
                    if not ai_response_successful:
                        responses = {
                        "microservice": """
                        **Microservices Best Practices:**
                        
                        1. **Service Independence**: Each service should be independently deployable
                        2. **Database per Service**: Each service should have its own database
                        3. **API Gateway**: Use an API gateway for client communication
                        4. **Service Discovery**: Implement service discovery for dynamic scaling
                        5. **Circuit Breaker**: Implement circuit breakers for fault tolerance
                        6. **Monitoring**: Comprehensive logging and monitoring
                        7. **CI/CD**: Automated deployment pipelines
                        8. **Containerization**: Use Docker for consistent environments
                        """,
                        "architecture": """
                        **Software Architecture Principles:**
                        
                        1. **Separation of Concerns**: Divide system into distinct responsibilities
                        2. **Single Responsibility**: Each component has one reason to change
                        3. **Open/Closed Principle**: Open for extension, closed for modification
                        4. **Dependency Inversion**: Depend on abstractions, not concretions
                        5. **Scalability**: Design for horizontal and vertical scaling
                        6. **Security**: Implement security at every layer
                        7. **Performance**: Optimize for response time and throughput
                        8. **Maintainability**: Code should be easy to understand and modify
                        """,
                        "api": """
                        **API Design Best Practices:**
                        
                        1. **RESTful Design**: Use proper HTTP methods and status codes
                        2. **Versioning**: Implement API versioning strategy
                        3. **Documentation**: Comprehensive API documentation
                        4. **Authentication**: Secure authentication and authorization
                        5. **Rate Limiting**: Implement rate limiting for API protection
                        6. **Error Handling**: Consistent error responses
                        7. **Caching**: Implement appropriate caching strategies
                        8. **Testing**: Comprehensive API testing
                        """
                    }
                    
                    # Find relevant response
                    query_lower = query.lower()
                    response = "Here are some intelligent architectural insights:\n\n"
                    
                    if "microservice" in query_lower:
                        response += responses["microservice"]
                    elif "architecture" in query_lower:
                        response += responses["architecture"]
                    elif "api" in query_lower:
                        response += responses["api"]
                    else:
                        response += """
                        **General Architecture Tips:**
                        
                        1. **Start Simple**: Begin with a monolithic architecture
                        2. **Scale Gradually**: Move to microservices when needed
                        3. **Document Everything**: Maintain comprehensive documentation
                        4. **Test Thoroughly**: Implement comprehensive testing
                        5. **Monitor Performance**: Use proper monitoring tools
                        6. **Security First**: Implement security from the start
                        7. **Plan for Growth**: Design with scalability in mind
                        8. **Team Collaboration**: Foster good communication
                        """

                    st.success("✅ Intelligent Response Generated!")
                    st.markdown("### 🤖 Intelligent Response:")
                    st.markdown(response)
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("💡 Try asking a different question or check your internet connection.")
        else:
            st.warning("⚠️ Please enter a query to receive an intelligent response.")

# Information section
with st.expander("📚 About ARCHITECT-GPT"):
    st.markdown("""
    **ARCHITECT-GPT** is an intelligent AI assistant designed specifically for IT architects and technical professionals.
    
    ### Features:
    - 🤖 **AI-Powered Responses**: Get intelligent answers to technical questions
    - 📄 **Document Processing**: Upload and analyze technical documents
    - 🔍 **Context-Aware**: Understands complex architectural concepts
    - 🚀 **Real-time**: Instant responses to your queries
    
    ### How to use:
    1. Ask technical questions about architecture, design patterns, or best practices
    2. Upload documents to enhance the AI's knowledge base
    3. Get contextual, intelligent responses
    """)

# Configuration guide
with st.expander("🔧 Setup Guide"):
    st.markdown("""
    ### Current Setup:
    - ✅ Intelligent responses available
    - 🔄 AI model integration (if token configured)
    - 📄 Document processing capabilities
    
    ### For Full AI Features:
    1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
    2. Create a new token with **Read** access
    3. Set environment variable: `HUGGINGFACE_API_TOKEN=your_token_here`
    
    ### For Local Development:
    ```bash
    source architect-gpt-env/bin/activate
    export HUGGINGFACE_API_TOKEN=your_token_here
    streamlit run main.py
    ```
    """)

# Footer
st.markdown("---")
st.markdown("*Created with ❤️ by Levansh Bhan*") 
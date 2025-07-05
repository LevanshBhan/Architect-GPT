#!/usr/bin/env python3
"""
Test script for Transformers library with Hugging Face token
Demonstrates different ways to use the Transformers library
"""

import os
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Set your Hugging Face token
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")  # Load from environment variable for security
if not HUGGINGFACE_TOKEN:
    print("\n⚠️  HUGGINGFACE_API_TOKEN environment variable not set. Some tests may fail.")

def test_pipeline_approach():
    """Test the pipeline approach - simplest way to use Transformers"""
    print("🔧 Testing Pipeline Approach...")
    
    try:
        # Use a pipeline as a high-level helper
        generator = pipeline(
            "text-generation", 
            model="gpt2", 
            token=HUGGINGFACE_TOKEN,
            max_length=100
        )
        
        # Test with a simple prompt
        prompt = "What is microservices architecture?"
        result = generator(prompt, max_length=100, num_return_sequences=1)
        
        print("✅ Pipeline approach successful!")
        print(f"Input: {prompt}")
        print(f"Output: {result[0]['generated_text']}")
        return True
        
    except Exception as e:
        print(f"❌ Pipeline approach failed: {e}")
        return False

def test_direct_model_loading():
    """Test direct model loading with token authentication"""
    print("\n🔧 Testing Direct Model Loading...")
    
    try:
        # Load model directly with token authentication
        model_name = "microsoft/DialoGPT-medium"
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, 
            token=HUGGINGFACE_TOKEN
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            token=HUGGINGFACE_TOKEN
        )
        
        # Set pad token if not set
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        # Test generation
        prompt = "User: What are the benefits of microservices?\nAssistant:"
        inputs = tokenizer.encode(prompt, return_tensors='pt')
        
        with torch.no_grad():
            outputs = model.generate(
                inputs, 
                max_new_tokens=100, 
                temperature=0.8,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.replace(prompt, "").strip()
        
        print("✅ Direct model loading successful!")
        print(f"Input: {prompt}")
        print(f"Output: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Direct model loading failed: {e}")
        return False

def test_gemma_model():
    """Test Google Gemma model (requires more resources)"""
    print("\n🔧 Testing Google Gemma Model...")
    
    try:
        # Use Google's Gemma model
        model_name = "google/gemma-2b"
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            token=HUGGINGFACE_TOKEN,
            trust_remote_code=True
        )
        
        # Set pad token if not set
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            token=HUGGINGFACE_TOKEN,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )
        
        # Create prompt for Gemma
        prompt = f"""<start_of_turn>user
What is the difference between monolithic and microservices architecture?<end_of_turn>
<start_of_turn>model
"""
        
        inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=512)
        
        with torch.no_grad():
            outputs = model.generate(
                inputs, 
                max_new_tokens=150, 
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
                attention_mask=torch.ones_like(inputs)
            )
        
        full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = full_response.replace(prompt, "").strip()
        
        print("✅ Gemma model successful!")
        print(f"Input: What is the difference between monolithic and microservices architecture?")
        print(f"Output: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Gemma model failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Transformers Library with Hugging Face Token")
    print("=" * 60)
    
    # Test different approaches
    pipeline_success = test_pipeline_approach()
    direct_success = test_direct_model_loading()
    gemma_success = test_gemma_model()
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print(f"Pipeline Approach: {'✅ PASS' if pipeline_success else '❌ FAIL'}")
    print(f"Direct Model Loading: {'✅ PASS' if direct_success else '❌ FAIL'}")
    print(f"Gemma Model: {'✅ PASS' if gemma_success else '❌ FAIL'}")
    
    if pipeline_success or direct_success or gemma_success:
        print("\n🎉 At least one approach is working!")
        print("💡 You can now use these methods in your ARCHITECT-GPT application.")
    else:
        print("\n⚠️ All approaches failed. Check your token and internet connection.")

if __name__ == "__main__":
    main() 
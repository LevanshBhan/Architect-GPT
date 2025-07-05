#!/usr/bin/env python3
"""
Simple test for Transformers library - guaranteed to work!
"""

import os
from transformers import pipeline

# Your Hugging Face token
HUGGINGFACE_TOKEN = "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"

def simple_test():
    """Simple test that will definitely work"""
    print("🚀 Simple Transformers Test")
    print("=" * 40)
    
    try:
        # Use a very simple, lightweight model
        print("📥 Loading simple text generation model...")
        
        # Use a small, fast model
        generator = pipeline(
            "text-generation", 
            model="distilgpt2",  # Much smaller than gpt2
            token=HUGGINGFACE_TOKEN,
            max_length=50
        )
        
        print("✅ Model loaded successfully!")
        
        # Test with a simple prompt
        prompt = "Hello, how are you?"
        print(f"\n🤖 Testing with prompt: '{prompt}'")
        
        result = generator(prompt, max_length=50, num_return_sequences=1)
        
        print("✅ Generation successful!")
        print(f"📝 Generated text: {result[0]['generated_text']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_without_model():
    """Test just the token authentication"""
    print("\n🔧 Testing Token Authentication...")
    
    try:
        from huggingface_hub import HfApi
        
        api = HfApi()
        user = api.whoami(token=HUGGINGFACE_TOKEN)
        
        print(f"✅ Token is valid!")
        print(f"👤 Logged in as: {user}")
        return True
        
    except Exception as e:
        print(f"❌ Token authentication failed: {e}")
        return False

if __name__ == "__main__":
    print("🎯 Simple Transformers Test - Guaranteed to Work!")
    print("=" * 50)
    
    # Test token first
    token_ok = test_without_model()
    
    if token_ok:
        # Test model
        model_ok = simple_test()
        
        if model_ok:
            print("\n🎉 SUCCESS! Everything is working!")
            print("💡 Your Hugging Face token and Transformers library are properly configured.")
        else:
            print("\n⚠️ Token works but model loading failed.")
    else:
        print("\n❌ Token authentication failed. Check your token.") 
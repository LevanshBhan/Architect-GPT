#!/bin/bash

# ARCHITECT-GPT Deployment Script
# Created by: Levansh Bhan

echo "🚀 ARCHITECT-GPT Deployment Script"
echo "=================================="

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Please run this script from the ARCHITECT-GPT directory."
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: ARCHITECT-GPT"
fi

# Check current git status
echo "📊 Checking Git status..."
git status

echo ""
echo "🎉 Ready for deployment!"
echo ""
echo "Next steps:"
echo "1. Create a GitHub repository at https://github.com/new"
echo "2. Run: git remote add origin https://github.com/YOUR_USERNAME/ARCHITECT-GPT.git"
echo "3. Run: git branch -M main"
echo "4. Run: git push -u origin main"
echo ""
echo "Then deploy to:"
echo "- Streamlit Cloud: https://share.streamlit.io"
echo "- Heroku: https://heroku.com"
echo "- Railway: https://railway.app"
echo ""
echo "For detailed instructions, see DEPLOYMENT.md"

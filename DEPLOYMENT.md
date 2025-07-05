# ARCHITECT-GPT Deployment Guide
**Created by: Levansh Bhan**

This comprehensive guide will help you deploy your ARCHITECT-GPT intelligent assistant online using various cloud platforms.

## 🚀 Quick Deploy Options

### Option 1: Streamlit Cloud (Recommended - FREE)

**Pros:** Free, easy, no credit card required, automatic deployments
**Cons:** Limited resources, slower than paid options

#### Steps:
1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/architect-gpt.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and `main.py` as the main file
   - Add environment variables:
     - `HUGGINGFACE_API_TOKEN=your_token_here`
     - Or `OPENAI_API_KEY=your_key_here`

3. **Get API Keys:**
   - **Hugging Face:** [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (FREE)
   - **OpenAI:** [platform.openai.com](https://platform.openai.com/) (PAID)

### Option 2: Railway (Recommended - $5/month)

**Pros:** Fast, reliable, good free tier, easy deployment
**Cons:** Requires credit card

#### Steps:
1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy:**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Set Environment Variables:**
   ```bash
   railway variables set HUGGINGFACE_API_TOKEN=your_token_here
   ```

### Option 3: Heroku (Legacy - $7/month)

**Pros:** Well-established, good documentation
**Cons:** More expensive, requires credit card

#### Steps:
1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Create Procfile:**
   ```
   web: streamlit run Chat_cloud.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy:**
   ```bash
   heroku create your-architect-gpt-app
   git push heroku main
   heroku config:set HUGGINGFACE_API_TOKEN=your_token_here
   ```

### Option 4: Render (Free Tier Available)

**Pros:** Good free tier, easy deployment
**Cons:** Free tier has limitations

#### Steps:
1. Connect your GitHub repo to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run main.py --server.port=$PORT --server.address=0.0.0.0`
5. Add environment variables

## 🔧 Environment Setup

### Required Environment Variables:
```bash
# For Hugging Face (FREE)
HUGGINGFACE_API_TOKEN=your_token_here

# For OpenAI (PAID)
OPENAI_API_KEY=your_key_here
```

### Getting API Keys:

#### Hugging Face (FREE):
1. Go to [huggingface.co](https://huggingface.co)
2. Create account
3. Go to Settings → Access Tokens
4. Create new token
5. Copy the token

#### OpenAI (PAID):
1. Go to [platform.openai.com](https://platform.openai.com)
2. Create account
3. Go to API Keys
4. Create new secret key
5. Copy the key

## 📁 File Structure for Deployment

```
ARCHITECT-GPT/
├── main.py               # Main application entry point
├── pages/
│   ├── 1_Upload.py       # Document upload
│   └── 2_About.py        # About page
├── requirements.txt      # Python dependencies
├── packages.txt          # System dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── setup.py              # Package setup
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

## 🐳 Docker Deployment (Advanced)

### Create Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deploy with Docker:
```bash
docker build -t saqa .
docker run -p 8501:8501 -e HUGGINGFACE_API_TOKEN=your_token architect-gpt
```

## 🔍 Troubleshooting

### Common Issues:

1. **"No module named 'langchain'"**
   - Make sure `requirements.txt` is in your repo
   - Check that all dependencies are listed

2. **"API key not found"**
   - Verify environment variables are set correctly
   - Check platform-specific variable naming

3. **"Model not found"**
   - For Hugging Face: Make sure the model exists
   - For OpenAI: Check your API key and billing

4. **"Port already in use"**
   - Use `$PORT` environment variable
   - Set `--server.address=0.0.0.0`

### Performance Tips:

1. **Use Hugging Face free models** for cost savings
2. **Limit document size** for faster processing
3. **Cache embeddings** to avoid reprocessing
4. **Use smaller models** for faster responses

## 🌐 Custom Domain (Optional)

### With Cloudflare:
1. Add your domain to Cloudflare
2. Point DNS to your deployment URL
3. Enable SSL/TLS

### With Netlify:
1. Deploy to Netlify
2. Add custom domain in settings
3. Configure DNS

## 📊 Monitoring & Analytics

### Free Options:
- **Streamlit Analytics:** Built-in usage tracking
- **Google Analytics:** Add tracking code
- **Logs:** Check platform-specific logs

### Paid Options:
- **Sentry:** Error tracking
- **DataDog:** Performance monitoring
- **New Relic:** Application monitoring

## 🚀 Next Steps

1. **Choose your deployment platform**
2. **Get API keys** (Hugging Face recommended for free tier)
3. **Deploy using the steps above**
4. **Test your application**
5. **Share your URL!**

---

**Need help?** Check the platform-specific documentation or create an issue in your GitHub repo.

**Created by:** Levansh Bhan  
**Project:** ARCHITECT-GPT - Intelligent Architecture Assistant 
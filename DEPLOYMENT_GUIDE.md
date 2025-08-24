# 🚀 Deployment Guide

This guide covers multiple deployment options for the Toxic Comment Classifier.

## 🌟 Recommended: Streamlit Community Cloud (Free)

### Prerequisites
- GitHub account
- Public repository with your code

### Steps
1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Your app will be live at:** `https://your-repo-name.streamlit.app`

### Configuration
- Add secrets in Streamlit Cloud dashboard if needed
- Configure custom domains (paid feature)
- Monitor usage and performance

---

## 🚂 Railway Deployment (Free Tier)

### Prerequisites
- Railway account
- GitHub repository

### Steps
1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Deploy**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Configure Environment**
   ```bash
   railway variables set STREAMLIT_SERVER_PORT=8501
   railway variables set STREAMLIT_SERVER_HEADLESS=true
   ```

---

## 🎨 Render Deployment (Free Tier)

### Prerequisites
- Render account
- GitHub repository

### Steps
1. **Connect Repository**
   - Go to [render.com](https://render.com)
   - Connect your GitHub account
   - Select "Web Service"

2. **Configure Service**
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - Environment: Python 3.9

3. **Environment Variables**
   ```
   STREAMLIT_SERVER_HEADLESS=true
   STREAMLIT_SERVER_ENABLE_CORS=false
   ```

---

## 🐳 Docker Deployment

### Local Docker
```bash
# Build image
docker build -t toxic-classifier .

# Run container
docker run -p 8501:8501 toxic-classifier
```

### Docker Compose
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Hub Deployment
```bash
# Tag and push
docker tag toxic-classifier your-username/toxic-classifier:latest
docker push your-username/toxic-classifier:latest
```

---

## ☁️ Cloud Platform Deployments

### Google Cloud Run
```bash
# Enable necessary APIs
gcloud services enable run.googleapis.com

# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/toxic-classifier
gcloud run deploy --image gcr.io/PROJECT_ID/toxic-classifier --platform managed
```

### AWS ECS/Fargate
```bash
# Create ECR repository
aws ecr create-repository --repository-name toxic-classifier

# Build and push
docker build -t toxic-classifier .
docker tag toxic-classifier:latest AWS_ACCOUNT.dkr.ecr.REGION.amazonaws.com/toxic-classifier:latest
docker push AWS_ACCOUNT.dkr.ecr.REGION.amazonaws.com/toxic-classifier:latest
```

### Azure Container Instances
```bash
# Create resource group
az group create --name toxic-classifier-rg --location eastus

# Deploy container
az container create --resource-group toxic-classifier-rg --name toxic-classifier --image your-registry/toxic-classifier:latest --ports 8501
```

---

## 🔧 Configuration for Production

### Environment Variables
```bash
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_PORT=8501
export MODEL_PATH=/app/resources/
export CONFIDENCE_THRESHOLD=0.5
```

### Resource Limits
- **Memory**: 512MB - 1GB recommended
- **CPU**: 0.5 - 1 vCPU recommended
- **Storage**: 1GB minimum for model files

### Monitoring
- Use platform-specific monitoring (Railway Metrics, Render Analytics)
- Implement custom logging for production debugging
- Set up health checks for container orchestration

---

## 🛡️ Security Best Practices

### 1. Environment Security
- Never commit secrets to git
- Use platform secret management
- Enable HTTPS (automatic on most platforms)

### 2. Application Security
- Input validation and sanitization
- Rate limiting (if supported by platform)
- Regular dependency updates

### 3. Model Security
- Store large model files in object storage
- Use environment variables for paths
- Implement model versioning

---

## 📊 Performance Optimization

### 1. Streamlit Optimization
```python
# Use caching for expensive operations
@st.cache_resource
def load_model():
    return ToxicClassifier()

@st.cache_data
def preprocess_text(text):
    return process(text)
```

### 2. Model Optimization
- Use quantized models for faster inference
- Implement batch processing for multiple texts
- Consider model distillation for smaller size

### 3. Infrastructure Optimization
- Use CDN for static assets
- Enable gzip compression
- Implement proper caching headers

---

## 🐛 Troubleshooting

### Common Issues

1. **Model files not found**
   - Ensure model files are in the repository
   - Check file paths in configuration
   - Verify file permissions

2. **Memory issues**
   - Reduce model size or use quantization
   - Implement lazy loading
   - Increase platform memory limits

3. **Slow loading times**
   - Use model caching
   - Optimize text preprocessing
   - Consider async processing

4. **CORS issues**
   - Set `STREAMLIT_SERVER_ENABLE_CORS=false`
   - Configure reverse proxy if needed
   - Check platform-specific settings

### Debug Commands
```bash
# Check logs
streamlit run app.py --logger.level debug

# Test locally
docker run -it --rm toxic-classifier /bin/bash

# Check resource usage
docker stats toxic-classifier
```

---

## 📝 Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Requirements.txt updated
- [ ] Model files included or accessible
- [ ] Environment variables configured
- [ ] Health checks implemented
- [ ] HTTPS enabled
- [ ] Custom domain configured (optional)
- [ ] Monitoring set up
- [ ] Backup strategy in place

---

Need help? Check the [GitHub Issues](https://github.com/yourusername/toxic-classification/issues) or create a new issue!

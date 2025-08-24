# 🚀 Quick Start Guide

Get your Toxic Comment Classifier running in minutes!

## 🌟 Deploy to Streamlit Cloud (Easiest - 5 minutes)

1. **Upload to GitHub**
   - Create a new repository on GitHub
   - Upload all project files (drag & drop the zip contents)
   - Make sure the repository is public

2. **Deploy**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app" → Select your repository
   - Main file: `app.py`
   - Click "Deploy"

3. **Done!** Your app will be live at: `https://your-repo-name.streamlit.app`

## 💻 Run Locally (2 minutes)

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py

# 3. Open browser to: http://localhost:8501
```

## 🐳 Docker (3 minutes)

```bash
# 1. Build image
docker build -t toxic-classifier .

# 2. Run container  
docker run -p 8501:8501 toxic-classifier

# 3. Open browser to: http://localhost:8501
```

## 📁 Model Files

The app works with dummy data by default. To use your own model:

1. Add these files to `resources/` folder:
   - `model.json` (Keras model architecture)
   - `weights.h5` (Model weights)
   - `tokenizer.pickle` (Trained tokenizer)

2. Restart the application

## ❓ Need Help?

- **Issues**: Check the GitHub Issues page
- **Documentation**: Read the full README.md
- **Deployment**: See DEPLOYMENT_GUIDE.md

## 🎉 That's it!

Your modern toxic comment classifier is now running with:
- ✅ Beautiful responsive UI
- ✅ Real-time analysis
- ✅ Interactive charts
- ✅ Mobile-friendly design
- ✅ Free cloud hosting

Enjoy your upgraded application! 🎊

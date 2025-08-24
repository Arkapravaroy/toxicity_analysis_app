# 🛡️ Modern Toxic Comment Classifier

A sleek, modern web application for detecting toxicity in text comments using machine learning. Built with Streamlit and modern ML practices.

## ✨ Features

- **Real-time Analysis**: Instant toxicity detection as you type
- **Interactive Visualizations**: Beautiful charts and radar plots
- **Multiple Categories**: Detects 6 types of toxicity
- **Modern UI**: Clean, responsive design with dark/light themes
- **Export Results**: Download analysis results as CSV
- **Example Texts**: Pre-loaded examples for quick testing
- **Mobile Friendly**: Responsive design for all devices

## 🚀 Quick Start

### Option 1: Streamlit Community Cloud (Recommended)

1. Fork this repository on GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy your forked repository
5. Your app will be live at `https://your-app-name.streamlit.app`

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/toxic-classification
cd toxic-classification

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 3: Docker

```bash
# Build the Docker image
docker build -t toxic-classifier .

# Run the container
docker run -p 8501:8501 toxic-classifier
```

## 📁 Project Structure

```
toxic-classification/
├── app.py                          # Main Streamlit application
├── models/
│   ├── __init__.py
│   └── toxic_classifier.py         # Model handling and prediction
├── utils/
│   ├── __init__.py
│   ├── text_preprocessing.py       # Text cleaning utilities
│   └── visualization.py            # Plotting and visualization
├── config/
│   ├── __init__.py
│   └── config.py                   # Configuration settings
├── assets/
│   ├── styles.css                  # Custom CSS styling
│   └── logo.png                    # Application logo
├── resources/                      # Model files (add your trained models here)
│   ├── model.json
│   ├── weights.h5
│   └── tokenizer.pickle
├── .streamlit/
│   └── config.toml                 # Streamlit configuration
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── setup.py                       # Package setup
├── .gitignore                      # Git ignore file
└── README.md                       # This file
```

## 🔧 Configuration

The application uses a centralized configuration system in `config/config.py`. You can customize:

- **Model Settings**: Confidence threshold, model paths
- **UI Theme**: Colors, layout preferences
- **Feature Flags**: Enable/disable specific features
- **Performance**: Caching, batch processing options

### Environment Variables

- `CONFIDENCE_THRESHOLD`: Toxicity classification threshold (default: 0.5)
- `MODEL_PATH`: Path to model files (default: "resources/")
- `DEBUG`: Enable debug mode (default: False)

## 📊 Toxicity Categories

The model detects 6 types of toxicity:

1. **Toxic**: General toxicity and harmful language
2. **Severe Toxic**: Highly toxic and extremely harmful content
3. **Obscene**: Obscene, vulgar, or sexually explicit language
4. **Threat**: Threatening language or intimidation
5. **Insult**: Insulting, offensive, or derogatory language
6. **Identity Hate**: Hatred based on identity, race, religion, etc.

## 🎯 Model Information

This application supports both:

- **Pre-trained Models**: Legacy Keras models with JSON + H5 format
- **Modern Models**: TensorFlow 2.x SavedModel format
- **Transformer Models**: HuggingFace transformers (optional)

### Adding Your Own Model

1. Place your model files in the `resources/` directory:
   - `model.json`: Model architecture (Keras JSON format)
   - `weights.h5`: Model weights
   - `tokenizer.pickle`: Trained tokenizer

2. Update `config/config.py` if needed for custom configurations

## 🚀 Deployment Options

### 1. Streamlit Community Cloud (Free)

**Pros:**
- ✅ Completely free
- ✅ Easy setup with GitHub integration
- ✅ Automatic deployments on git push
- ✅ Custom subdomain (your-app.streamlit.app)
- ✅ No server maintenance required

**Steps:**
1. Push your code to GitHub (public repo)
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub and select your repository
4. Click "Deploy"

### 2. Railway (Free Tier)

**Pros:**
- ✅ Free tier available
- ✅ Supports Docker deployment
- ✅ Automatic deployments
- ✅ Custom domains

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### 3. Render (Free Tier)

**Pros:**
- ✅ Free web services
- ✅ Docker support
- ✅ Custom domains
- ✅ Automatic SSL

### 4. Docker Deployment

```bash
# Build and run locally
docker build -t toxic-classifier .
docker run -p 8501:8501 toxic-classifier

# Or use docker-compose
docker-compose up
```

## 🎨 Customization

### Custom Styling

Modify `assets/styles.css` to customize the appearance:

```css
/* Custom color scheme */
.main-title {
    color: #your-color;
    font-family: 'Your-Font';
}
```

### Adding New Features

1. **New Visualizations**: Add functions to `utils/visualization.py`
2. **Text Processing**: Extend `utils/text_preprocessing.py`
3. **Model Support**: Update `models/toxic_classifier.py`

## 🧪 Testing

```bash
# Run basic tests
python -m pytest tests/

# Test individual components
python models/toxic_classifier.py
python utils/text_preprocessing.py
python utils/visualization.py
```

## 📈 Performance Optimization

- **Caching**: Uses Streamlit's caching for model loading
- **Lazy Loading**: Models loaded only when needed
- **Batch Processing**: Support for analyzing multiple texts
- **Memory Management**: Efficient memory usage for large texts

## 🔒 Privacy & Security

- **No Data Storage**: Text inputs are not stored or logged
- **Rate Limiting**: Configurable request limits
- **Input Sanitization**: Safe handling of user inputs
- **HTTPS**: Automatic SSL on most deployment platforms

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 🏆 Credits & Acknowledgments

**Original Project Mentors:**
- **Dr. Asif Ekbal** - For guidance and mentoring
- **Dr. Soumitra Ghosh** - For technical supervision

**Refactored for Modern Deployment:**
- Updated to modern ML frameworks
- Streamlit-based responsive UI
- Best practices implementation
- Cloud deployment optimization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issue Reporting

Found a bug or have a suggestion? Please:

1. Check existing issues on GitHub
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

## 📞 Support

- **Documentation**: This README and inline code comments
- **Issues**: GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions

---

**⭐ If you find this project useful, please give it a star on GitHub!**

Made with ❤️ for the ML community | Modern deployment by [Your Name]

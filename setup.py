"""
Setup script for Toxic Comment Classifier
==========================================
Modern ML web application for toxicity detection.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="toxic-comment-classifier",
    version="2.0.0",
    author="Modern ML Applications",
    author_email="your.email@example.com",
    description="AI-powered toxicity detection with real-time analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/toxic-classification",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "transformers": [
            "transformers>=4.30.0",
            "torch>=2.0.0",
        ],
        "spacy": [
            "spacy>=3.6.0",
            "en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0.tar.gz",
        ],
    },
    entry_points={
        "console_scripts": [
            "toxic-classifier=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.css", "*.toml", "*.md"],
        "assets": ["*"],
        "resources": ["*"],
    },
    keywords="machine-learning nlp toxicity-detection streamlit web-app",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/toxic-classification/issues",
        "Source": "https://github.com/yourusername/toxic-classification",
        "Documentation": "https://github.com/yourusername/toxic-classification#readme",
    },
)

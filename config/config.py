"""
Configuration Settings
=====================
Central configuration for the Toxic Comment Classification app.
"""

import os
from typing import Dict, List

# Application Configuration
APP_CONFIG = {
    "name": "Toxic Comment Classifier",
    "version": "2.0.0",
    "description": "AI-powered toxicity detection with real-time analysis",
    "author": "Refactored for Modern Deployment",
    "credits": ["Dr. Asif Ekbal", "Dr. Soumitra Ghosh"],
    "icon": "🛡️",
    "layout": "wide"
}

# Model Configuration
MODEL_CONFIG = {
    "model_path": "resources/",
    "model_files": {
        "architecture": "model.json",
        "weights": "weights.h5",
        "tokenizer": "tokenizer.pickle"
    },
    "max_features": 20000,
    "max_length": 100,
    "confidence_threshold": 0.5
}

# Toxicity Categories
TOXICITY_CATEGORIES = [
    "toxic",
    "severe_toxic", 
    "obscene",
    "threat",
    "insult",
    "identity_hate"
]

# Category Descriptions
CATEGORY_DESCRIPTIONS = {
    "toxic": "General toxicity and harmful language",
    "severe_toxic": "Highly toxic and extremely harmful content",
    "obscene": "Obscene, vulgar, or sexually explicit language",
    "threat": "Threatening language or intimidation",
    "insult": "Insulting, offensive, or derogatory language",
    "identity_hate": "Hatred based on identity, race, religion, etc."
}

# UI Configuration
UI_CONFIG = {
    "primary_color": "#FF6B6B",
    "secondary_color": "#4ECDC4",
    "background_color": "#F7F9FC",
    "text_color": "#2C3E50",
    "success_color": "#2ECC71",
    "warning_color": "#F39C12",
    "error_color": "#E74C3C",
    "chart_colors": [
        "#FF6B6B", "#4ECDC4", "#45B7D1", 
        "#96CEB4", "#FFEAA7", "#DDA0DD"
    ]
}

# Example Texts for Testing
EXAMPLE_TEXTS = [
    {
        "label": "Positive Comment",
        "text": "This is a great post, thank you for sharing your insights!",
        "expected_toxicity": "low"
    },
    {
        "label": "Neutral Disagreement", 
        "text": "I respectfully disagree with this perspective.",
        "expected_toxicity": "low"
    },
    {
        "label": "Mild Negative",
        "text": "This idea seems poorly thought out and unconvincing.",
        "expected_toxicity": "medium"
    },
    {
        "label": "Harsh Criticism",
        "text": "This is absolutely stupid and makes no sense at all!",
        "expected_toxicity": "high"
    },
    {
        "label": "Personal Attack",
        "text": "You're such an idiot, I can't believe anyone listens to you.",
        "expected_toxicity": "high"
    }
]

# Deployment Configuration
DEPLOYMENT_CONFIG = {
    "streamlit_cloud": {
        "requirements_file": "requirements.txt",
        "python_version": "3.9",
        "main_file": "app.py"
    },
    "docker": {
        "base_image": "python:3.9-slim",
        "port": 8501,
        "healthcheck": True
    },
    "environment_variables": [
        "STREAMLIT_SERVER_PORT",
        "STREAMLIT_SERVER_ENABLE_CORS",
        "STREAMLIT_SERVER_HEADLESS"
    ]
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "handlers": ["console"],
    "log_file": "app.log"
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    "cache_ttl": 3600,  # 1 hour
    "max_text_length": 5000,
    "batch_size": 32,
    "enable_gpu": False,
    "memory_limit": "1GB"
}

# Security Configuration
SECURITY_CONFIG = {
    "max_requests_per_minute": 100,
    "enable_rate_limiting": False,
    "sanitize_input": True,
    "log_predictions": False  # Privacy consideration
}

# Feature Flags
FEATURE_FLAGS = {
    "enable_examples": True,
    "enable_statistics": True,
    "enable_export": True,
    "enable_batch_processing": False,
    "enable_api_mode": False,
    "enable_model_comparison": False
}

def get_config(section: str) -> Dict:
    """
    Get configuration for a specific section.

    Args:
        section (str): Configuration section name

    Returns:
        Dict: Configuration dictionary
    """
    configs = {
        "app": APP_CONFIG,
        "model": MODEL_CONFIG,
        "ui": UI_CONFIG,
        "deployment": DEPLOYMENT_CONFIG,
        "logging": LOGGING_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "security": SECURITY_CONFIG,
        "features": FEATURE_FLAGS
    }

    return configs.get(section, {})

def is_feature_enabled(feature_name: str) -> bool:
    """
    Check if a feature is enabled.

    Args:
        feature_name (str): Feature flag name

    Returns:
        bool: True if feature is enabled
    """
    return FEATURE_FLAGS.get(feature_name, False)

def get_environment_config():
    """
    Get environment-specific configuration.

    Returns:
        Dict: Environment configuration
    """
    env_config = {
        "debug_mode": os.getenv("DEBUG", "False").lower() == "true",
        "model_path": os.getenv("MODEL_PATH", MODEL_CONFIG["model_path"]),
        "confidence_threshold": float(os.getenv("CONFIDENCE_THRESHOLD", MODEL_CONFIG["confidence_threshold"])),
        "max_text_length": int(os.getenv("MAX_TEXT_LENGTH", PERFORMANCE_CONFIG["max_text_length"])),
    }

    return env_config

if __name__ == "__main__":
    # Test configuration functions
    print("🔧 Configuration Testing")
    print("=" * 40)

    app_config = get_config("app")
    print(f"App Name: {app_config['name']}")
    print(f"Version: {app_config['version']}")

    print(f"\nToxicity Categories: {TOXICITY_CATEGORIES}")
    print(f"\nExample enabled: {is_feature_enabled('enable_examples')}")

    env_config = get_environment_config()
    print(f"\nEnvironment Config: {env_config}")

    print("\n✅ Configuration loaded successfully!")

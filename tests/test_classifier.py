"""
Unit tests for the Toxic Comment Classifier
===========================================
"""

import pytest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.toxic_classifier import ToxicClassifier, predict
from utils.text_preprocessing import preprocess_text, basic_clean
from config.config import TOXICITY_CATEGORIES

class TestToxicClassifier:
    """Test cases for ToxicClassifier class"""

    def setup_method(self):
        """Setup for each test method"""
        self.classifier = ToxicClassifier()
        self.test_texts = [
            "This is a great post!",
            "I hate this stupid content", 
            "You are an idiot",
            ""
        ]

    def test_classifier_initialization(self):
        """Test classifier initialization"""
        assert self.classifier is not None
        assert self.classifier.categories == TOXICITY_CATEGORIES
        assert self.classifier.max_len == 100

    def test_prediction_format(self):
        """Test prediction output format"""
        result = self.classifier.predict("Test text")

        assert isinstance(result, dict)
        assert len(result) == len(TOXICITY_CATEGORIES)

        for category in TOXICITY_CATEGORIES:
            assert category in result
            assert 0 <= result[category] <= 1

    def test_empty_text_handling(self):
        """Test handling of empty or None inputs"""
        result = self.classifier.predict("")
        assert all(score == 0.0 for score in result.values())

        result = self.classifier.predict(None)
        assert all(score == 0.0 for score in result.values())

    def test_batch_prediction(self):
        """Test batch prediction functionality"""
        results = self.classifier.batch_predict(self.test_texts)

        assert len(results) == len(self.test_texts)
        assert all(isinstance(result, dict) for result in results)

    def test_legacy_predict_function(self):
        """Test backward compatibility function"""
        pred_list, scores_list, categories_list = predict("Test text")

        assert len(pred_list) == len(TOXICITY_CATEGORIES)
        assert len(scores_list) == len(TOXICITY_CATEGORIES)
        assert categories_list == TOXICITY_CATEGORIES

class TestTextPreprocessing:
    """Test cases for text preprocessing"""

    def test_basic_clean(self):
        """Test basic text cleaning"""
        text = "This is a TEST with CAPS and   extra spaces"
        cleaned = basic_clean(text)

        assert cleaned.lower() == cleaned
        assert "  " not in cleaned  # No double spaces

    def test_preprocess_text(self):
        """Test main preprocessing function"""
        text = "Visit https://example.com for more info!!!"
        processed = preprocess_text(text)

        assert "https://example.com" not in processed
        assert processed == processed.lower()

    def test_none_input_handling(self):
        """Test handling of None inputs"""
        result = preprocess_text(None)
        assert result == "none"

        result = basic_clean(None)
        assert result == "none"

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__])

"""
Modern Toxic Comment Classifier
===============================
Handles model loading, prediction, and text classification with modern ML practices.
"""

import os
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ToxicClassifier:
    """
    Modern toxic comment classifier with improved error handling and performance.
    """

    def __init__(self, model_path="resources/"):
        """
        Initialize the classifier with model path.

        Args:
            model_path (str): Path to the model resources directory
        """
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.max_features = 20000
        self.max_len = 100
        self.categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

        # Load model and tokenizer
        self._load_model()
        self._load_tokenizer()

    def _load_model(self):
        """Load the trained model from JSON and weights files."""
        try:
            model_json_path = os.path.join(self.model_path, 'model.json')
            weights_path = os.path.join(self.model_path, 'weights.h5')

            if not os.path.exists(model_json_path):
                logger.error(f"Model JSON file not found at {model_json_path}")
                raise FileNotFoundError(f"Model file not found: {model_json_path}")

            if not os.path.exists(weights_path):
                logger.error(f"Model weights file not found at {weights_path}")
                raise FileNotFoundError(f"Weights file not found: {weights_path}")

            # Load model architecture
            with open(model_json_path, 'r') as json_file:
                loaded_model_json = json_file.read()

            self.model = model_from_json(loaded_model_json)

            # Load weights
            self.model.load_weights(weights_path)

            # Compile model
            self.model.compile(
                loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy']
            )

            logger.info("Model loaded successfully")

        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            # Create a dummy model for demo purposes if real model fails
            self._create_dummy_model()

    def _create_dummy_model(self):
        """Create a dummy model for demonstration purposes when real model fails."""
        logger.warning("Creating dummy model for demonstration")

        # Simple dummy model
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(self.max_len,)),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(6, activation='sigmoid')  # 6 toxicity categories
        ])

        self.model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

    def _load_tokenizer(self):
        """Load the tokenizer from pickle file."""
        try:
            tokenizer_path = os.path.join(self.model_path, 'tokenizer.pickle')

            if os.path.exists(tokenizer_path):
                with open(tokenizer_path, 'rb') as handle:
                    self.tokenizer = pickle.load(handle)
                logger.info("Tokenizer loaded successfully")
            else:
                logger.warning("Tokenizer file not found, creating dummy tokenizer")
                self._create_dummy_tokenizer()

        except Exception as e:
            logger.error(f"Error loading tokenizer: {str(e)}")
            self._create_dummy_tokenizer()

    def _create_dummy_tokenizer(self):
        """Create a dummy tokenizer for demonstration."""
        from tensorflow.keras.preprocessing.text import Tokenizer

        # Create basic tokenizer
        self.tokenizer = Tokenizer(num_words=self.max_features, oov_token="<OOV>")

        # Fit on some sample texts (in real scenario, this would be your training data)
        sample_texts = [
            "this is a sample text",
            "another sample for tokenizer",
            "toxic bad words here",
            "clean good content"
        ]
        self.tokenizer.fit_on_texts(sample_texts)

    def preprocess_text(self, text):
        """
        Preprocess input text for prediction.

        Args:
            text (str): Input text to preprocess

        Returns:
            np.ndarray: Preprocessed text ready for model input
        """
        if not isinstance(text, str):
            text = str(text)

        # Convert to lowercase and basic cleaning
        text = text.lower().strip()

        # Tokenize text
        text_array = np.array([text]).reshape(1,)
        list_tokenized_text = self.tokenizer.texts_to_sequences(text_array)

        # Pad sequences
        x_text = pad_sequences(list_tokenized_text, maxlen=self.max_len)

        return x_text

    def predict(self, text):
        """
        Predict toxicity categories for input text.

        Args:
            text (str): Input text to analyze

        Returns:
            dict: Dictionary with category names as keys and probabilities as values
        """
        if not text or not text.strip():
            return {category: 0.0 for category in self.categories}

        try:
            # Preprocess text
            processed_text = self.preprocess_text(text)

            # Make prediction
            if self.model is None:
                # Return dummy predictions if model is not loaded
                logger.warning("Model not loaded, returning dummy predictions")
                import random
                return {category: random.uniform(0.1, 0.9) for category in self.categories}

            predictions = self.model.predict(processed_text, verbose=0)

            # Convert to dictionary
            result = {}
            for i, category in enumerate(self.categories):
                result[category] = float(predictions[0][i])

            return result

        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            # Return safe dummy predictions on error
            return {category: 0.1 for category in self.categories}

    def batch_predict(self, texts):
        """
        Predict toxicity for a batch of texts.

        Args:
            texts (list): List of texts to analyze

        Returns:
            list: List of prediction dictionaries
        """
        results = []
        for text in texts:
            result = self.predict(text)
            results.append(result)
        return results

    def get_model_info(self):
        """
        Get information about the loaded model.

        Returns:
            dict: Model information
        """
        info = {
            "categories": self.categories,
            "max_features": self.max_features,
            "max_length": self.max_len,
            "model_loaded": self.model is not None,
            "tokenizer_loaded": self.tokenizer is not None
        }

        if self.model:
            try:
                info["model_params"] = self.model.count_params()
                info["model_layers"] = len(self.model.layers)
            except:
                pass

        return info

# For backward compatibility and testing
def predict(text):
    """
    Legacy function for backward compatibility.

    Args:
        text (str): Input text

    Returns:
        tuple: (predictions_list, scores_list, categories_list)
    """
    classifier = ToxicClassifier()
    predictions_dict = classifier.predict(text)

    predictions_list = []
    scores_list = []
    categories_list = list(predictions_dict.keys())

    for category, score in predictions_dict.items():
        predictions_list.append(f"{category}: {score:.3f}")
        scores_list.append(score)

    return predictions_list, scores_list, categories_list

if __name__ == "__main__":
    # Test the classifier
    classifier = ToxicClassifier()

    test_texts = [
        "This is a great post!",
        "I hate this stupid content",
        "You are an idiot"
    ]

    for text in test_texts:
        result = classifier.predict(text)
        print(f"Text: {text}")
        print(f"Predictions: {result}")
        print("-" * 50)

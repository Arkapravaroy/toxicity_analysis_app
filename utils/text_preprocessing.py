"""
Text Preprocessing Utilities
============================
Modern text preprocessing functions with improved performance and error handling.
"""

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Download required NLTK data (with error handling)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    try:
        nltk.download('punkt', quiet=True)
    except:
        logger.warning("Failed to download NLTK punkt tokenizer")

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    try:
        nltk.download('stopwords', quiet=True)
    except:
        logger.warning("Failed to download NLTK stopwords")

class TextPreprocessor:
    """Modern text preprocessor with configurable options."""

    def __init__(self, 
                 remove_punctuation=True,
                 remove_stopwords=False,
                 lowercase=True,
                 remove_urls=True,
                 remove_special_chars=True,
                 stemming=False):
        """
        Initialize text preprocessor with configuration options.

        Args:
            remove_punctuation (bool): Remove punctuation marks
            remove_stopwords (bool): Remove common stopwords
            lowercase (bool): Convert text to lowercase
            remove_urls (bool): Remove URLs from text
            remove_special_chars (bool): Remove special characters
            stemming (bool): Apply stemming to words
        """
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords
        self.lowercase = lowercase
        self.remove_urls = remove_urls
        self.remove_special_chars = remove_special_chars
        self.stemming = stemming

        # Initialize components
        self.stemmer = PorterStemmer() if stemming else None
        self.stop_words = set(stopwords.words('english')) if remove_stopwords else set()

    def clean_text(self, text):
        """
        Clean and preprocess text according to configuration.

        Args:
            text (str): Input text to clean

        Returns:
            str: Cleaned text
        """
        if not isinstance(text, str):
            text = str(text)

        # Convert to lowercase
        if self.lowercase:
            text = text.lower()

        # Remove URLs
        if self.remove_urls:
            text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

        # Remove special characters and digits
        if self.remove_special_chars:
            text = re.sub(r'[^a-zA-Z\s]', '', text)

        # Remove extra whitespace
        text = ' '.join(text.split())

        # Tokenize
        try:
            tokens = word_tokenize(text)
        except:
            # Fallback to simple split if NLTK fails
            tokens = text.split()

        # Remove stopwords
        if self.remove_stopwords and self.stop_words:
            tokens = [token for token in tokens if token.lower() not in self.stop_words]

        # Remove punctuation
        if self.remove_punctuation:
            tokens = [token for token in tokens if token not in string.punctuation]

        # Apply stemming
        if self.stemming and self.stemmer:
            try:
                tokens = [self.stemmer.stem(token) for token in tokens]
            except:
                logger.warning("Stemming failed, skipping...")

        # Join tokens back to text
        cleaned_text = ' '.join(tokens)

        return cleaned_text.strip()

# Global preprocessor instance
_default_preprocessor = TextPreprocessor(
    remove_punctuation=False,  # Keep punctuation for toxicity detection
    remove_stopwords=False,    # Keep stopwords for context
    lowercase=True,
    remove_urls=True,
    remove_special_chars=False,
    stemming=False
)

def preprocess_text(text, preprocessor=None):
    """
    Preprocess text using default or custom preprocessor.

    Args:
        text (str): Input text to preprocess
        preprocessor (TextPreprocessor, optional): Custom preprocessor

    Returns:
        str: Preprocessed text
    """
    if preprocessor is None:
        preprocessor = _default_preprocessor

    return preprocessor.clean_text(text)

def basic_clean(text):
    """
    Basic text cleaning for quick preprocessing.

    Args:
        text (str): Input text

    Returns:
        str: Cleaned text
    """
    if not isinstance(text, str):
        text = str(text)

    # Convert to lowercase
    text = text.lower().strip()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove extra whitespace
    text = ' '.join(text.split())

    return text

def extract_features(text):
    """
    Extract basic features from text for analysis.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with extracted features
    """
    if not isinstance(text, str):
        text = str(text)

    features = {
        'length': len(text),
        'word_count': len(text.split()),
        'char_count': len(text),
        'uppercase_ratio': sum(1 for c in text if c.isupper()) / len(text) if text else 0,
        'punctuation_count': sum(1 for c in text if c in string.punctuation),
        'digit_count': sum(1 for c in text if c.isdigit()),
        'exclamation_count': text.count('!'),
        'question_count': text.count('?'),
        'caps_words': sum(1 for word in text.split() if word.isupper()),
    }

    return features

def is_spam_pattern(text):
    """
    Check if text matches common spam patterns.

    Args:
        text (str): Input text

    Returns:
        bool: True if spam pattern detected
    """
    if not isinstance(text, str):
        text = str(text)

    text_lower = text.lower()

    # Common spam patterns
    spam_patterns = [
        r'(buy now|click here|free money|urgent|winner)',
        r'(\$\d+|money back|guarantee|limited time)',
        r'(call now|act now|don\'t wait|hurry)',
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text_lower):
            return True

    return False

if __name__ == "__main__":
    # Test the preprocessing functions
    test_texts = [
        "This is a GREAT post with https://example.com and some !!! marks",
        "I HATE this stupid content, it's terrible!!!",
        "Check out this link: www.spam.com for FREE MONEY NOW!!!"
    ]

    preprocessor = TextPreprocessor()

    for text in test_texts:
        cleaned = preprocess_text(text)
        features = extract_features(text)
        is_spam = is_spam_pattern(text)

        print(f"Original: {text}")
        print(f"Cleaned: {cleaned}")
        print(f"Features: {features}")
        print(f"Is spam: {is_spam}")
        print("-" * 80)

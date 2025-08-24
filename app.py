"""
Modern Toxic Comment Classification Web App
==========================================
A sleek, modern Streamlit application for detecting toxicity in text comments.

Built with best practices and modern ML libraries.
Author: Refactored for modern deployment
Credits: Dr. Asif Ekbal and Dr. Soumitra Ghosh for mentoring
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Custom imports
from models.toxic_classifier import ToxicClassifier
from utils.text_preprocessing import preprocess_text
from utils.visualization import create_toxicity_chart, create_radar_chart
from config.config import APP_CONFIG, TOXICITY_CATEGORIES

# Configure page
st.set_page_config(
    page_title="Toxic Comment Classifier",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    """Load custom CSS for modern styling"""
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the toxic classification model with caching"""
    try:
        classifier = ToxicClassifier()
        return classifier
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def main():
    """Main application function"""

    # Load custom styling
    try:
        load_css()
    except:
        pass  # CSS file optional for deployment

    # Header section with modern design
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">🛡️ Toxic Comment Classifier</h1>
        <p class="subtitle">AI-powered toxicity detection with real-time analysis</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")

        # Model settings
        confidence_threshold = st.slider(
            "Confidence Threshold", 
            min_value=0.1, 
            max_value=0.9, 
            value=0.5, 
            step=0.1,
            help="Threshold for classification confidence"
        )

        show_probabilities = st.checkbox("Show Probabilities", value=True)
        show_preprocessing = st.checkbox("Show Text Preprocessing", value=False)

        st.markdown("---")
        st.markdown("""
        ### 📊 About Categories
        - **Toxic**: General toxicity
        - **Severe Toxic**: Highly toxic content
        - **Obscene**: Obscene language
        - **Threat**: Threatening content
        - **Insult**: Insulting language
        - **Identity Hate**: Identity-based hate
        """)

        st.markdown("---")
        st.markdown("""
        ### 🏆 Credits
        **Mentors:**
        - Dr. Asif Ekbal
        - Dr. Soumitra Ghosh

        **Technology Stack:**
        - Streamlit
        - TensorFlow/Keras
        - Plotly
        - scikit-learn
        """)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📝 Enter Text for Analysis")

        # Text input with modern styling
        user_input = st.text_area(
            "Type or paste the comment you want to analyze:",
            height=150,
            placeholder="Enter your text here...",
            help="The text will be analyzed for various types of toxicity"
        )

        # Analysis button
        analyze_button = st.button(
            "🔍 Analyze Text",
            type="primary",
            use_container_width=True
        )

        if analyze_button and user_input.strip():
            with st.spinner("🤖 Analyzing text..."):
                # Load model
                classifier = load_model()

                if classifier is None:
                    st.error("❌ Model failed to load. Please try again.")
                    return

                # Preprocess text
                processed_text = preprocess_text(user_input)

                if show_preprocessing:
                    st.info(f"**Preprocessed text:** {processed_text}")

                # Get predictions
                try:
                    predictions = classifier.predict(user_input)

                    # Create results display
                    st.markdown("---")
                    st.markdown("### 📈 Analysis Results")

                    # Overall toxicity indicator
                    max_score = max(predictions.values())
                    if max_score >= confidence_threshold:
                        st.error(f"⚠️ **TOXIC CONTENT DETECTED** (Confidence: {max_score:.1%})")
                        st.markdown("This text contains potentially harmful content.")
                    else:
                        st.success("✅ **CLEAN CONTENT** - No toxicity detected")

                    # Detailed results
                    if show_probabilities:
                        st.markdown("#### Detailed Breakdown")

                        # Create metrics columns
                        cols = st.columns(3)
                        for i, (category, score) in enumerate(predictions.items()):
                            with cols[i % 3]:
                                color = "red" if score >= confidence_threshold else "green"
                                st.metric(
                                    label=category.replace('_', ' ').title(),
                                    value=f"{score:.1%}",
                                    delta=None
                                )

                    # Visualization
                    fig = create_toxicity_chart(predictions, confidence_threshold)
                    st.plotly_chart(fig, use_container_width=True)

                    # Radar chart
                    radar_fig = create_radar_chart(predictions)
                    st.plotly_chart(radar_fig, use_container_width=True)

                    # Export results
                    results_df = pd.DataFrame([{
                        'timestamp': datetime.now(),
                        'text': user_input[:100] + "..." if len(user_input) > 100 else user_input,
                        **predictions
                    }])

                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results (CSV)",
                        data=csv,
                        file_name=f"toxicity_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )

                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")

        elif analyze_button and not user_input.strip():
            st.warning("⚠️ Please enter some text to analyze.")

    with col2:
        st.markdown("### 💡 Quick Examples")

        example_texts = [
            "This is a great post, thank you for sharing!",
            "I completely disagree with this opinion.",
            "What a stupid idea, this is terrible!",
            "You're an idiot if you believe this.",
            "I hate people like you, you should disappear."
        ]

        for i, example in enumerate(example_texts):
            if st.button(f"Example {i+1}", key=f"ex_{i}", use_container_width=True):
                st.session_state['example_text'] = example

        # Display selected example
        if 'example_text' in st.session_state:
            st.text_area(
                "Selected Example:",
                value=st.session_state['example_text'],
                height=100,
                disabled=True
            )
            if st.button("📋 Use This Example"):
                user_input = st.session_state['example_text']

        # Statistics section
        st.markdown("### 📊 Usage Statistics")

        # Mock statistics (in real app, these would come from a database)
        col1_stat, col2_stat = st.columns(2)
        with col1_stat:
            st.metric("Total Analyses", "1,234")
            st.metric("Clean Comments", "892")
        with col2_stat:
            st.metric("Toxic Comments", "342")
            st.metric("Accuracy", "94.2%")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit | 
        Mentored by Dr. Asif Ekbal & Dr. Soumitra Ghosh | 
        © 2025 Modern ML Applications</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

"""
Visualization Utilities
======================
Modern visualization functions using Plotly for interactive charts.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def create_toxicity_chart(predictions, threshold=0.5, title="Toxicity Analysis"):
    """
    Create an interactive bar chart for toxicity predictions.

    Args:
        predictions (dict): Dictionary with category predictions
        threshold (float): Threshold for toxicity classification
        title (str): Chart title

    Returns:
        plotly.graph_objects.Figure: Interactive bar chart
    """
    categories = list(predictions.keys())
    scores = list(predictions.values())

    # Create colors based on threshold
    colors = ['red' if score >= threshold else 'green' for score in scores]

    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=scores,
            text=[f'{score:.1%}' for score in scores],
            textposition='auto',
            marker_color=colors,
            hovertemplate='<b>%{x}</b><br>Score: %{y:.3f}<extra></extra>'
        )
    ])

    # Add threshold line
    fig.add_hline(
        y=threshold, 
        line_dash="dash", 
        line_color="orange",
        annotation_text=f"Threshold ({threshold:.1%})"
    )

    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title="Toxicity Categories",
        yaxis_title="Confidence Score",
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        template="plotly_white",
        height=400,
        showlegend=False
    )

    return fig

def create_radar_chart(predictions, title="Toxicity Radar Chart"):
    """
    Create a radar chart for toxicity predictions.

    Args:
        predictions (dict): Dictionary with category predictions
        title (str): Chart title

    Returns:
        plotly.graph_objects.Figure: Radar chart
    """
    categories = list(predictions.keys())
    scores = list(predictions.values())

    # Format category names for display
    formatted_categories = [cat.replace('_', ' ').title() for cat in categories]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=formatted_categories,
        fill='toself',
        name='Toxicity Scores',
        line_color='rgb(255, 99, 71)',
        fillcolor='rgba(255, 99, 71, 0.3)',
        hovertemplate='<b>%{theta}</b><br>Score: %{r:.3f}<extra></extra>'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                ticksuffix='',
                tickformat='.1%'
            )
        ),
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        template="plotly_white",
        height=400,
        showlegend=False
    )

    return fig

def create_comparison_chart(predictions_list, labels, title="Toxicity Comparison"):
    """
    Create a comparison chart for multiple predictions.

    Args:
        predictions_list (list): List of prediction dictionaries
        labels (list): Labels for each prediction
        title (str): Chart title

    Returns:
        plotly.graph_objects.Figure: Comparison bar chart
    """
    if len(predictions_list) != len(labels):
        raise ValueError("predictions_list and labels must have the same length")

    categories = list(predictions_list[0].keys())

    fig = go.Figure()

    colors = px.colors.qualitative.Set3[:len(predictions_list)]

    for i, (predictions, label) in enumerate(zip(predictions_list, labels)):
        scores = [predictions[cat] for cat in categories]

        fig.add_trace(go.Bar(
            name=label,
            x=categories,
            y=scores,
            text=[f'{score:.1%}' for score in scores],
            textposition='auto',
            marker_color=colors[i],
            hovertemplate=f'<b>{label}</b><br>%{{x}}: %{{y:.3f}}<extra></extra>'
        ))

    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title="Toxicity Categories",
        yaxis_title="Confidence Score",
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        template="plotly_white",
        barmode='group',
        height=500,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig

def create_time_series_chart(data, title="Toxicity Over Time"):
    """
    Create a time series chart for toxicity analysis.

    Args:
        data (pd.DataFrame): DataFrame with timestamp and toxicity scores
        title (str): Chart title

    Returns:
        plotly.graph_objects.Figure: Time series chart
    """
    fig = go.Figure()

    # Add traces for each toxicity category
    toxicity_categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    colors = px.colors.qualitative.Set1

    for i, category in enumerate(toxicity_categories):
        if category in data.columns:
            fig.add_trace(go.Scatter(
                x=data['timestamp'],
                y=data[category],
                mode='lines+markers',
                name=category.replace('_', ' ').title(),
                line=dict(color=colors[i % len(colors)]),
                hovertemplate=f'<b>{category.title()}</b><br>Time: %{{x}}<br>Score: %{{y:.3f}}<extra></extra>'
            ))

    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title="Time",
        yaxis_title="Toxicity Score",
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        template="plotly_white",
        height=500,
        hovermode='x unified'
    )

    return fig

def create_word_cloud_data(text, max_words=50):
    """
    Prepare data for word cloud visualization.

    Args:
        text (str): Input text
        max_words (int): Maximum number of words to include

    Returns:
        dict: Word frequency data
    """
    if not isinstance(text, str):
        text = str(text)

    # Simple word frequency calculation
    words = text.lower().split()
    word_freq = {}

    for word in words:
        # Basic cleaning
        word = word.strip('.,!?";:()[]{}')
        if len(word) > 2:  # Skip very short words
            word_freq[word] = word_freq.get(word, 0) + 1

    # Sort by frequency and limit
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_words[:max_words])

def create_distribution_chart(scores, title="Score Distribution"):
    """
    Create a distribution chart for toxicity scores.

    Args:
        scores (list): List of toxicity scores
        title (str): Chart title

    Returns:
        plotly.graph_objects.Figure: Distribution chart
    """
    fig = go.Figure()

    fig.add_trace(go.Histogram(
        x=scores,
        nbinsx=20,
        name="Score Distribution",
        marker_color='skyblue',
        opacity=0.7,
        hovertemplate='Range: %{x}<br>Count: %{y}<extra></extra>'
    ))

    # Add mean line
    mean_score = np.mean(scores)
    fig.add_vline(
        x=mean_score,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Mean: {mean_score:.3f}"
    )

    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title="Toxicity Score",
        yaxis_title="Frequency",
        template="plotly_white",
        height=400,
        showlegend=False
    )

    return fig

if __name__ == "__main__":
    # Test visualization functions
    sample_predictions = {
        'toxic': 0.8,
        'severe_toxic': 0.3,
        'obscene': 0.6,
        'threat': 0.2,
        'insult': 0.7,
        'identity_hate': 0.1
    }

    # Test bar chart
    bar_fig = create_toxicity_chart(sample_predictions)
    print("✅ Bar chart created")

    # Test radar chart
    radar_fig = create_radar_chart(sample_predictions)
    print("✅ Radar chart created")

    # Test word cloud data
    sample_text = "This is a sample text for testing word frequency analysis"
    word_data = create_word_cloud_data(sample_text)
    print(f"✅ Word cloud data created: {word_data}")

    print("🎨 All visualization functions tested successfully!")

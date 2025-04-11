import json
import numpy as np
from transformers import pipeline

# Load model
summarizer = pipeline("text2text-generation", model="google/flan-t5-large")

def convert_to_serializable(obj):
    if isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(v) for v in obj]
    elif hasattr(obj, "item"):
        return obj.item()
    return obj

def generate_narrative_gpt(numeric_summary, sentiment_summary, tone="Formal", linked_insights=None):
    numeric_summary = convert_to_serializable(numeric_summary)
    sentiment_summary = convert_to_serializable(sentiment_summary)

    # Format cross-link insights
    linked_insight_lines = []
    if linked_insights:
        for link in linked_insights:
            d1, d2 = link.get('datasets', [0, 1])
            key = link.get('key', 'unknown')
            rows = link.get('intersection_rows', 0)
            linked_insight_lines.append(f"Dataset {d1 + 1} and Dataset {d2 + 1} share {rows} rows using key '{key}'.")

    # Build a compact prompt — FLAN struggles with too much noise
    prompt = f"""You are a helpful data assistant.
Create a {tone.lower()} summary of the following:

- Numeric stats: {numeric_summary}
- Sentiment: {sentiment_summary}
- Cross-dataset links: {' | '.join(linked_insight_lines) if linked_insight_lines else 'None'}

Write a short paragraph summarizing trends, key figures, and relationships. Make it sound like a human wrote it."""

    try:
        result = summarizer(prompt, max_length=256, do_sample=False)
        response = result[0]['generated_text'].strip()
        return [f"📘 **Story:**\n\n{response}"]
    except Exception as e:
        return [f"⚠ Error generating story: {e}"]

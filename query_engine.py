import os
import json
import numpy as np
from transformers import pipeline

# Disable TensorFlow usage
os.environ["TRANSFORMERS_NO_TF"] = "1"

# Load the lightweight model
qa = pipeline("text2text-generation", model="google/flan-t5-base")

# Helper to convert numpy types for JSON serialization
def convert_to_builtin(obj):
    if isinstance(obj, dict):
        return {k: convert_to_builtin(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_builtin(v) for v in obj]
    elif isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    return obj

# Answer user questions based on a preview of the datasets
def answer_query(query, datasets):
    if not datasets:
        return "No datasets available."

    try:
        prompt = "Answer this question based on the following data:\n\n"
        for i, df in enumerate(datasets):
            preview = convert_to_builtin(df.head(10).to_dict(orient="records"))
            prompt += f"Dataset {i+1}:\n{json.dumps(preview, indent=2)}\n"

        prompt += f"\nQuestion: {query}\nAnswer:"

        result = qa(prompt, max_length=128, do_sample=False)[0]['generated_text']
        return result.strip()
    except Exception as e:
        return f"⚠ Error interpreting query: {e}"

import streamlit as st
import pandas as pd
import numpy as np

from data_loader import load_data
from analysis import numeric_summary, sentiment_analysis
from visualization import plot_distribution
from narrative_generator import generate_narrative_gpt
from insight_linker import link_insights_across_datasets


st.set_page_config(layout="wide")
st.title("🧠 Cognitive Data Storyteller (CDS)")

# Sidebar
st.sidebar.header("Settings")
tone = st.sidebar.selectbox("Narrative Tone", ["Formal", "Casual"])
anomaly_method = st.sidebar.selectbox("Anomaly Detection", ["iqr", "isolation_forest"])
uploaded_files = st.sidebar.file_uploader("Upload CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    datasets = []
    for file in uploaded_files:
        try:
            df = load_data(file)
            datasets.append(df)
        except Exception as e:
            st.error(f"Error in file {file.name}: {e}")
            continue

    if len(datasets) >= 1:
        df = datasets[0]

        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        st.subheader("📊 Summary Statistics")
        st.dataframe(df.describe(include='all'))

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        meaningful_cols = [col for col in numeric_cols if df[col].nunique() > 1]
        text_cols = df.select_dtypes(include=['object']).columns.tolist()

        num_summary = numeric_summary(df, meaningful_cols, method=anomaly_method)
        sentiment_summary = sentiment_analysis(df, text_cols)

        linked_insights = []
        if len(datasets) > 1:
            st.subheader("🔗 Cross-Domain Insight Linking")
            common_keys = st.text_input("Enter keys (comma-separated):", "Date,Product")
            keys = [k.strip() for k in common_keys.split(",")]
            linked_insights = link_insights_across_datasets(datasets, keys)
            if linked_insights:
                for link in linked_insights:
                    st.markdown(f"- 📎 Datasets {link['datasets'][0]} and {link['datasets'][1]} share {link['intersection_rows']} records on **{link['key']}**.")
            else:
                st.info("No cross-domain matches found.")

        st.subheader("🧠 AI-Generated Narrative")
        with st.spinner("Generating narrative..."):
            narrative_lines = generate_narrative_gpt(num_summary, sentiment_summary, tone=tone, linked_insights=linked_insights)
            for line in narrative_lines:
                st.markdown(f"- {line.strip()}")


        st.subheader("📊 Column Distribution")
        all_columns = df.columns.tolist()
        x_col = st.selectbox("X-axis column:", options=all_columns, index=0)
        y_col_options = ["Count"] + all_columns
        y_col = st.selectbox("Y-axis column (optional):", options=y_col_options, index=0)
        fig = plot_distribution(df, x_col, y_col)
        st.pyplot(fig)
        


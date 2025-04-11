import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, col, method="iqr"):
    if col not in df.columns:
        return pd.Series([False] * len(df))

    col_data = df[col].dropna().values.reshape(-1, 1)

    if method == "isolation_forest":
        model = IsolationForest(contamination=0.05, random_state=42)
        predictions = model.fit_predict(col_data)
        return pd.Series(predictions == -1, index=df[col].dropna().index).reindex(df.index, fill_value=False)

    # IQR method
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (df[col] < lower) | (df[col] > upper)

def numeric_summary(df, meaningful_cols, method="iqr"):
    summary = {}
    for col in meaningful_cols:
        col_data = df[col].dropna()
        stats = {
            'mean': col_data.mean(),
            'median': col_data.median(),
            'std': col_data.std(),
            'anomalies': detect_anomalies(df, col, method=method).sum()
        }
        summary[col] = stats
    return summary

def sentiment_analysis(df, text_cols):
    sentiment_summary = {}
    for col in text_cols:
        sample_texts = df[col].dropna().astype(str)
        if len(sample_texts) > 10 and sample_texts.str.len().mean() > 10:
            sentiments = sample_texts.apply(lambda x: TextBlob(x).sentiment.polarity)
            sentiment_summary[col] = sentiments.mean()
    return sentiment_summary

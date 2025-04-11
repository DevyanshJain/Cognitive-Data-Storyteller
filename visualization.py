import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_distribution(df, x_col, y_col):
    fig, ax = plt.subplots()
    if y_col == "Count":
        plot_data = df[x_col].value_counts().reset_index()
        plot_data.columns = [x_col, "Count"]
        sns.barplot(data=plot_data, x=x_col, y="Count", ax=ax, palette="Blues_d")
        ax.set_ylabel("Count")
    else:
        if pd.api.types.is_numeric_dtype(df[y_col]):
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax, palette="Blues_d")
        else:
            plot_data = df[x_col].value_counts().reset_index()
            plot_data.columns = [x_col, "Count"]
            sns.barplot(data=plot_data, x=x_col, y="Count", ax=ax, palette="Blues_d")
            ax.set_ylabel("Count")
    ax.set_title(f"Distribution: {x_col} vs {y_col}", fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    return fig

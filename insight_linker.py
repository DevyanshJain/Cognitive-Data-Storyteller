import pandas as pd

def link_insights_across_datasets(datasets, common_keys):
    linked_insights = []

    for i in range(len(datasets)):
        for j in range(i + 1, len(datasets)):
            df1 = datasets[i]
            df2 = datasets[j]

            for key in common_keys:
                if key in df1.columns and key in df2.columns:
                    merged = pd.merge(df1, df2, on=key, how='inner')
                    if not merged.empty:
                        linked_insights.append({
                            "datasets": (i, j),
                            "key": key,
                            "intersection_rows": len(merged)
                        })

    return linked_insights

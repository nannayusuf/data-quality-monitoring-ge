import pandas as pd
import os


def inject_outliers(input_file, output_file, column, outlier_value=-999, frac=0.05):
    df = pd.read_csv(input_file)
    outlier_indices = df.sample(frac=frac, random_state=42).index
    df.loc[outlier_indices, column] = outlier_value
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Outliers injetados e salvo em: {output_file}")

if __name__ == "__main__":
    inject_outliers(
        input_file='data/raw/olist/olist_order_items_dataset.csv',
        output_file='data/synthetic/olist_order_items_with_outliers.csv',
        column='price',
        outlier_value=-999
    )
    
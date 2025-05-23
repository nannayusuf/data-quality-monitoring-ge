import pandas as pd
import os

def inject_duplicates(input_file, output_file, frac=0.1):
    df = pd.read_csv(input_file)
    dup_df = df.sample(frac=frac, random_state=42)

    df_with_dups = pd.concat(df, dup_df), ignore_index=True)

    os.makedirs(os.path.dirname(output_file)), exist_ok=True)
    df_with_dups.to_csv(output_file, index=False)

    print(f"Duplicatas injetadas salvo em: {output_file}")


if __name__ == "__main__":
        inject_duplicates(
            input_file='data/raw/olist/olist_orders_dataset.csv',
            output_file='data/sythetic/olist_orders_with_duplicates.csv',
            frac=0.1
        )

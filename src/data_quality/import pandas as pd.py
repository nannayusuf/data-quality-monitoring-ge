
import pandas as pd
import os

def inject_date_inconsistencies(input_file, output_file, date_cols, frac=0.05):
    df = pd.read_csv(input_file, parse_dates=date_cols)
    
    inconsistent_indices = df.sample(frac=frac, random_state=42).index
    
    for idx in inconsistent_indices:
        # Troca as duas datas entre si
        df.at[idx, date_cols[0]], df.at[idx, date_cols[1]] = \
            df.at[idx, date_cols[1]], df.at[idx, date_cols[0]]
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Inconsistências de datas injetadas e salvo em: {output_file}")

if __name__ == "__main__":
    inject_date_inconsistencies(
        input_file='data/raw/olist/olist_orders_dataset.csv',
        output_file='data/synthetic/olist_orders_with_date_issues.csv',
        date_cols=['order_purchase_timestamp', 'order_delivered_customer_date'],
        frac=0.05
    )

import kagglehub
from kagglehub import KaggleDatasetAdapter

dataset = "olistbr/brazilian-ecommerce"
file = "olist_orders_dataset.csv"
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    dataset,
    file
)
print(df.head())

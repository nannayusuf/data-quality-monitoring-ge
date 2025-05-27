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

from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.data_context import DataContext 

context = DataContext()

batch_request = RuntimeBatchRequest(
        datasource_name="olist_data",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="olist_orders",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "test"}
)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="olist_suite"
)

validator.expect_column_values_to_not_be_null("product_id")

print("Expectation suite saved successfully!")

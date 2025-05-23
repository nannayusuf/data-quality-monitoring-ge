import great_expectations as ge
from great_expectations.data_context import FileDataContext
import pandas as pd

# Dados fictícios
data = {"order_id": [1, 2, None, 4]}
df = pd.DataFrame(data)

context = FileDataContext("/home/lena/projeto_ge/great_expectations")

batch = context.get_batch(
    batch_request={
        "datasource_name": "my_datasource",
        "data_connector_name": "default_runtime_data_connector_name",
        "data_asset_name": "my_data_asset",
        "runtime_parameters": {"batch_data": df},
        "batch_identifiers": {"default_identifier_name": "default_identifier"}
    },
    expectation_suite_name="my_suite"
)

results = context.run_checkpoint(checkpoint_name="my_checkpoint")
print(results)

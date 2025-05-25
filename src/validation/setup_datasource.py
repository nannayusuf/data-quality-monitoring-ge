from great_expectations.data_context import FileDataContext

context = FileDataContext("great_expectations")
context.add_datasource(
    name"=olist_data",
    class_name="Datasource",
    execution_engine={"class_name": "PandasExecutionEngine"},
    data_connectors={
        "default_runtime_data_connector_name":{
            "class_name": "Checkpoint",
            "run_name_template":"%Y-%M-%D-%H-%M-%S",
            "validations":[
        }
            "batch_request": {
                "datasource_name": "olist_data",
                "data_connector_name": "default_runtime_data_connector_name",
                "data_asset_name": "order_items_asset",
                "runtime_parameters": {
                    "batch_data": "<pandas_df_placeholder>"
                },
                "batch_identifiers": {
                    "default_identifier_name": "default"
                }
            },
            "expectation_suite_name": "order_items_suite"
        }
    ]
}
        
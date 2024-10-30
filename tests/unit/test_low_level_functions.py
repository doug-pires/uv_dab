import pyspark.sql.functions as F
from chispa.column_comparer import assert_column_equality

from uv_dab.low_level_functions.utils import add_current_timestampe_to_df


def test_add_correctly_current_timestamp_to_df(spark_session):
    # Given a DataFrame with some data and a fake timestamp
    data = [("dummy1",), ("dummy2",), ("dummy3",)]
    schema = ["dummy_column"]
    df = spark_session.createDataFrame(data, schema)

    # When we add the current timestamp to the DataFrame using the function

    df_with_timestamp = df.transform(add_current_timestampe_to_df).withColumn(
        "expected_ingestion_timestamp", F.current_timestamp()
    )
    print(df_with_timestamp.show(truncate=False))
    # Then the DataFrame should have a new column with the current timestamp
    assert "ingestion_timestamp" in df_with_timestamp.columns
    assert_column_equality(
        df_with_timestamp, "ingestion_timestamp", "expected_ingestion_timestamp"
    )

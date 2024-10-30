import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session():
    """
    PyTest fixture for creating a SparkSession.

    This fixture creates a SparkSession and automatically closes it at the end of the test session.

    Returns:
        SparkSession: An instance of SparkSession ready for use in tests.

    Example:
        ```python
        def test_spark_operations(spark_session):
            # Perform Spark operations using the provided SparkSession.
            df = spark_session.read.csv("test_data.csv")
            assert df.count() > 0
        ```
    """
    # Create a SparkSession

    spark = (
        SparkSession.builder.appName("pytest_spark_fixture")
        .master("local[1]")
        .getOrCreate()
    )

    # Set any necessary configuration options
    spark.conf.set("spark.sql.shuffle.partitions", "2")

    # Yield the SparkSession to the tests
    yield spark

    # Teardown - stop the SparkSession
    spark.stop()

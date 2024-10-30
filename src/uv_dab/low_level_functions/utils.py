from datetime import datetime
from typing import Any

import pyspark.sql.functions as F
from pyspark.sql import DataFrame


def add_current_timestampe_to_df(df: DataFrame) -> DataFrame:
    return df.withColumn("ingestion_timestamp", F.current_timestamp())


def add_word_count_to_df(df: DataFrame, col: str) -> DataFrame:
    return df.withColumn("word_count", F.size(F.split(F.col(col), " ")))


def save_file(path: str, data: list[dict, Any]) -> None:
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{path}/data_{current_datetime}.json", "w") as file:
        file.write(data)

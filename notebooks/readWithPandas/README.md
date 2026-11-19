# readWithPandas

`readWithPandas_v1.py` shows the three frames from the Databricks how-to:

- `spark.read` for a Spark DataFrame
- `.toPandas()` for Pandas Core, after the extract is small enough for one machine
- `pyspark.pandas.read_parquet` for the Pandas API on Spark

Large raw data stays on Spark. Pandas Core is for a few hundred rows.

# Databricks notebook source
# MAGIC %md
# MAGIC # readWithPandas
# MAGIC
# MAGIC Use Pandas Core only after the data is small enough for one machine. Use Pandas API on Spark when you want the pandas API on the cluster.

# COMMAND ----------

import pyspark.pandas as ps
import pandas as pd

environment = 'dev'
storage_account = 'storageaccount'
file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.parquet'

# PySpark
spark_df = spark.read.format('parquet').load(file_path)

# Pandas Core. This collects the rows onto the driver.
pd_df = spark_df.toPandas()

# Pandas API on Spark
ps_df = ps.read_parquet(file_path)

# COMMAND ----------

# Pandas Core back to Delta
out_path = '/mnt/adls-' + storage_account + environment + '-optimized/business-area/subject-area/dataset'
spark.createDataFrame(pd_df).write.format('delta').mode('overwrite').save(out_path)

# Pandas API on Spark back to Delta
ps_df.to_delta(out_path)

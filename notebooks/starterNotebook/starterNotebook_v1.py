# Databricks notebook source
# MAGIC %md
# MAGIC # starterNotebook
# MAGIC
# MAGIC Copy this file, set `environment` and `storage_account`, then change the path.

# COMMAND ----------

environment = 'dev'
storage_account = 'storageaccount'

file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.parquet'
spark_df = spark.read.format('parquet').load(file_path)

# COMMAND ----------

# Optional. Run this only when the data fits on one machine.
pd_df = spark_df.toPandas()

# COMMAND ----------

file_path = '/mnt/adls-' + storage_account + environment + '-optimized/business-area/subject-area/dataset'
spark_df.write.format('delta').mode('overwrite').option('overwriteSchema', 'True').save(file_path)

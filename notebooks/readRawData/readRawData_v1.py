# Databricks notebook source
# MAGIC %md
# MAGIC # readRawData
# MAGIC
# MAGIC Same pattern as the Databricks how-to: one mount path, then `spark.read`.

# COMMAND ----------

environment = 'dev'
storage_account = 'storageaccount'

file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.parquet'
spark_df = spark.read.format('parquet').load(file_path)

# COMMAND ----------

file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.json'
spark_df = spark.read.format('json').load(file_path)

# COMMAND ----------

file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.csv'
spark_df = spark.read.format('csv').option('header', 'true').load(file_path)

# COMMAND ----------

file_path = '/mnt/adls-' + storage_account + environment + '-enterprise/business-area/subject-area/dataset'
spark_df.write.format('delta').mode('overwrite').option('overwriteSchema', 'True').save(file_path)

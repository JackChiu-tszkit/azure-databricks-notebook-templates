# Databricks notebook source
# MAGIC %md
# MAGIC # writeOptimizedData
# MAGIC
# MAGIC Read Delta, write Delta, then register the path in the SQL warehouse.

# COMMAND ----------

environment = 'dev'
storage_account = 'storageaccount'

file_path = '/mnt/adls-' + storage_account + environment + '-enterprise/business-area/subject-area/dataset'
spark_df = spark.read.format('delta').load(file_path)

# COMMAND ----------

file_path = '/mnt/adls-' + storage_account + environment + '-optimized/business-area/subject-area/dataset'
spark_df.write.format('delta').mode('overwrite').option('overwriteSchema', 'True').save(file_path)

# COMMAND ----------

spark.sql(f"""
CREATE TABLE IF NOT EXISTS database_name.table_name_v1
USING DELTA
LOCATION '{file_path}'
""")

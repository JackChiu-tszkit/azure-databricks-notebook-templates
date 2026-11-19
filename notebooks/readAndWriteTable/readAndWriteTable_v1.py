# Databricks notebook source
# MAGIC %md
# MAGIC # readAndWriteTable
# MAGIC
# MAGIC Read a table from the Databricks database and save it back as a table. No mount path.

# COMMAND ----------

database_name = 'database_name'
source_table = 'source_table'
target_table = 'target_table'

spark.sql('CREATE DATABASE IF NOT EXISTS ' + database_name)

spark_df = spark.table(database_name + '.' + source_table)

# COMMAND ----------

# Optional. Run this only when the data fits on one machine.
pd_df = spark_df.toPandas()

# COMMAND ----------

spark_df.write.mode('overwrite').option('overwriteSchema', 'True').saveAsTable(database_name + '.' + target_table)

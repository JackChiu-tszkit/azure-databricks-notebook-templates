# Databricks notebook source
# MAGIC %md
# MAGIC # readAndWriteUnityCatalog
# MAGIC
# MAGIC Read a table directly from Unity Catalog and save it back to Unity Catalog.
# MAGIC
# MAGIC ## Where the data comes from
# MAGIC
# MAGIC Set `catalog_name` to the Unity Catalog catalog. On a workspace created on or after 8 October 2026, that catalog is created with the workspace and usually has the workspace name.
# MAGIC
# MAGIC A database and a schema are the same object. The full table name has three parts:
# MAGIC
# MAGIC `catalog_name.database_name.table_name`
# MAGIC
# MAGIC Find the three names in Catalog Explorer. In the left sidebar, click **Catalog**.
# MAGIC
# MAGIC 1. The first level is the catalog. Copy it into `catalog_name`.
# MAGIC 2. Open the catalog. The next level is labeled **Schema**. That is the database. Copy it into `database_name`.
# MAGIC 3. Open the schema. Copy the table you want to read into `source_table`.
# MAGIC 4. Click the table. The heading shows `catalog_name.database_name.table_name`.
# MAGIC
# MAGIC `spark.table` reads that table directly from Unity Catalog. `source_table` must already exist. This notebook creates the schema inside the catalog. It does not create the catalog or the source table. The last cell writes `target_table` into the same Unity Catalog schema with `saveAsTable`.

# COMMAND ----------

catalog_name = 'catalog_name'
database_name = 'database_name'
source_table = 'source_table'
target_table = 'target_table'

spark.sql('CREATE SCHEMA IF NOT EXISTS ' + catalog_name + '.' + database_name)

spark_df = spark.table(catalog_name + '.' + database_name + '.' + source_table)

# COMMAND ----------

# Optional. Run this only when the data fits on one machine.
pd_df = spark_df.toPandas()

# COMMAND ----------

spark_df.write.mode('overwrite').option('overwriteSchema', 'True').saveAsTable(catalog_name + '.' + database_name + '.' + target_table)

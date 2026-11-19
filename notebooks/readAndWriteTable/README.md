# readAndWriteTable

`readAndWriteTable_v1.py` reads and saves a table in the Databricks database. It does not use a mount path.

Set `database_name`, `source_table`, and `target_table`. The notebook creates the database if it is missing, reads `database_name.source_table`, and writes `database_name.target_table`.

The middle cell is optional: `pd_df = spark_df.toPandas()` when the data fits on one machine.

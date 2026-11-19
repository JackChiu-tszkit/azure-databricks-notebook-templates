# readAndWriteUnityCatalog

`readAndWriteUnityCatalog_v1.py` reads a table directly from Unity Catalog and saves it back to the same catalog.

Set `catalog_name` to the Unity Catalog catalog. On a workspace created on or after 8 October 2026, this catalog usually has the workspace name. A database and a schema are the same object. The table name is `catalog_name.database_name.table_name`.

The notebook creates the schema if it is missing. `spark.table` reads `source_table` from Unity Catalog. `saveAsTable` writes `target_table`.

The middle cell is optional: `pd_df = spark_df.toPandas()` when the data fits on one machine.

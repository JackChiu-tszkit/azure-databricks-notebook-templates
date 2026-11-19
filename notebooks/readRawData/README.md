# readRawData

`readRawData_v1.py` follows the Databricks how-to.

Set `environment` to `dev`, `test`, or `prod`. Set `storage_account` to your account name. The mount path is `/mnt/adls-<storageaccount><environment>-raw/...`.

The notebook reads Parquet, JSON, and CSV with `spark.read`, then writes Delta with `mode('overwrite')` and `overwriteSchema`.

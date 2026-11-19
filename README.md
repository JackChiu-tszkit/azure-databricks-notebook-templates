# Azure Databricks notebook templates

Short notebooks in the same style as the Databricks how-to. A mount path is built from `environment` and `storage_account`, then the notebook reads or writes with one `spark` call.

```python
environment = 'dev'
storage_account = 'storageaccount'
file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.parquet'
spark_df = spark.read.format('parquet').load(file_path)
```

`environment` is `dev`, `test`, or `prod`. `storageaccount` is a placeholder. There are no real account names, credentials, or cloud identifiers in this repository.

| Notebook | What it does |
| --- | --- |
| `notebooks/mountAzureDataLakeStorage/mountAzureDataLakeStorage_v1.py` | Mount the raw and optimized containers with a service principal. |
| `notebooks/readRawData/readRawData_v1.py` | Read Parquet, JSON, and CSV. Write Delta. |
| `notebooks/writeOptimizedData/writeOptimizedData_v1.py` | Read Delta and write Delta. Register the table. |
| `notebooks/readWithPandas/readWithPandas_v1.py` | Spark, Pandas Core, and Pandas API on Spark. |
| `notebooks/starterNotebook/starterNotebook_v1.py` | The same read and write, with nothing else. |
| `notebooks/readAndWriteTable/readAndWriteTable_v1.py` | Read a table from the Databricks database and save it back as a table. |

Run `mountAzureDataLakeStorage_v1.py` first. It creates `/mnt/adls-<storageaccount><environment>-raw` and `-optimized`. Replace `<tenant-id>` and point the secret-scope widgets at your own Key Vault secrets. The notebook does not contain a real tenant id, storage account, or secret.

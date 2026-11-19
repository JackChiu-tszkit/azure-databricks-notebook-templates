# Azure Databricks notebook templates

Short notebooks in the same style as the Databricks how-to. There are two ways to get data.

## 1. Mount Azure Data Lake Storage, then read from it

Mount the storage account on Azure Databricks, then read and write files on that mount.

```python
environment = 'dev'
storage_account = 'storageaccount'
file_path = '/mnt/adls-' + storage_account + environment + '-raw/business-area/subject-area/file.parquet'
spark_df = spark.read.format('parquet').load(file_path)
```

`environment` is `dev`, `test`, or `prod`. `storageaccount` is a placeholder. Run `mountAzureDataLakeStorage_v1.py` first. It creates `/mnt/adls-<storageaccount><environment>-raw` and `-optimized`. Replace `<tenant-id>` and point the secret-scope widgets at your own Key Vault secrets.

| Notebook | What it does |
| --- | --- |
| `notebooks/mountAzureDataLakeStorage/mountAzureDataLakeStorage_v1.py` | Mount the raw and optimized containers with a service principal. |
| `notebooks/readRawData/readRawData_v1.py` | Read Parquet, JSON, and CSV. Write Delta. |
| `notebooks/writeOptimizedData/writeOptimizedData_v1.py` | Read Delta and write Delta. Register the table. |
| `notebooks/readWithPandas/readWithPandas_v1.py` | Spark, Pandas Core, and Pandas API on Spark. |
| `notebooks/starterNotebook/starterNotebook_v1.py` | The same read and write, with nothing else. |

## 2. Read directly from Unity Catalog

Skip the mount. Read and save a table in Unity Catalog with the three-part name `catalog_name.database_name.table_name`.

```python
catalog_name = 'catalog_name'
database_name = 'database_name'
source_table = 'source_table'
spark_df = spark.table(catalog_name + '.' + database_name + '.' + source_table)
```

Find the three names in the Azure Databricks workspace. The notebook does not list them for you.

1. In the left sidebar, click **Catalog**. Catalog Explorer opens beside the notebook.
2. The first level is the catalog. Copy that name into `catalog_name`. On a workspace created on or after 8 October 2026, this is usually the workspace name.
3. Open that catalog. The next level is labeled **Schema**. A schema is the database. Copy that name into `database_name`.
4. Open that schema. Each entry under **Tables** is a table name. Copy the one you want to read into `source_table`.
5. Click the table. The heading shows the full name `catalog_name.database_name.table_name`.

| Notebook | What it does |
| --- | --- |
| `notebooks/readAndWriteUnityCatalog/readAndWriteUnityCatalog_v1.py` | Read a table directly from Unity Catalog and save it back to Unity Catalog. |

There are no real account names, credentials, or cloud identifiers in this repository.

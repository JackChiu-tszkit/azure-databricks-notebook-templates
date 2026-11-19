# mountAzureDataLakeStorage

`mountAzureDataLakeStorage_v1.py` mounts Azure Data Lake Storage. Run it once in the workspace that matches the secret scope.

Widgets:

- `scope`, `key`, `id`, `type`: secret scope and the three secret names (OAuth provider type, client id, client secret)
- `environment`: `prod`, `dev`, or `test`
- `storage_account`: account name prefix. The account used is `<storage_account><environment>`
- `tenant_id`: directory tenant id. Replace `<tenant-id>` before you run it

It mounts two containers:

- `abfss://raw@<storageaccount><environment>.dfs.core.windows.net/` to `/mnt/adls-<storageaccount><environment>-raw`
- `abfss://optimized@<storageaccount><environment>.dfs.core.windows.net/` to `/mnt/adls-<storageaccount><environment>-optimized`

If a path is already mounted, the cell prints `Already mounted or could not mount`.

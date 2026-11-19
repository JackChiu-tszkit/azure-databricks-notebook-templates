# writeOptimizedData

`writeOptimizedData_v1.py` loads the enterprise Delta path and writes the optimized Delta path.

The last cell registers that path:

```sql
CREATE TABLE IF NOT EXISTS database_name.table_name_v1
USING DELTA
LOCATION '/mnt/adls-<storageaccount><environment>-optimized/...'
```

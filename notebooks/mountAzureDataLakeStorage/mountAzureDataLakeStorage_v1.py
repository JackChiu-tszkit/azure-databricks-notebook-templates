# Databricks notebook source
# MAGIC %md
# MAGIC # mountAzureDataLakeStorage
# MAGIC
# MAGIC A secret scope belongs to one workspace. In the prod workspace, choose `prod` and `secretscope-prod`. Do the same for dev and test.
# MAGIC
# MAGIC ## Where each value comes from
# MAGIC
# MAGIC The notebook never contains the client id or the client secret. It only selects their names.
# MAGIC
# MAGIC 1. Create the secret scope in Databricks, not in this notebook. Open `https://<workspace-host>#secrets/createScope` and enter the scope name, the Key Vault DNS name, and the Key Vault resource ID. Use `secretscope-dev`, `secretscope-test`, or `secretscope-prod` in the matching workspace.
# MAGIC 2. Store three secrets in that Key Vault:
# MAGIC    - `client-id`: application (service principal) client id
# MAGIC    - `client-secret`: client secret for that application
# MAGIC    - `oauth-provider-type`: `org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider`
# MAGIC 3. Run the next cell. Widgets appear at the top of the notebook. Select `scope`, `id`, `key`, and `type`. Type `storage_account` and replace `<tenant-id>`.
# MAGIC 4. Run the mount cell. `dbutils.secrets.get` reads the secret values from Key Vault.
# MAGIC
# MAGIC | Widget | What you select | Where the value lives |
# MAGIC | --- | --- | --- |
# MAGIC | `scope` | `secretscope-dev`, `secretscope-test`, or `secretscope-prod` | Databricks secret scope for this workspace |
# MAGIC | `id` | `client-id` | Key Vault secret name for the client id |
# MAGIC | `key` | `client-secret` | Key Vault secret name for the client secret |
# MAGIC | `type` | `oauth-provider-type` | Key Vault secret name for the OAuth provider class |
# MAGIC | `environment` | `dev`, `test`, or `prod` | Same workspace you are in |
# MAGIC | `storage_account` | account name prefix | Typed in the widget. The account is `<storage_account><environment>` |
# MAGIC | `tenant_id` | directory tenant id | Typed in the widget. Replace `<tenant-id>` |
# MAGIC
# MAGIC The dropdown lists are fixed in the next cell. If a Key Vault secret has another name, change that list, run the cell again, then pick the new name in the widget.

# COMMAND ----------

# parameterize scope for mounting
dbutils.widgets.dropdown('scope', 'secretscope-prod', ['secretscope-prod', 'secretscope-dev', 'secretscope-test'])
dbutils.widgets.dropdown('key', 'client-secret', ['client-secret'])
dbutils.widgets.dropdown('id', 'client-id', ['client-id'])
dbutils.widgets.dropdown('type', 'oauth-provider-type', ['oauth-provider-type'])
dbutils.widgets.dropdown('environment', 'prod', ['prod', 'dev', 'test'])
dbutils.widgets.text('storage_account', 'storageaccount')
dbutils.widgets.text('tenant_id', '<tenant-id>')

# create variables
scope_secret = dbutils.widgets.get('scope')
scope_key = dbutils.widgets.get('key')
scope_id = dbutils.widgets.get('id')
scope_type = dbutils.widgets.get('type')
environment = dbutils.widgets.get('environment')
storage_account = dbutils.widgets.get('storage_account')
tenant_id = dbutils.widgets.get('tenant_id')

# COMMAND ----------

# run once to mount Azure Data Lake Storage Gen2 to access content
# Source: https://docs.databricks.com/data/data-sources/azure/adls-gen2/azure-datalake-gen2-sp-access.html
# set configuration settings
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": dbutils.secrets.get(scope=scope_secret, key=scope_type),
          "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope=scope_secret, key=scope_id),
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope=scope_secret, key=scope_key),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/" + tenant_id + "/oauth2/token"}
try:
    # mount raw container
    dbutils.fs.mount(
      source = 'abfss://raw@' + storage_account + environment + '.dfs.core.windows.net/',
      mount_point = '/mnt/adls-' + storage_account + environment + '-raw',
      extra_configs = configs)
except:
    print('Already mounted or could not mount')

try:
    # mount optimized container
    dbutils.fs.mount(
      source = 'abfss://optimized@' + storage_account + environment + '.dfs.core.windows.net/',
      mount_point = '/mnt/adls-' + storage_account + environment + '-optimized',
      extra_configs = configs)
except:
    print('Already mounted or could not mount')

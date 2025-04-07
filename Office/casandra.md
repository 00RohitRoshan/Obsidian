✅ Recommended Options for Read-Only Use Case
✅ 1. Create a Materialized View (MV)
If the data is inserted into this table, and you're not writing yourself, you can still create a Materialized View to expose a different query model — without modifying the write logic.
```sql
CREATE MATERIALIZED VIEW IF NOT EXISTS camunda_workflow_mv AS
SELECT 
  tenant_id,
  product_flow_name,
  current_task_assignee,
  process_creation_date,
  process_id,
  total_calls,
  total_apis_call,
  total_forms_fetch
FROM camunda_workflow
WHERE 
  tenant_id IS NOT NULL AND 
  product_flow_name IS NOT NULL AND 
  current_task_assignee IS NOT NULL AND 
  process_creation_date IS NOT NULL AND 
  process_id IS NOT NULL
PRIMARY KEY ((tenant_id, product_flow_name, current_task_assignee), process_creation_date, process_id);
```
Why this works:
Cassandra will automatically keep the MV in sync with the base table.

You can query it like this (no filtering needed):

```sql
SELECT SUM(total_calls), SUM(total_apis_call), SUM(total_forms_fetch)
FROM camunda_workflow_mv
WHERE 
  tenant_id = ?
  AND product_flow_name = ?
  AND current_task_assignee = ?
  AND process_creation_date >= ?
  AND process_creation_date <= ?;
```
✅ No ALLOW FILTERING
✅ Fast + scalable
✅ No write logic changes needed

⚠️ Just be aware: materialized views can occasionally go out of sync or cause performance issues under heavy write load, but if you’re only reading, and the write volume isn't insane, it's a valid solution.

Index
Cassandra doesn’t handle multi-column indexes well, and range queries on secondary indexes are not supported.


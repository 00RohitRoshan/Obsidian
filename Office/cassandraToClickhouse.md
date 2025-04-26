- make cassandra connection pool
- make clickhouse connection pool
- check and get the latest inserted time
    - filter by latest time to now
        - run a goroutine to insert these to clickhouse
- filter by time all data upto now
    - create table
    - run a goroutine to insert these to clickhouse
- create ticker
- run a goroutine every one hour from time.Now

one function to query and fetch on time range
what about feature?

---
- make cassandra connection pool
- make clickhouse connection pool
- craete ticker 
- check and get the latest inserted time
    - update data latest time to now
    - if table doesn't exists create table
        - start inserting data until now



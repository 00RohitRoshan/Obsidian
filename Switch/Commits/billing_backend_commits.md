# Commit History for 'billing_backend'

## Branch: origin/main

Initial commit
## Branch: origin/stage

feat: Implement feature graph and bank list endpoints with corresponding request and response structures

feat: Add feature list API with request and response structures

feat: Initialize global configurations and database connection

- Added global package with initialization logic for Cassandra database connection.
- Implemented logging to a file for application events.
- Configured TLS settings for secure database communication.
- Created a new Go module for the project with necessary dependencies.

feat: Implement API handlers for fetching billing details and heartbeat check

- Added GetApiCalls handler to process API call requests and fetch data from Cassandra.
- Implemented dynamic query building based on request parameters.
- Created HeartBeat handler to check the service status.

chore: Set up main application entry point

- Configured Fiber web server with routes for API calls and heartbeat check.
- Ensured proper resource cleanup on application exit.

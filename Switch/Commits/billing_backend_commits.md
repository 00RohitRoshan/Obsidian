# Unique Commit Messages for 'billing_backend'
- Added GetApiCalls handler to process API call requests and fetch data from Cassandra.
- Added global package with initialization logic for Cassandra database connection.
- Configured Fiber web server with routes for API calls and heartbeat check.
- Configured TLS settings for secure database communication.
- Created HeartBeat handler to check the service status.
- Created a new Go module for the project with necessary dependencies.
- Ensured proper resource cleanup on application exit.
- Implemented dynamic query building based on request parameters.
- Implemented logging to a file for application events.
Initial commitfeat: Implement feature graph and bank list endpoints with corresponding request and response structures
chore: Set up main application entry point
feat: Add feature list API with request and response structures
feat: Implement API handlers for fetching billing details and heartbeat check
feat: Initialize global configurations and database connection

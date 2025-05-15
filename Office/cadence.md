#### Cadence
- It is a durable function platform, like a platform for distributed lambda function execution but with logic check and order for those lambda function.
- The flow needs to be written through code.
- A common Cadence-based application consists of a Cadence service, workflow and activity_workers, and external clients.
![topology](https://user-images.githubusercontent.com/14902200/160308507-2854a98a-0582-4748-87e4-e0695d3b6e86.jpg)
- The service exposes all of its functionality through a strongly typed gRPC API.
- A Cadence cluster include multiple services, each of which may run on multiple nodes for scalability and reliablity:
    - Front End: which is a stateless service used to handle incoming requests from Workers. It is expected that an external load balancing mechanism is used to distribute load between Front End instances.
    - History Service: where the core logic of orchestrating workflow steps and activities is implemented
    - Matching Service: matches workflow/activity tasks that need to be executed to workflow/activity workers that are able to execute them. Matching is assigned task for execution by the history service
    - Internal Worker Service: implements Cadence workflows and activities for internal requirements such as archiving
    - Workers: are effectively the client apps for Cadence. This is where user created workflow and activity logic is executed
- Apache Cassandra, MySQL, PostgreSQL, CockroachDB (PostgreSQL compatible) and TiDB (MySQL compatible) stores are supported out of the box
- Cadence service is responsible for keeping `workflow state` and `associated durable timers`. It maintains internal queues (called task_lists) which are used to dispatch tasks to external workers.
##### Execution

![execution](https://user-images.githubusercontent.com/14902200/160308592-400e11bc-0b21-4dd1-b568-8ac59005e6b7.svg)  
- Here the `Workflow starter` starts the workflow `driverRewards` with parameter driverID.
- Then in the workflow `driverRewards` has two possible cases based on checkEligibility which controls the flow direction.
- The implementation of the bussiness logic implemented in the activity worker `DriverRewardsActivitiesImpl`
- Cadence manages the required function calls.
##### Workflow worker
- The workflow code is hosted by an external (from the service point of view) workflow_worker process. 
- The Cadence service does not execute workflow code directly. 
- These processes receive decision_tasks that contain events that the workflow is expected to handle from the Cadence service, delivers them to the workflow code, and communicates workflow decisions back to the service.
- The state of the workflow code, including local variables and threads it creates, is immune to process and Cadence service failures. It encapsulates state, processing threads, durable timers and event handlers.
- Workflow_ID is assigned by a client when starting a workflow. Cadence guarantees that there could be only one workflow (across all workflow types) with a given ID open per domain at any time. An attempt to start a workflow with the same ID is going to fail with WorkflowExecutionAlreadyStarted error.
- A workflow can execute other workflows as child :workflow:workflows:. A child workflow completion or failure is reported to its parent.
- Workflow code is unaffected by infrastructure level downtime and failures. But it still can fail due to business logic level failures. For example, an activity can fail due to exceeding the retry interval and the error is not handled by application code, or the workflow code having a bug.
##### Activity Worker
- Activities are hosted by activity_worker processes that receive activity_tasks from the Cadence service, invoke correspondent activity implementations and report back task completion statuses.
- Cadence activities are very feature-rich compared to queuing systems. 
- Such as task routing to specific processes, infinite retries, heartbeats, and unlimited execution time.
- Cadence does not recover activity state in case of failures. 
- Activities are invoked asynchronously through task_lists. A task_list is essentially a queue used to store an activity_task until it is picked up by an available worker. The worker processes an activity by invoking its implementation function. When the function returns, the worker reports the result back to the Cadence service which in turn notifies the workflow about completion. It is possible to implement an activity fully asynchronously by completing it from a different process.
##### External Clients / workflow starter
- workflows are started by outside entities like UIs, microservices or CLIs are called `external clients`.
- can also:
    - notify workflows about asynchronous external events in the form of signals
    - synchronously query workflow state
    - synchronously wait for a workflow completion
    - cancel, terminate, restart, and reset workflows
    - search for specific workflows using list API
### In comparison to CAMUNDA
- It has no in build tasklist UI and user task , though interactive application can be made but it requires fontend application code change for every new flow.
- There is no drag & drop flow builder , workflow needs to be created through code with error handling.
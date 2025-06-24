    set status failed for delteotaschedule api
 added fetchresultcount api
 changes in sdk
 made changes in fetch and delete api
 optimised logs
"Error in the padding or block size in the payload."
-	modified:   database/dbconn.go
- Added GetApiCalls handler to process API call requests and fetch data from Cassandra.
- Added global package with initialization logic for Cassandra database connection.
- Configured Fiber web server with routes for API calls and heartbeat check.
- Configured TLS settings for secure database communication.
- Created HeartBeat handler to check the service status.
- Created a new Go module for the project with necessary dependencies.
- Ensured proper resource cleanup on application exit.
- Implemented dynamic query building based on request parameters.
- Implemented logging to a file for application events.
.\.git\stage code added
AWS Things Creation while inserting data
Add OtaLedgerAPI url
Add error handling for missing SecretNameRedis and SecretNameMongo environment variables
Application to check device_status
CHnages in
Change in MQTT connection
Change in config file
Change in config.env
Change in config.go
Change in db connection
Change in docker file
Change in fetchInv
Change in graylog package
Change in init
Change in init.go
Change in insert API
Change in response body
Change in uploadbin
Change1
Changed the NodeApi url
Changed the OTALedger API
Changed the SM for master
Changed the SMs for master
Changed the query
Changed the secret manager url for BankUserSecret
Changed the service name of node API
Changed the service name of node APIs.
Changes
Changes from
Changes in data
Changes in validation
Chnages in fix conflict
Chnages in validation
Client_id or Client_secret miss-match
DeviceInfo endpoint
Dockerfile Updated
Encryption Only For 200 Status Code , Accept all content encoding formats
FechAll api addded
Fix MongoDB TLS CA file name in Envvariables function
Handled error
Handled errors
Implemented OTALedger API
Implemented grayLog
Implemented graylog
Initial commit
Initial commit add updated code
Initial commitChange in graylog package
Initial commitChanged the NodeApi url
Initial commitChanged the query
Initial commitImplemented the git library
Initial commitImplemented the library
Initial commitInitial commitChanged the OTALedgerUrl
Initial commitInitial commitChanged the service name of node APIs.
Initial commitInitial commitadd header buffer increase
Initial commitInitial commitadded defer in db conn
Initial commitInitial commitchanged db sm
Initial commitInitial commitchanged in mqtt connection
Initial commitInitial commitchanged the token properties
Initial commitInitial commitdone some minor changes
Initial commitInitial commitrun prod on docerfile
Initial commitMerge branch 'stage' into 'main'
Initial commitRedis TLS
Initial commitSet DB environment variable in Envvariables function
Initial commitad
Initial commitadd changes
Initial commitadd differnetiation for apiuser and wl
Initial commitadd maltrail configs
Initial commitadd prod aws final
Initial commitadd rate limit
Initial commitadded defer
Initial commitauth-app
Initial commitauthentication fails when key not present in both DB
Initial commitbankit gateway
Initial commitbin upload added
Initial commitchange in db connection
Initial commitchange in fetchInv
Initial commitchange in upload_in_bucket
Initial commitchange some logs
Initial commitchanged sm for prod
Initial commitchanged the allowed methods
Initial commitchanged the query of fetch deviceInfo2
Initial commitchanged the token properties
Initial commitchanges in ippb gateway
Initial commitcode update for ippb using token
Initial commitconfig file implemented and logging done
Initial commitcreate  local file for cert and key
Initial commitdb chng
Initial commitdb credentials updated
Initial commitdecryption and encryption done for the endpoint
Initial commitdocker version changed to 1.22-bullseye
Initial commitenc added
Initial commitfeat: Implement feature graph and bank list endpoints with corresponding request and response structures
Initial commitfinal Referemce Code v1
Initial commitfinal app
Initial commitfinal rate-limit code
Initial commithandled error
Initial commitheader key routing
Initial commitimplemented pull pubsub data store in db
Initial commitjti
Initial commitkey implementedc in header
Initial commitmade changes for disabled feature
Initial commitmade changes in fetchDevices.go
Initial commitnew branch for uat
Initial commitnew redirect proxy pass app
Initial commitnoise handle
Initial commitoptions add
Initial commitprod code
Initial commitprod gateway
Initial commitprod jwt code
Initial commitprod redis cred added
Initial commitredirect app
Initial commitredis TLS
Initial commitrefactor main function to use environment variable for targetURL and improve logging
Initial commitremoved ip whitelist & changed DB to cardclientstage
Initial commitremoved role from token
Initial commitrequest redirect app
Initial commitresponse_code_changed to -1
Initial commitrollback added
Initial committest code
Initial commitupdated code
Initial commitupdated redirect code with go-proxy package
LocalCred
Made redis connection
Merge branch 'aadharvault' of https://gitlab.com/reeturaj/aadharvalut into aadharvault
Merge branch 'common_stage' of https://gitlab.txninfra.com/soundbox/tms/device-registration into common_stage
Merge branch 'internalStage' of https://gitlab.iserveu.tech/soundbox/tms/device_inventory into internalStage
Merge branch 'stage' into 'main'
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/BOB/bob-soundbox-device-activity-status-golang-service into stage
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/slice/slice-soundbox-device-inventory into stage
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/tms/device-mapping into stage
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/tms/mqtt_config_internal into uat
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/tms/otamanagementadminapi into uat
Merge branch 'stage' of https://gitlab.txninfra.com/soundbox/tms/otamanagementinternal into uat
Merge branch 'test' into 'main'
Merge branch 'unifiedgateway_prod' of https://gitlab.com/sovitacharya/extauth-istio into unifiedgateway_prod
Merge branch 'unifiedgateway_stage' of https://gitlab.com/sovitacharya/extauth-istio into unifiedgateway_stage
Merge remote-tracking branch 'origin/aadharvault'
OPtimised code
OS check and port configuration
Production code
REDiS SM Key
Read buffer size added
Redis SM
Redis SM Key
Refactor MongoDB replica set string formatting in Envvariables function
Refactor Redis and MongoDB certificate file handling in createRedisPool and Envvariables functions
Refactor Redis and MongoDB credential structures and initialization to get secret from env
Refactor Redis connection initialization and error handling in createRedisPool and GetMongoClient functions
Removed the json file
Renamed the Dockerfile
SM Redis
SM key
See merge request sovitacharya/extauth-istio!1
See merge request sovitacharya/redirect_application!2
Test
Update Redis secret name environment variable to 'SecretNameRedis'
ad
add 3rd key
add apiusername feature
add card -stage
add cbsgw-stage
add changes
add client id and apiusername
add comments
add differnetiation for apiuser and wl
add file create and get
add insert to redis for existing ips
add ippb configs
add ippb db details and remove ip checks
add ippb updated code
add key
add mongo secret manager
add new mongo creds and change in secret manager
add new primary mongo node config
add new redis implementation
add prod gateway url
add redis
add redis cache and delete feature from redis
add remove set
add singularity modification for client id and ip for whitelisting
add stage db
add stage final redirect maps
add unknown
add username and client id
add whitelistig concept for prod
add whitelisting feture with redis
added 2 fields
added JSON validator for request
added acknowlege for play status already success in db
added api for fetch result count
added apiusername key to response header
added auth token validation
added bankcode in req
added bankcode to req body
added both jwt and clientsecret authentication
added check for adminname
added check for internal
added config part for server
added conn close part in postgres
added conn pooling
added defer
added deleteOtaLedger api
added else condition
added endpoint for deleteOtaLedger api
added fetch APIs for admin and api
added fetch device info api
added few conditions in device mapping api
added few validation
added gitignore file
added greylog
added heartBeat API
added jwt token part from oauth app
added key part in redisinsertclient
added logs
added logs and uncommented allow cors headers
added logs of client_id client_secret apiusername and key
added mongo part for rateconfigip
added mqtt_details field
added new SM
added new endpoint for no_auth device mapping
added ota_version in fetch ota api
added ota_version in fetchota api
added ota_version in otacreate api
added ota_version in req for otacreate api
added priviledge for user
added priviledges
added proper logs and methods
added rateconfigIp api
added redis part in update
added rollback for unmaping
added secret manager part for mongo client
added server config
added sm key
added some logs to verify query hit time difference
added support for content-encoding of br type
added trim for schedule and update api
added unique constraint for createota api
added unique constraint in createota api
added update part for rateconfigip endpoint
added validation for start date
adding logs for response
adding statuscode in logs
allowed all methods
api user go stage final without redis
apiuser code
apiusername resolved for redis
bankcode added in req
bin upload added
bring final
cahnge endpoint
card-stage
card-switch-apiuser-redirect
certificate added to the redis cluster
change in DeviceMappingAdmin
change in InsertInv
change in Token_properties
change in config file
change in config.go
change in db connection
change in dbconnection
change in fetchApi
change in fetchInv
change in init.go
change in main.go
change in query
change in redis code
change in request method type
change in secret manager
change in string
change in subscriber.go
change in upload bin
change in upload_in_bucket
change some logs
change the bankcode for redis
change the database attribute name
change type for ledger id
changed admin check part
changed aws policy
changed caCert type used file by name
changed code for scheduleota
changed conn string
changed connection string
changed connstring for db admins
changed db credentials
changed db name
changed docker file
changed docker file and privilege id
changed endpoint
changed endpoint format
changed error symbol in logs due to log.printf to fmt.printf
changed few logic in mapping api
changed few logics of mapping
changed hbt endpoint
changed in add device
changed in aws policy
changed in device maping
changed in device mapping
changed in docker
changed in endpoint names
changed in fetch api
changed in fetchAll api
changed in fetchall api
changed in go version
changed in init
changed in insert inv
changed in logic
changed in logs
changed in mqtt conn
changed in redis connection
changed in register.go
changed in response body of node api
changed in token_properties
changed in updateStatus
changed json key  for mqtt
changed listener url
changed log.printf to fmt.printf
changed methods for api
changed mqtt config struct
changed port
changed port address
changed port in docker
changed public key
changed redis connection
changed redis insert part
changed secret manager access part
changed server port
changed sm for prod
changed sm for stage bob
changed sm key for prod
changed some logics
changed status code
changed status codes
changed struct for token
changed struct for token properties
changed the BankCode
changed the SM for master
changed the SM for redis
changed the SM url
changed the admin_name validation
changed the allowed methods
changed the bankcode
changed the config file
changed the endpoint
changed the field name
changed the json field
changed the map and unmap url
changed the map and unmap urls
changed the message passed in response body
changed the method
changed the mqtt SM
changed the node API url
changed the node api url
changed the nodeApiUrl
changed the otaLedger url
changed the otaledger url for stage
changed the privillege id
changed the query of fetch deviceInfo2
changed the redis SM
changed the redis sm
changed the required details for SLICE
changed the required details for slice
changed the responses according to conditions
changed the status desc
changed the url
changed the validation for admin
changed token part
changed token struct
changed type
changed upadate and fetch query , now only using publish id for fetching and updating
changed url for mongodb
changes
changes done for pass_key and handled error for new sdk-requirement
changes for aes_adhaar_vault
changes for isu-switch-staging
changes for optimize
changes for ota_schedule_api
changes for uat
changes in decryption
changes in docker file
changes in go.mod
changes in ippb encr decr with encrypted and epoch handle
changes in mqtt_config
changes in scheduleota api
changes regarding new sdk-flow
checkip is commented
chore: Set up main application entry point
code for admin & api portal
code updated for ippb deleteclient and enable/disable added
commit1
config added
config commented
config file implemented and logging done
config for tls connection in mongodb is hardcoded
config.env modification
connection Pool exhausted issue resolved
corrected env varaible
corrected return type in grpc
cors
cors handled
created a subscriber
created new api for device mapping
curren_status field added
database changed
database host change
db changed
db chng
db cred updated for uat
db credentials changed
db credentials updated
db crentials changed
db sm changed for stage
db url changed
dburl changed
defer st added
delete_client added
disabled and checkclient merged
docker file added
docker file changed
done some minor changes
duu
enable/disable added
enabled secret manager
encr decr logic implemented
endpoint
endpoint changed
env file implemented
epoch time validation added
error handled
error handled for apiusername
ext-authcode
feat: Add feature list API with request and response structures
feat: Implement API handlers for fetching billing details and heartbeat check
feat: Initialize global configurations and database connection
fetch api added
fetch error handled
fetch ota_ledger api added
final Referemce Code v1
final apiuser auth application
final app
final change
final changes
final code
final code base
final code clean
final jwt code
final prod code
final prod manager
final rate limit stage
final redirect app
final-prod-auth
first
fix bug
fixed bankcode in req
fixed bug
fixed errorcode
fixed init
fixed otaschedule api
fixed schedule ota api and added trim func
fixed schedule ota api and added trim func for string fields
formatting done
grayLog added
grayLog credentials changed
hadled error
handle 431 error
handled 431 error
handled GET type request
handled all method allowed case
handled all methods failed case
handled bugs
handled cors error
handled duplicate entry for mqtt config
handled error
handled errors
handled if block when null headersecretes is there its getting passed inside the if block which panics the server
handled the redis connection error to solve the nil pointer issue
hard coded key for sdk-redirect isu-internal
header commented to stop 431 error
heartbeat API created
image update
implemented SM for MQTT connection
implemented grayLog
implemented graylog
implemented graylogs
imported strings package
in tokenproperties role is updated from string to []string
in tokenproperties role is updated to []string ,initially it was string
inital commit
initial commit
initial commit for stage
initial commit to main
inserted date and time through insertInv API
inserted mqtt name through  insertInv API
insertrd is_soundbox inside device_info
internal api changed
invStatus API added
ip changed to service
ippb ip port
ippb prod
ippb- encr
ippb-auth-gateway-stage
kept validations for request body fields
key creation and insertion added in mongodb
key generation added
key implementedc in header
key is added in header
key is got throgh header
language update api
latest code
latest code for csc
log changed to fmt as error is shown in logs
log changes
logged resp struct
logging done
logging for redis and mongo updated
logging updated
logs changes
logs handled
made change for local testing
made changes for admin user
made changes for bob
made changes for disabled feature
made changes for exposed ip
made changes for prod
made changes for quality code
made changes for redisdeletecollection
made changes for req for internal
made changes for scheduleota , deleteota, deleteledger api
made changes for sm
made changes for stage
made changes for uat
made changes in config
made changes in db connection
made changes in db.go
made changes in dbconnect
made changes in dockerfile
made changes in fetch and delete api
made changes in fetch device api
made changes in fetchOta api
made changes in init
made changes in logs and methods
made changes in redis
made changes in updateStatus api
made changes in url
made changes in validation
made changes uat
made db connection
made few changes
made the necessary changes for SLICE
made the required changes for SLICE
minor changes
mod file name change
modified the select.conn.Release()
modified the validation file
modify Response Commented Out
mqtt config struct changed
mqtt data configuration through secret manager
new app with redis and mongo whitelisting
new branch for PROD
new branch for aws
new branch for internal
new branch for production
new branch for uat
new db conn
new db conn1
new field added
new flow changes with encrypt decrypt changes
new mongo ip
new primary node ip
new redirect proxy pass app
new workflow for sdk-auth-staging
noise removed
optimised code
optimized code
optimized logs
options add
panic coming in logs: resolved the issue
path issue fixed
payload not header_secret
pkg add redis rate limit
playsound status callback implemented
print statement
print statement changed
prod apiuser auth app
prod final
prod gateway
prod new url
prod redis cluster
prod redis cred added
prod redis creds used
prod redis used and config is set
prod-jwt application
pulled from staging
push latest code
query optimization
rate limit implementation along with client combination redis implementation
redeclared function commented out
redirect app
redis TLS
redis added
redis and mongo logging updaetd
redis connection config change
redis prod cred used
removed bankcode
removed config file
removed config from env
removed config.env
removed database url
removed db ip
removed docker file
removed ip whitelist feature
removed role from token
removed the db url
removed the extra connections
removed the files
request nil is handled
resolve test 431
response key commented out
response_code_changed to -1
rm unnecessary data
rollback added
secret db access
secret key added
secret manager
secret manager added for redis
secret manager implemented
services added for ota-management
services added for tms
set status failed for delteotaschedule api
sm redis  tls
solved issue in insert
solved redis connection issue and  handled some logs
solved token issues
ssl pgsql db added
stage build code
stage code with ip block
staging created for unifiedgateway credentials updated for stage
table name changed
temp changes changes regarding content-type
test code
tls certificate added for redis
tls config
to handle apiuser clients
tokenHeaderjwt added
tsl connection to mongodb
uat branch created
uat-auth
uat-redirect
uncommented checkip part
unified gateway code
update decrypt-func
update go
update ip blocklist with redis cache
update proxyHandler to include query parameters in application endpoint
updated
updated bankcode part
updated code
updated code using switch case
updated ippb gateway auth
updated redirect code with go-proxy package
updated the error codes and messages accordingly in sdk-stage gateway.
upload mp3 file code
url added
url change https to http
used kubeds instead of ip
used toggleStatus api
validation added
validation added for fetch device
whitelabel app

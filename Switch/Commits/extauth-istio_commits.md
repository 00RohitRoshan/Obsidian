# Unique Commit Messages for 'extauth-istio'
 changes in sdk
-	modified:   database/dbconn.go
Add error handling for missing SecretNameRedis and SecretNameMongo environment variables
Client_id or Client_secret miss-match
Dockerfile Updated
Fix MongoDB TLS CA file name in Envvariables function
Initial commit
Initial commitRedis TLS
Initial commitSet DB environment variable in Envvariables function
Initial commitadd changes
Initial commitadd differnetiation for apiuser and wl
Initial commitadd prod aws final
Initial commitadd rate limit
Initial commitauth-app
Initial commitauthentication fails when key not present in both DB
Initial commitcode update for ippb using token
Initial commitcreate  local file for cert and key
Initial commitdb chng
Initial commitdb credentials updated
Initial commitfinal Referemce Code v1
Initial commitfinal rate-limit code
Initial commitjti
Initial commitkey implementedc in header
Initial commitmade changes for disabled feature
Initial commitoptions add
Initial commitprod jwt code
Initial commitprod redis cred added
Initial commitredis TLS
Initial commitremoved ip whitelist & changed DB to cardclientstage
Initial commitresponse_code_changed to -1
Initial commitupdated code
LocalCred
Merge branch 'test' into 'main'
Merge branch 'unifiedgateway_prod' of https://gitlab.com/sovitacharya/extauth-istio into unifiedgateway_prod
Merge branch 'unifiedgateway_stage' of https://gitlab.com/sovitacharya/extauth-istio into unifiedgateway_stage
REDiS SM Key
Redis SM
Redis SM Key
Refactor MongoDB replica set string formatting in Envvariables function
Refactor Redis and MongoDB certificate file handling in createRedisPool and Envvariables functions
Refactor Redis and MongoDB credential structures and initialization to get secret from env
Refactor Redis connection initialization and error handling in createRedisPool and GetMongoClient functions
SM Redis
SM key
See merge request sovitacharya/extauth-istio!1
Test
Update Redis secret name environment variable to 'SecretNameRedis'
add 3rd key
add apiusername feature
add comments
add differnetiation for apiuser and wl
add file create and get
add ippb db details and remove ip checks
add mongo secret manager
add new mongo creds and change in secret manager
add redis
add singularity modification for client id and ip for whitelisting
add stage db
add unknown
add whitelistig concept for prod
added apiusername key to response header
added auth token validation
added both jwt and clientsecret authentication
added jwt token part from oauth app
added logs
added logs and uncommented allow cors headers
added logs of client_id client_secret apiusername and key
api user go stage final without redis
apiuser code
apiusername resolved for redis
card-stage
changed caCert type used file by name
changed db name
changed error symbol in logs due to log.printf to fmt.printf
changed log.printf to fmt.printf
changed public key
changed redis insert part
changes
changes done for pass_key and handled error for new sdk-requirement
changes for isu-switch-staging
changes in decryption
changes in ippb encr decr with encrypted and epoch handle
checkip is commented
config commented
config for tls connection in mongodb is hardcoded
config.env modification
connection Pool exhausted issue resolved
corrected return type in grpc
database host change
db changed
db chng
db crentials changed
db url changed
disabled and checkclient merged
env file implemented
epoch time validation added
error handled
error handled for apiusername
ext-authcode
final Referemce Code v1
final apiuser auth application
final changes
final jwt code
final prod code
final rate limit stage
final-prod-auth
formatting done
handled if block when null headersecretes is there its getting passed inside the if block which panics the server
handled the redis connection error to solve the nil pointer issue
header commented to stop 431 error
image update
in tokenproperties role is updated from string to []string
in tokenproperties role is updated to []string ,initially it was string
ippb-auth-gateway-stage
key implementedc in header
key is added in header
log changed to fmt as error is shown in logs
logging done
logging for redis and mongo updated
logging updated
logs changes
logs handled
made changes for disabled feature
mod file name change
new mongo ip
new workflow for sdk-auth-staging
optimised code
options add
pkg add redis rate limit
prod apiuser auth app
prod final
prod redis cred added
prod redis creds used
prod redis used and config is set
prod-jwt application
push latest code
rate limit implementation along with client combination redis implementation
redeclared function commented out
redis TLS
redis added
redis and mongo logging updaetd
redis connection config change
redis prod cred used
removed config.env
resolve test 431
response key commented out
response_code_changed to -1
secret db access
secret manager
secret manager implemented
sm redis  tls
solved issue in insert
solved redis connection issue and  handled some logs
solved token issues
stage code with ip block
staging created for unifiedgateway credentials updated for stage
tls config
to handle apiuser clients
tokenHeaderjwt added
tsl connection to mongodb
uat-auth
uncommented checkip part
unified gateway code
update ip blocklist with redis cache
updated code
updated ippb gateway auth
updated the error codes and messages accordingly in sdk-stage gateway.

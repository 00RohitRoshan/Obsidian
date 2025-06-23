# Commit History for 'mqtt_server_soundbox'

## Branch: origin/ag_stage

added auth and tls part

added api call for publish and call_back

 added api call part for onconnect and disconnect

added log part for onconnect and disconnect

## Branch: origin/bob_prod

made changes for prod bob

changed username , psswrd for uat bob

changed certs to add uat domain

changed certs for bob_uat

made changes in http

added code for bob

cabank prod code

changed uname and password

production code

Initial commit
## Branch: origin/bob_uat

changed username , psswrd for uat bob

changed certs to add uat domain

changed certs for bob_uat

made changes in http

added code for bob

cabank prod code

changed uname and password

production code

Initial commit
## Branch: origin/bobbank

made changes in http

added code for bob

cabank prod code

changed uname and password

production code

Initial commit
## Branch: origin/cabank

cabank prod code

changed uname and password

production code

Initial commit
## Branch: origin/cabank_nossl

no ssl code added

cabank prod code

changed uname and password

production code

Initial commit
## Branch: origin/can_stage

playstatus 1 client

rm go routine in onpacketread

Revert "added worker pool"

tttt reverts commit 82fd5667c5419ac5b3efea31bd2d7d46f14866e0.

changed type for update api

added worker pool

optimise api call

added sleep

added time stamp for asia location

error handling txn insert

insert transaction api call

initial commit

Update server version

Move cl.WriteLoop() to attachClient() and call cl.Stop() in loadClients() to update client.State. (#344)

* Moving go cl.WriteLoop() out of NewClient() and placing it in server.attachClient().

* Call cl.Stop() to cancel the context, update cl.State with information such as disconnected time, and set the stopCause.

* update README-CN.md

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
feat: return tcp.Address from listener, if exists (#336)

* This is the more accurate and correct address of the listener
* Useful if you want to listen on port 0 to dynamically create
listeners (think of unit/integration tests)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Packet encoding optimization (#343)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

* Reduce double write of pk.Payload

* Use memory pool for packet encode

* Pool doesn't guarantee value between Put and Get

* Add benchmark for bufpool

* Fix issue #346

* Change default pool not to have size cap

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix data race issue with write buffer (#347)


Handle expired clients in server.loadClients(). (#341)

* Handle expired clients in server.loadClients().

* No need to call s.Clients.Delete().

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Dynamically allocate write buffer if needed. (ready for merge) (#324)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add a Japanese version of README.md (#338)

* Add a Japanese version of README.md

* add jp link
Add a demonstration in examples/hooks on how to subscribe to a topic and publish messages directly within the hook. (#333)


Revert "improve transport performance with bufio (#321)" (#323)

This reverts commit 8e52e49b94026c3380b8c2cacce22fc565858cc7.
improve transport performance with bufio (#321)

* improve transport performance with bufio

* fix issue of unit test

* fix issue

* optimize code
Fix for unlimited maximum message expiry interval (#315)

* fix when no max msg expiry interval is set

* fix expiry handling of clearExpiredInflights

* Modify it to handle cases where the MaximumMessageExpiryInterval is set to 0 or math.MaxInt64 for no expiry, and optimize some of the code and test cases.

* Set MaximumMessageExpiryInterval to 0 or math.MaxInt64 for no expiration, and optimize some of the code and test cases.

* Addressing the issue of numeric overflow with expiration values.

* Only when server.Options.Capabilities.MaximumMessageExpiryInterval is set to math.MaxInt64 for no expiry.

* fix typo in README.md

* There is no need to verify whether 'maximumExpiry' is 'math.MaxInt64' within 'client.ClearInflight()

* Optimize the code to make it easier to understand.

* Differentiate the handling of 'expire' in MQTTv5 and MQTTv3; skip expiration checks if MaximumMessageExpiryInterval is set to 0; optimize code and test cases.

* When MaximumMessageExpiryInterval is set to 0, it should not affect the message's own expiration(for v5) evaluation.

* Adding client.ClearExpiredInflights() to clear expired messages, while client.ClearInflights() is used to clear all inflight messages.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werben <werben@aliyun.com>
Co-authored-by: werben <werben@qq.com>
Remove vendor folder (#319)

* Remove vendor folder

* Add vendor to gitignore

---------

Co-authored-by: mochi-co <moumochi@icloud.com>
Bump golang.org/x/net from 0.7.0 to 0.17.0 (#316)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.7.0 to 0.17.0.
- [Commits](https://github.com/golang/net/compare/v0.7.0...v0.17.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
update README-CN.md (#312)


Update README.md
Indicate translators wanted
Emit warning if client keepalive is less than recommended minimum (#305)

Co-authored-by: mochi-co <moumochi@icloud.com>
Add a Chinese version of README.md. (#307)

* Add a Chinese version of the README.md.

* rename README_CN.md to README-CN.md

* Optimize some aspects

* Correct some translation errors.

* Optimize some aspects.

* Initial completion of all translations.

* Optimize some aspects.

* Optimize some aspects.

* Refinement of translations.
only build docker on tag for mochi-mqtt repo

Add some error logging in Listener.Serve(). (#303)

* Add some error logging in Listener.Serve().

* Remove error logging for TCP listener Accept() calls.

* Optimize code.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update build.yml
Update build.yml

multiple platforms
Update build.yml
Update build.yml
Update build.yml

alternative tags attempt
Update build.yml
Fix docker repo name
Update build.yml

test push to docker with version
Update build.yml

test pushing directly to docker
Update build.yml
Refactor Listener WG to track clients (#301)


Update readme v2.4.0

Small fixes and cleanups (#295)

* fix typos, indicate unused returns

* Add test for publishToClient acl unauthorized

* Add Inline Client as a server option
Disconnect or return ack if unauthorized publish (#292)

* Ensure msg doesn't exceed subscription QoS

* Disconnect or return ack if unauthorized publish

* Disconnect or return ack if unauthorized publish

* Create new server for eery test case

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Another code implementation for Inline Client Subscriptions. (#284)

* Another code implementation for Inline Client Subscriptions.

* Added a few test cases.

* Changed the return value types of Server.Unsubscribe() and Subscribe() to boolean.

* Implementing the delivery of retained messages and supporting multiple callbacks per topic using different inline client IDs.

* Added validation checks for the legality of the inline client id during Subscribe and Unsubscribe.

* Added validation checks for the legality of the client during Subscribe and Unsubscribe.

* Fixed the TestServerSubscribe/invalid_client_id test case failure.

* Add Server.inlineClient and Temporarily removing test cases for better code review readability.

* Using server.inlineClient in server.InjectPacket().

* After unsubscribing, if there are other subscriptions in particle.inlineSubscriptions, particle cannot be deleted.

* Add comments to particle.inlineSubscriptions and modify to return ErrTopicFilterInvalid when the topic is invalid during subscription.

* Fixed some test case failures caused by adding inlineClient to the server.

* More test cases have been added.

* Optimization of test case code.

* Modify server.go: When used as a publisher, treat the qos of inline client-published messages as 0.

* Resolve conflict.
Migrate from zerolog to slog (#248)

* Begin adding new slog calls

* Fixed unit tests

* Add leveler example

* Add debug log level to Redis example

* Change location of server.Close() and add logs to example/hooks

* Begin removing references to zerolog

* Removed final references to zerolog

* Change where server.Close() occurs in main

* Change to 1.21 to remove x dependency

* Add slog

* Update references to 1.21

* Begin change of LogAttrs to standard logging interface

* Change the rest of LogAttrs to default

* Fix bad log

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update server.go

Not checking if err is equal to nil

* Update server.go

printing information for ID or error is missing.

* Change references of err.Error() to err in slog

* Remove missed removal of Error() references for logging

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werbenhu <werben@qq.com>
add aclcheck in publishToClient (#287)

Co-authored-by: unknow <beunknow@outlook.com>
Fix readme example (#276)

* Update README example to better match other examples

* Fix formatting

* Fix err formatting issue

* Fix bad import in README example

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Use JSONeq to compare JSON (#267)

* WriterSize parameter is incorrectly set

The WriterSize parameter is incorrectly set in the newClient method.

* Use JSONeq to compare JSON

This ensures that test results pass even if the field order is inconsistent.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update README.md
Fix badges
Update README.md
Update README.md
migrate imports, copyrights, etc (#270)


Update server version

Allow Publish to return custom Ack error responses (#256)

* Allow publish error returns as acks

* Add Ignore Packet, tests
fix: fix data-race in badger hook (#266)

Co-authored-by: Gabriel Sagula <gsagula@magicleap.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
method UnsubscribeClient's packet add fixedHeader (#264)


Do not retain messages if retain is not available (#261)

* Do not retain messages if retain is not available

* Add Test
Preference Write, Read, Deny filters in ledger (#262)


Retain flag should be delivered as false in v3 (#257)

* retain should be delivered as false in v3

* Forward retained flag if publish is from subscribe action
Fix websocket reads for packets > 1 buffer size (#260)


Update README.md
Ensure msg doesn't exceed subscription QoS (#253)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
WriterSize parameter is incorrectly set (#252)

The WriterSize parameter is incorrectly set in the newClient method.
Small language clarification for non-english

Update server version

Add OnSessionEstablish hook (#247)

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update Readme

Add Healthcheck listener

Update README.md
Update SPDX annotations

Update Contribution Guidelines

Update server version

Add healthcheck listener (#244)

* Add healthcheck listener

* Update improper comments

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix ScanSubscribersTopicInheritanceBug (#243)

* Sub a/b should not receive msg for a/b/c...

* Add TestScanSubscribersTopicInheritanceBug test

* Ensure sharedSubscription are gathered

* Fix Unsubscribe for sharedSub and optimization

* Unsub with lower case in TestUnsubscribeShared

* Add test with # for TestScanSubscribersShared
Update Hooks List

Update Server Version

Expose SendConnack, err return on OnConnect (#240)


Add OnRetainPublished hook (#237)

* Add OnRetainPublished hook

* Skip OnRetainPublished if publish error
Update server version

Add retainMessage to LWT to properly handle message retention (#234)

* Add retainMessage to LWT to properly handle message retention if specified in connect

* Add will retain flag on missed test

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update server version

Now when a "publish" command fails, then the publish method will throw an error (#229)

Errors in the hook when doing a publish were ignored. This caused that test cases could not be made where the publish failed and an error was thrown.

Co-authored-by: hector.oliveros@wabtec.com <hectoroliveros@MacBook-Pro-de-Hector.local>
Minimize client lock duration (#223)

* Minimize client lock duration
* Fix server option example

Fix example usage of NewHTTPStats (#231)

Co-authored-by: Dominic Plourde <plourded@amotus.ca>
Update README.md new benchmarks
update server version

Use context to exit WriteLoop (#222)

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Fix misspelling
update server version

refactor server keepalive for hook access (#220)


Use context to signal client open state (#218)


Add packet ID exhausted hook (#217)


Expire session if SessionExpiryInterval is 0 (#216)

If SessionExpiryInterval was not set in CONNECT, SessionExpiryIntervalFlag is also not set. According to spec:
  If the Session Expiry Interval is absent the value 0 is used. If it is set to 0, or is absent, the Session ends when the Network Connection is closed.
Update codes.go (#215)

fix typo
Update codes.go (#214)

Fix typo
Update server version

Lock on close outbound (#213)


Add lock to client writes (#212)


Add OnPacketIDExhausted hook (#211)


Correctly validate WillProperties (#210)

Co-authored-by: sukvojte <sukvojte@gmail.com>
Update build.yml (#203)


Protect close of nil outbound channel

Protect close of nil outbound channel

#78 storage hook should not execute the relevant code if the client has been reconnected (#198)

* storage hook should not execute the relevant code if the client has been reconnected #78

* add test cases for coverage decrease

add test cases for coverage decrease
Move msgToPacket to storage.Message.ToPacket

Simplified code (#195)

Simplify the code for the loadInflight and loadRetained methods.
Adjust the validation order of the processSubscribe method to ensure that it fails quickly if there is an error, since s.hooks. OnACLCheck generally takes a long time.

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Ensure to close client WriteLoop (#193)

* Ensure client WriteLoop is closed

* Ensure to close client WriteLoop
fix: common subscriptions issued by different clients at the same time may be lost (#186)


Update readme

Update server version

Configurable client bufio reader/writer sizes (#190)


Update server version

Bump golang.org/x/net from 0.0.0-20220927171203-f486391704dc to 0.7.0 (#182)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.0.0-20220927171203-f486391704dc to 0.7.0.
- [Release notes](https://github.com/golang/net/releases)
- [Commits](https://github.com/golang/net/commits/v0.7.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Skip expire cleanup for isTakenOver session (#183)

* Skip expire cleanup for isTakenOver session

* Set prev connection to isTakenOver on CleanSession

#173.
Allow 0 byte usernames if correctly formed (#181)

* Allow 0 byte usernames if correctly formed

* Allow 0 byte usernames if correctly formed
Correctly identify and clean taken-over sessions (#180)


Small style fix

Update server version

Use *packets.Packet for outbound chan (#176)

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan
update server version

fix: correct decoding of packets including Properties exceeding 127 bytes in length (#172)


Update server version

Expose dropped publish messages count in sys info (#170)


Fix potential NextPacketID endless loop, expand tests (#169)

* Fix possible NextPacketID endless loop, expand tests

* Optimize NextPacketID

* Use math constants
Add PublishDropped metrics (#167)

* Add PublishDropped

* Add PublishDropped

* Add PublishDropped

* Update storage_test.go

* Update system.go

* Update server.go
No longer issue retained messages on session takeover (#166)


Client write buffers (#165)

* Replace fanpool with client write buffers
Add Clone to system.Info (#163)

* Add Clone using atomic operations

* Add Clone using atomic operations

* Use sysinfo.Clone

* Unit test for Clone

* Add Clone using atomic operations

* Update

* Update
Update server version

failed to delete inflight data (#162)

The s.hooks.OnQosPublish method needs to be called, otherwise the following s.hooks.OnQosComplete or processPuback(s.hooks.OnQosComplete) method will report a data not found error.
Update server version

Rename Quota methods for clarity (#159)


Move refreshDeadline to only trigger on successful transmission (#157)


Include a listener accepting an existing net.Listener (#155)


invalid config type provided (#152)

* invalid config type provided

examples/persistence/bolt/main.go: invalid config type provided

* fixed ErrReceiveMaximum(receive maximum exceeded)

No quotas of the inflight is set in the readStore method, so each quota is equal to 0. The inheritClientSession method overrides the quotas of the new client inflight, so the processPublish method reports an ErrReceiveMaximum and disconnects the client.

* reset receive quota

receive quota should be reset across connections (as specified in the spec).
Update server version

Publish retained messages only after connack (#147)


Use Atomic instead of RWMutex for Hooks concurrency (#148)

* Use Atomic instead of RWMutex for Hooks concurrency
* Lock Hooks on Add Hook
Ignore retain as published v3 (#142)

* Optimise Capabilities struct alignment

* Only use RetainAsPublished for v5 clients
Update version number

Use correct connack return codes for MQTTv3 (#140)


Update server version

Fix example imports

export client.Net.Conn for external use

Small code improvements

Make hooks safe for concurrency (#139)

Co-authored-by: thedevop <60499013+thedevop@users.noreply.github.com>

Update server version

Change inline check order (#133)


fix grammar on Closed method doc

Update version number

Refactor stored subscription value assignments

Fix Typos

Save subscription properties for mqttv5 (#131)

* Update redis.go

Save the subscription properties for mqqtv5

* Update badger.go

Save the subscription properties for mqqtv5

* Update bolt.go

Save the subscription properties for mqqtv5

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add Client Closed (#130)

* Add Client Closed
* Add Client Closed
* Update clients_test.go
Update README.md
Update README.md
Update readme and server version

Connect ReturnResponseInfo only applies to Connack values (#128)


Optimize inflight expiry (#127)

* Small formatting/style changes for filter existed

* Use OnQoSDropped hook instead of onInflightExpired
Merge pull request #123 from wind-c/master

Variable existed in the method processSubscribe is unstable
Merge branch 'master' into master
Merge pull request #124 from zgwit/master

Add unix socket listener
Add unix socket listener

Variable existed in the method processSubscribe is unstable

The variable existed can be changed repeatedly within a for loop. An array variable must be used to record the subscription of each filter.
Merge branch 'mochi-co:master' into master

Update server version
Add the OnUnsubscribed hook to the unsubscribeClient method (#122)

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.
Add the OnUnsubscribed hook to the unsubscribeClient method

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.

Update version number
Enforce server max packet (#121)

* Enforce Server Maximum Packet Size on client read
* Fix tests
Merge pull request #116 from tommyminds/bugfix/ws_malformed_package

Fix websocket malformed packet bug
Merge branch 'master' into bugfix/ws_malformed_package
Merge pull request #119 from mochi-co/fix-on-published

Fix mis-typed onpublished hook, update version, fanpool defaults
Fix mis-typed onpublished hook, update version, fanpool defaults

Fix websocket malformed packet bug

Update README.md
Simplify Client construction, add NewClient method to Server, add Publish convenience method

Add newline for godoc formatting

Update badges to use v2 references
Cleanup godoc formatting

Update README.md
Update go mod and imports to v2

Update go.mod
Update go.mod
Update README.md
Update README.md
Update README.md
Update README.md
Update build.yml
update github workflow go version to 1.19

Rewrite everything from scratch for mqtt v5

Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Contributions paused pending v2.0.0
Update README.md
Revert "Merge pull request #97 from alexsporn/fix/writer-full"

This reverts commit f22b8276e8c33c1e34f941beb5d59667bbda9de6, reversing
changes made to b2fc287a9885a94d14f394d84216d123220ab9d5.

Merge pull request #97 from alexsporn/fix/writer-full

Instead of waiting for the writing buffer to have enough space, skip writing and return an error
Merge branch 'mochi-co:master' into fix/writer-full

Merge pull request #99 from mochi-co/fix-inflight-race

Fix concurrent map access for clients and inflights causes data race 
Return copies of client and inflight maps to avoid missed locks

Increase inlinepub messages buffer

Instead of waiting for the writing buffer to have enough space, skip writing and return an error

Check against the correct clean session var for abandoning old inflights

Keep in sync server.System.Inflight (#92)

* Keep in sync server.System.Inflight

* Fix args order in tests
Update README.md
Update README.md
Abandon inflights at the end of clean-session connections

Merge pull request #90 from mochi-co/resend-inflights

Adds Inflight TTL and Period Resend
Adds Inflight TTL and Period Resend

Merge pull request #84 from mochi-co/goreport-fixes

Goreport fixes
remove ineffective assignments

apply gofmt -s

Merge pull request #83 from mochi-co/tls-client-auth

Expose tls.Config to Listeners
Merge pull request #82 from mochi-co/expose-event-client-username

Add CleanSession and Username to events.Client struct
use TLSConfig instead of deprecated TLS field

Add TLSConfig field to allow direct tls.Config setting

update TLS example to use TLSConfig field

Add CleanSession and Username to events.Client struct

Add OnSubscribe, OnUnsubscribe events examples

Extend onsusbcribe, onunsubscribe events

Merge pull request #74 from muXxer/feat/topic-subscription-events


Add topic un-/subscribe events

Merge pull request #72 from BoskyWSMFN/master

fix-panic
fix-panic

fixed runtime panic in server/internal/circ/pool.go occurring on 32-bits architectures caused by misalignment of BytesPool struct members.

https://github.com/golang/go/issues/36606#issue-551005857

fix comments

Add auth controller example

Add Docker info
Merge pull request #69 from mochi-co/v1.2.0

V1.2.0
use NewServer instead of New

update readme for new events

Merge pull request #68 from mochi-co/fix-store-retained

Fix Store Retained Messages
Merge branch 'v1.2.0' of https://github.com/mochi-co/mqtt into fix-store-retained

Merge pull request #67 from mochi-co/release-client-buffers

Release client buffers
only check final outcome due to races

accept any error for invalid protocol due to races

Check for protocol violation errors

Add comments

Remove unused code

Abandon client state if the existing client specified a cleansession

Expose CleanSession value for checking

Store retained message based on corrected r value

Expect correct r values for RetainMessage

Correctly return R value of retainMessage

Update EstablishConnection tests to ensure buffers and pool are correctly released after use

Export R/W buffer values so they can be assessed in tests without causing races

Track number of pool blocks in use

Use package errors instead of strings

test clarbuffers

clear buffers after deferred stop

refactor clients for buffer releasing

Refactor establishconnection to prevent same-id disconnects

refactor connSetup for clarity

Clarify error messages

clarify error checking

Use defer to release buffers and decrease stats on any client closure

Merge pull request #61 from mochi-co/server-options

Configurable Server Options
Merge pull request #63 from mochi-co/add-drop-packet-error

Add ErrRejectPacket to OnProcessMessage
Merge pull request #62 from mochi-co/fix-inflight-key

Fix Inflight Persistence Key
track logged error

Update test to check for packet rejection

Ensure OnError is set before using it

Update OnProcessMessage documentation

Optionally drop a packet if the ErrRejectPacket error is returned from OnProcessMessage

Add ErrRejectPacket error to abandon packet processing from OnMessageProcess

Merge pull request #53 from stffabi/feature/onprocessmessage-event

Events: Add OnProcessMessage event
fix inflight key reference

Fix code block formatting

Update readme with server options

Add example implementation

add tests for new NewServer function

remove deprecated log message

Update code to use new NewServer function instead of deprecated New

Update example code to use new NewServer function instead of deprecated New

Use internal default values instead of relying on passed value

Add Server Options

Adds a new struct of server options which can be used to override default properties. A new options-accepting NewServer function has been created to supersede the New method, which is now deprecated.

Update go mod to ensure bolt is using 1.3.5

Bolt 1.3.6 fails to build correctly and has been removed, so rollback to bolt 1.3.5. Also upgrade to Go 1.18

Merge pull request #57 from hybridgroup/v1.2.0-docker

docker: add initial simple Dockerfile
Merge pull request #58 from soyoo/patch-1

typo
typo
docker: add initial simple Dockerfile

Merge pull request #51 from jmacd/jmacd/noracefix

Two no-functional-change cleanups combined
Events: Add OnProcessMessage event

This event gets called right after ACL checking but before any other
Fields of the packet get evaluated.

Combines two fixes

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

Update README.md
Update README.md
Merge pull request #46 from stffabi/bugfix/acls-retain

Subscribe: Only send retained messages if ACLs has allowed subscription to the topic
Subscribe: Only send retained messages if ACLs has allowed subscription to the topic

Fix incorrect test

The previous publish inline test incorrectly approved retain packets without retain=true fixedheader values.

Publish: Set the retain flag in the fixedheader (#42)

* Publish: Set the retain flag in the fixedheader

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

# Conflicts:
#	server/internal/clients/clients.go

Update README.md
Update README.md
Replace Travis with Github Actions (#41)

* Remove Travis CI

* Add Github Actions Workflow

* Update badges for build status, coverage, report card, doc reference

* use actions for all pull requests and pushes

* test all files for coverage

* Apply gofmt -s to simplify code

* Fix typos

* Cleanup comments

* Cleanup comments

Co-authored-by: mochi <mochimou@icloud.com>
Fix typo

Add Keyed fields to events.Client for readability and go vet

Add missing method comments

Add an OnError handler; report the reason for disconnects. (#38)


Wrap packet errors with cause information (#39)


Move two WaitGroup.Add calls (#36)


Merge pull request #29 from jmacd/jmacd/payload_not_utf8

Support non-UTF8 payloads (per MQTT specification)
Support non-UTF8 payloads per MQTT specification

revert redis update
revert server version
Merge pull request #27 from mochi-co/revert-26-master

Revert "added redis persistence mode"
Revert "added redis persistence mode"

Update server version
Update README.md
Merge pull request #26 from wind-c/master

added redis persistence mode
redis and trie

add redis persistence mode and example

update server version

Merge pull request #24 from mochi-co/feature/optimise-struct-fields

Optimise Struct Fields + Fixes
optimise Server struct

pass byte pool by address

remove println

Pass inflight by address to avoid lock copying

Correct function signature

Update test to match new FixedHeader struct

Prevent locks from being copied

8bit align struct fields

Update comment for clarity

Update version to 1.1.0

indicate ARM32 compatibility

Merge pull request #22 from mochi-co/feature/32bit-compatibility

ARM32 Compatibility
Merge pull request #19 from rkennedy/bugfix/32-bit-atomic-alignment

Improve 32-bit compatibility
Fix encodeLength for 32-bit platforms

When `int` is 32 bits, `MaxInt64` doesn't fit. It's apparent that
`encodeLength` expects to handle 64-bit inputs, so let's make that
explicit, which allows the test to run on all platforms.

Avoid race condition when closing listeners

"Atomic load" followed by "atomic store" is not itself an atomic
operation. This commit replaces that sequence with CompareAndSwap
instead.

Make atomics work on 32-bit systems

On 32-bit systems, `atomic` requires its 64-bit arguments to have 64-bit
alignment, but the compiler doesn't help ensure that's the case. In this
commit, fields that don't need to hold large numbers have been converted
to 32-bit types, which are always aligned correctly on all platforms.
For fields that may hold large numeric values, padding has been added to
get the necessary alignment, and tests have been added to avoid
regressions.

Update server version to 1.0.5

Merge pull request #18 from mochi-co/feature/connect-disconnect-hooks

OnConnect and OnDisconnect Event Hooks
Update for OnConnect and OnDisconnect hooks

Add tests for OnConnect, OnDisconnect

Add OnConnect and OnDisconnect hooks to example

Call OnDisconnect Event if applicable

Add OnDisconnect Event Hook

Add testbolt file to ignore list

Call OnConnect Event if applicable

Add OnConnect event hook

Prevent locks being copied by passing non-pointer to FromClient

Merge pull request #15 from ClarkQAQ/master

Fixed some bugs, wish the project better and better
update tcp.go maybe this will be better

fix local variable black hole

update mock.go plase use range

fix [ST1005] strings should not be capitalized

update websocket.go fix check origin

Update README.md
Merge pull request #14 from mochi-co/feature/allow-clients-value

Add AllowClients Field to packets
Add example for AllowClients field

Add test for AllowClients field

Remove unnecessary type declarations

Add setupServerClients to inherit existing server instance

previously new clients generated a new server object, so system stats were not shared. This change ensures all test clients use the same server

Add AllowClients check in publishToSubscribers

If AllowClients has been set on a packet, ensure only clients in the slice are sent the message

use .systemInfo instead of .system for clarity

use .systemInfo instead of .system for clarity

Add AllowClients field to packets

AllowClients field can be specified during onMessage event to selectively deliver messages

Increment server version

Add tests for InSliceString

Add InSliceString function

Check if a slice of strings contains a string (until slices package available)

Revert server version

increment server version

Remove unnecessary fmt import

Increment server version

Merge pull request #12 from jphastings/remove-erroneous-print


Remove unnecessary println

fix indentation in code blocks

convert tabs to spaces
Update README.md
Update vendor

Update go mod to 1.17

fix code indents

Update go to 1.17

Increment server version to 1.0.1

Merge pull request #11 from mochi-co/feature/event-hooks-publish

Feature/event hooks publish
fix onmessage test

change scheduled message for clarity

remove redundant code

Update Readme to add Event Hooks section

Merge OnMessage and OnMessageModify

Update events example with publish hooks

Adds tests for publishing event hooks

Add Event Hooks

Adds basic event hooks (OnMessage, OnMessageModify) to the server using the new events library.

Add Events

Events library contains event hook types and related utility functions

Return packets to internal

Now that we can alias types, there's no compelling reason to expose the packets library

Merge pull request #10 from mochi-co/expose-packets

Expose packets library
Merge pull request #8 from mochi-co/feature/inline-publish

Inline Publishing
update packets library import reference

expose packets library

Add .DS_Store to ignore list

Update with direct publishing

Adds information about direct publishing and moves performance section

Add inline publishing example

Adds an example file which demonstrates the usage of the `Publish` method. This file will also be used to demonstrate event hooks.

Add tests for new inline publishing method

Directly publish messages from embedding system

When the broker is embedded in a larger Go codebase, it is beneficial to be able to publish messages directly from the system to topics. This change provides a Publish method which adds messages to an inline publishing queue in a separate goroutine, which are then processed in the standard way and issued to all clients with matching topic filters.

Update comments and rename input parameter for clarity

Update comments for clarity

Add  .gitignore

Ensure we're not committing any binaries

Remove Codacy badge
Update Readme


Update Readme


Update Chart Labels


Update Readme


Update Badges


Update Badges


Fix test races


Update travis


Fix examples


Add TravisCI


Add badges


Update Readme


Update Readme


Resort Charts


Resort Charts


Charts


Image test


Image test


Update README


Update README, better command main


Code and Comments cleanup, vendor deps


Persistence V1


Adds delete from persistence


Adds more persistence tests


Load persistence into server


Persistence and tests


Inflght and retained messages persistence


Progress on persistence


Adds TLS/SSL


Websocket Listener


Don't receive $SYS retained on #


Publish $SYS Stats to topics


Basic $SYS stats


Merge branch 'restructure-paths'
Http Sys Stats listener


Restructures code


Fix tests


Pass Paho Tests


Dont inflight secondary qos flow messages


Satisfy Keepalive, fix Keepalive 0


Small fix


Satisfy 4.7.2 - restrict $ topics


Periodic Resend of Inflight messages


Cleanup TCP Listener


Merge remote-tracking branch 'origin/master'


Merge pull request #1 from mochi-co/iobuffers

Iobuffers
Merge branch 'iobuffers'
Fix close sequence, update test coverage


LWT and Validate packet


bytes buffer to pool


refactor pointers


Publish


Process packets


Establish Tests


start establish 


client write packet


update tests


Rebuilding


New Packets


Fix CheckEmpty


Rebuild


Rebuild


Rebuild


Rebuild


Rebuild


working but bottlenecks


pre-refactor


More tests, connecting MQTT


More Tests


Fixes sync.cond deadlock


Debug func, better closers


Tests and buffer sizes


Write Bytes


Processor Read and Tests


Refactor, fixes to Circ Peek, start processor/parser


WriteTo / Tests


Read+Read Test


cleanup


AwaitFilled


Cleanup, start reader/writer model


Small fixes


WriteTo / Tests


Start on Peek


ReadFrom IO


AwaitCapacity tests


Working wait logic


Move Parser, cleanup to basic


Cleanup


All working


Adds Retained Delete


Cleanup, Tests fix, Client closers


Fix packet buffer mutation


midway various pointer bytes fixes


server cmd


Cleanup


Fix unsafe.pointer, unsub cascade bugs


Testing example


Cleanup


Fix Error nil/contains checks


Send LWT+tests


Resend unsent inFlight


Performance changes


Cleanup tests and benchmarks


Handle CleanSession


Pub/sub ACL and acks


Write Client coverage


Client Tests


Tests Cleanup


Refactor Tests


Subscribe Retain


Subscribe basic + Unsubscribe


Pubcomp


Pubrel + Pubrec


Fix Establish tests


Fix Establish test


Process Publish+Recv


Switch out bufio pools


Start processing Publish


Zero-alloc retain messages + fixes


Zero-alloc topics


Alloc free subscribers


Topics interface


Deprecate particle bucket subscribers


Trie subscribers tree


Start processing packets


Update more tests


Update more tests


Refactor Clients into Server


Refactor packets/parser to take bufio rw


Add bufio rw pools


Refactor Client read to Server


Refactor fixedheader


Auth Controllers and listener options


Client Tests


Refactor MockNetConn


Add auth controller interface


Refactor Listener into Listen()


Decode a Connect packet on connection


Divest Validation from Parser


Cleanup Packets tests


Adds Mock net.Conn, errors for establisher


Refactor listeners for performance


Reworking listeners


Error strings to errors


Remove limiter


Add Benchmarks and tests


Add README


Cleanup


alloc free encoding


Convert all packet processes to byte.buffers


Benchmarks


Cleanup


New Packets library and new benchmarks


Initial commit
## Branch: origin/jkbank

changed ssl certs

changed uname and password

production code

Initial commit
## Branch: origin/main

Initial commit
## Branch: origin/nossl_prod

latest code for csc

initial commit

initial commit

changed ssl certs

changed uname and password

production code

Initial commit
## Branch: origin/nossl_stage

initial commit

changed ssl certs

changed uname and password

production code

Initial commit
## Branch: origin/packetchange

changed certs

updated_time

_ time

packet change

rm go routine in onpacketread

Revert "added worker pool"

tttt reverts commit 82fd5667c5419ac5b3efea31bd2d7d46f14866e0.

changed type for update api

added worker pool

optimise api call

added sleep

added time stamp for asia location

error handling txn insert

insert transaction api call

initial commit

Update server version

Move cl.WriteLoop() to attachClient() and call cl.Stop() in loadClients() to update client.State. (#344)

* Moving go cl.WriteLoop() out of NewClient() and placing it in server.attachClient().

* Call cl.Stop() to cancel the context, update cl.State with information such as disconnected time, and set the stopCause.

* update README-CN.md

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
feat: return tcp.Address from listener, if exists (#336)

* This is the more accurate and correct address of the listener
* Useful if you want to listen on port 0 to dynamically create
listeners (think of unit/integration tests)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Packet encoding optimization (#343)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

* Reduce double write of pk.Payload

* Use memory pool for packet encode

* Pool doesn't guarantee value between Put and Get

* Add benchmark for bufpool

* Fix issue #346

* Change default pool not to have size cap

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix data race issue with write buffer (#347)


Handle expired clients in server.loadClients(). (#341)

* Handle expired clients in server.loadClients().

* No need to call s.Clients.Delete().

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Dynamically allocate write buffer if needed. (ready for merge) (#324)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add a Japanese version of README.md (#338)

* Add a Japanese version of README.md

* add jp link
Add a demonstration in examples/hooks on how to subscribe to a topic and publish messages directly within the hook. (#333)


Revert "improve transport performance with bufio (#321)" (#323)

This reverts commit 8e52e49b94026c3380b8c2cacce22fc565858cc7.
improve transport performance with bufio (#321)

* improve transport performance with bufio

* fix issue of unit test

* fix issue

* optimize code
Fix for unlimited maximum message expiry interval (#315)

* fix when no max msg expiry interval is set

* fix expiry handling of clearExpiredInflights

* Modify it to handle cases where the MaximumMessageExpiryInterval is set to 0 or math.MaxInt64 for no expiry, and optimize some of the code and test cases.

* Set MaximumMessageExpiryInterval to 0 or math.MaxInt64 for no expiration, and optimize some of the code and test cases.

* Addressing the issue of numeric overflow with expiration values.

* Only when server.Options.Capabilities.MaximumMessageExpiryInterval is set to math.MaxInt64 for no expiry.

* fix typo in README.md

* There is no need to verify whether 'maximumExpiry' is 'math.MaxInt64' within 'client.ClearInflight()

* Optimize the code to make it easier to understand.

* Differentiate the handling of 'expire' in MQTTv5 and MQTTv3; skip expiration checks if MaximumMessageExpiryInterval is set to 0; optimize code and test cases.

* When MaximumMessageExpiryInterval is set to 0, it should not affect the message's own expiration(for v5) evaluation.

* Adding client.ClearExpiredInflights() to clear expired messages, while client.ClearInflights() is used to clear all inflight messages.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werben <werben@aliyun.com>
Co-authored-by: werben <werben@qq.com>
Remove vendor folder (#319)

* Remove vendor folder

* Add vendor to gitignore

---------

Co-authored-by: mochi-co <moumochi@icloud.com>
Bump golang.org/x/net from 0.7.0 to 0.17.0 (#316)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.7.0 to 0.17.0.
- [Commits](https://github.com/golang/net/compare/v0.7.0...v0.17.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
update README-CN.md (#312)


Update README.md
Indicate translators wanted
Emit warning if client keepalive is less than recommended minimum (#305)

Co-authored-by: mochi-co <moumochi@icloud.com>
Add a Chinese version of README.md. (#307)

* Add a Chinese version of the README.md.

* rename README_CN.md to README-CN.md

* Optimize some aspects

* Correct some translation errors.

* Optimize some aspects.

* Initial completion of all translations.

* Optimize some aspects.

* Optimize some aspects.

* Refinement of translations.
only build docker on tag for mochi-mqtt repo

Add some error logging in Listener.Serve(). (#303)

* Add some error logging in Listener.Serve().

* Remove error logging for TCP listener Accept() calls.

* Optimize code.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update build.yml
Update build.yml

multiple platforms
Update build.yml
Update build.yml
Update build.yml

alternative tags attempt
Update build.yml
Fix docker repo name
Update build.yml

test push to docker with version
Update build.yml

test pushing directly to docker
Update build.yml
Refactor Listener WG to track clients (#301)


Update readme v2.4.0

Small fixes and cleanups (#295)

* fix typos, indicate unused returns

* Add test for publishToClient acl unauthorized

* Add Inline Client as a server option
Disconnect or return ack if unauthorized publish (#292)

* Ensure msg doesn't exceed subscription QoS

* Disconnect or return ack if unauthorized publish

* Disconnect or return ack if unauthorized publish

* Create new server for eery test case

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Another code implementation for Inline Client Subscriptions. (#284)

* Another code implementation for Inline Client Subscriptions.

* Added a few test cases.

* Changed the return value types of Server.Unsubscribe() and Subscribe() to boolean.

* Implementing the delivery of retained messages and supporting multiple callbacks per topic using different inline client IDs.

* Added validation checks for the legality of the inline client id during Subscribe and Unsubscribe.

* Added validation checks for the legality of the client during Subscribe and Unsubscribe.

* Fixed the TestServerSubscribe/invalid_client_id test case failure.

* Add Server.inlineClient and Temporarily removing test cases for better code review readability.

* Using server.inlineClient in server.InjectPacket().

* After unsubscribing, if there are other subscriptions in particle.inlineSubscriptions, particle cannot be deleted.

* Add comments to particle.inlineSubscriptions and modify to return ErrTopicFilterInvalid when the topic is invalid during subscription.

* Fixed some test case failures caused by adding inlineClient to the server.

* More test cases have been added.

* Optimization of test case code.

* Modify server.go: When used as a publisher, treat the qos of inline client-published messages as 0.

* Resolve conflict.
Migrate from zerolog to slog (#248)

* Begin adding new slog calls

* Fixed unit tests

* Add leveler example

* Add debug log level to Redis example

* Change location of server.Close() and add logs to example/hooks

* Begin removing references to zerolog

* Removed final references to zerolog

* Change where server.Close() occurs in main

* Change to 1.21 to remove x dependency

* Add slog

* Update references to 1.21

* Begin change of LogAttrs to standard logging interface

* Change the rest of LogAttrs to default

* Fix bad log

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update server.go

Not checking if err is equal to nil

* Update server.go

printing information for ID or error is missing.

* Change references of err.Error() to err in slog

* Remove missed removal of Error() references for logging

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werbenhu <werben@qq.com>
add aclcheck in publishToClient (#287)

Co-authored-by: unknow <beunknow@outlook.com>
Fix readme example (#276)

* Update README example to better match other examples

* Fix formatting

* Fix err formatting issue

* Fix bad import in README example

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Use JSONeq to compare JSON (#267)

* WriterSize parameter is incorrectly set

The WriterSize parameter is incorrectly set in the newClient method.

* Use JSONeq to compare JSON

This ensures that test results pass even if the field order is inconsistent.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update README.md
Fix badges
Update README.md
Update README.md
migrate imports, copyrights, etc (#270)


Update server version

Allow Publish to return custom Ack error responses (#256)

* Allow publish error returns as acks

* Add Ignore Packet, tests
fix: fix data-race in badger hook (#266)

Co-authored-by: Gabriel Sagula <gsagula@magicleap.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
method UnsubscribeClient's packet add fixedHeader (#264)


Do not retain messages if retain is not available (#261)

* Do not retain messages if retain is not available

* Add Test
Preference Write, Read, Deny filters in ledger (#262)


Retain flag should be delivered as false in v3 (#257)

* retain should be delivered as false in v3

* Forward retained flag if publish is from subscribe action
Fix websocket reads for packets > 1 buffer size (#260)


Update README.md
Ensure msg doesn't exceed subscription QoS (#253)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
WriterSize parameter is incorrectly set (#252)

The WriterSize parameter is incorrectly set in the newClient method.
Small language clarification for non-english

Update server version

Add OnSessionEstablish hook (#247)

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update Readme

Add Healthcheck listener

Update README.md
Update SPDX annotations

Update Contribution Guidelines

Update server version

Add healthcheck listener (#244)

* Add healthcheck listener

* Update improper comments

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix ScanSubscribersTopicInheritanceBug (#243)

* Sub a/b should not receive msg for a/b/c...

* Add TestScanSubscribersTopicInheritanceBug test

* Ensure sharedSubscription are gathered

* Fix Unsubscribe for sharedSub and optimization

* Unsub with lower case in TestUnsubscribeShared

* Add test with # for TestScanSubscribersShared
Update Hooks List

Update Server Version

Expose SendConnack, err return on OnConnect (#240)


Add OnRetainPublished hook (#237)

* Add OnRetainPublished hook

* Skip OnRetainPublished if publish error
Update server version

Add retainMessage to LWT to properly handle message retention (#234)

* Add retainMessage to LWT to properly handle message retention if specified in connect

* Add will retain flag on missed test

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update server version

Now when a "publish" command fails, then the publish method will throw an error (#229)

Errors in the hook when doing a publish were ignored. This caused that test cases could not be made where the publish failed and an error was thrown.

Co-authored-by: hector.oliveros@wabtec.com <hectoroliveros@MacBook-Pro-de-Hector.local>
Minimize client lock duration (#223)

* Minimize client lock duration
* Fix server option example

Fix example usage of NewHTTPStats (#231)

Co-authored-by: Dominic Plourde <plourded@amotus.ca>
Update README.md new benchmarks
update server version

Use context to exit WriteLoop (#222)

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Fix misspelling
update server version

refactor server keepalive for hook access (#220)


Use context to signal client open state (#218)


Add packet ID exhausted hook (#217)


Expire session if SessionExpiryInterval is 0 (#216)

If SessionExpiryInterval was not set in CONNECT, SessionExpiryIntervalFlag is also not set. According to spec:
  If the Session Expiry Interval is absent the value 0 is used. If it is set to 0, or is absent, the Session ends when the Network Connection is closed.
Update codes.go (#215)

fix typo
Update codes.go (#214)

Fix typo
Update server version

Lock on close outbound (#213)


Add lock to client writes (#212)


Add OnPacketIDExhausted hook (#211)


Correctly validate WillProperties (#210)

Co-authored-by: sukvojte <sukvojte@gmail.com>
Update build.yml (#203)


Protect close of nil outbound channel

Protect close of nil outbound channel

#78 storage hook should not execute the relevant code if the client has been reconnected (#198)

* storage hook should not execute the relevant code if the client has been reconnected #78

* add test cases for coverage decrease

add test cases for coverage decrease
Move msgToPacket to storage.Message.ToPacket

Simplified code (#195)

Simplify the code for the loadInflight and loadRetained methods.
Adjust the validation order of the processSubscribe method to ensure that it fails quickly if there is an error, since s.hooks. OnACLCheck generally takes a long time.

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Ensure to close client WriteLoop (#193)

* Ensure client WriteLoop is closed

* Ensure to close client WriteLoop
fix: common subscriptions issued by different clients at the same time may be lost (#186)


Update readme

Update server version

Configurable client bufio reader/writer sizes (#190)


Update server version

Bump golang.org/x/net from 0.0.0-20220927171203-f486391704dc to 0.7.0 (#182)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.0.0-20220927171203-f486391704dc to 0.7.0.
- [Release notes](https://github.com/golang/net/releases)
- [Commits](https://github.com/golang/net/commits/v0.7.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Skip expire cleanup for isTakenOver session (#183)

* Skip expire cleanup for isTakenOver session

* Set prev connection to isTakenOver on CleanSession

#173.
Allow 0 byte usernames if correctly formed (#181)

* Allow 0 byte usernames if correctly formed

* Allow 0 byte usernames if correctly formed
Correctly identify and clean taken-over sessions (#180)


Small style fix

Update server version

Use *packets.Packet for outbound chan (#176)

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan
update server version

fix: correct decoding of packets including Properties exceeding 127 bytes in length (#172)


Update server version

Expose dropped publish messages count in sys info (#170)


Fix potential NextPacketID endless loop, expand tests (#169)

* Fix possible NextPacketID endless loop, expand tests

* Optimize NextPacketID

* Use math constants
Add PublishDropped metrics (#167)

* Add PublishDropped

* Add PublishDropped

* Add PublishDropped

* Update storage_test.go

* Update system.go

* Update server.go
No longer issue retained messages on session takeover (#166)


Client write buffers (#165)

* Replace fanpool with client write buffers
Add Clone to system.Info (#163)

* Add Clone using atomic operations

* Add Clone using atomic operations

* Use sysinfo.Clone

* Unit test for Clone

* Add Clone using atomic operations

* Update

* Update
Update server version

failed to delete inflight data (#162)

The s.hooks.OnQosPublish method needs to be called, otherwise the following s.hooks.OnQosComplete or processPuback(s.hooks.OnQosComplete) method will report a data not found error.
Update server version

Rename Quota methods for clarity (#159)


Move refreshDeadline to only trigger on successful transmission (#157)


Include a listener accepting an existing net.Listener (#155)


invalid config type provided (#152)

* invalid config type provided

examples/persistence/bolt/main.go: invalid config type provided

* fixed ErrReceiveMaximum(receive maximum exceeded)

No quotas of the inflight is set in the readStore method, so each quota is equal to 0. The inheritClientSession method overrides the quotas of the new client inflight, so the processPublish method reports an ErrReceiveMaximum and disconnects the client.

* reset receive quota

receive quota should be reset across connections (as specified in the spec).
Update server version

Publish retained messages only after connack (#147)


Use Atomic instead of RWMutex for Hooks concurrency (#148)

* Use Atomic instead of RWMutex for Hooks concurrency
* Lock Hooks on Add Hook
Ignore retain as published v3 (#142)

* Optimise Capabilities struct alignment

* Only use RetainAsPublished for v5 clients
Update version number

Use correct connack return codes for MQTTv3 (#140)


Update server version

Fix example imports

export client.Net.Conn for external use

Small code improvements

Make hooks safe for concurrency (#139)

Co-authored-by: thedevop <60499013+thedevop@users.noreply.github.com>

Update server version

Change inline check order (#133)


fix grammar on Closed method doc

Update version number

Refactor stored subscription value assignments

Fix Typos

Save subscription properties for mqttv5 (#131)

* Update redis.go

Save the subscription properties for mqqtv5

* Update badger.go

Save the subscription properties for mqqtv5

* Update bolt.go

Save the subscription properties for mqqtv5

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add Client Closed (#130)

* Add Client Closed
* Add Client Closed
* Update clients_test.go
Update README.md
Update README.md
Update readme and server version

Connect ReturnResponseInfo only applies to Connack values (#128)


Optimize inflight expiry (#127)

* Small formatting/style changes for filter existed

* Use OnQoSDropped hook instead of onInflightExpired
Merge pull request #123 from wind-c/master

Variable existed in the method processSubscribe is unstable
Merge branch 'master' into master
Merge pull request #124 from zgwit/master

Add unix socket listener
Add unix socket listener

Variable existed in the method processSubscribe is unstable

The variable existed can be changed repeatedly within a for loop. An array variable must be used to record the subscription of each filter.
Merge branch 'mochi-co:master' into master

Update server version
Add the OnUnsubscribed hook to the unsubscribeClient method (#122)

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.
Add the OnUnsubscribed hook to the unsubscribeClient method

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.

Update version number
Enforce server max packet (#121)

* Enforce Server Maximum Packet Size on client read
* Fix tests
Merge pull request #116 from tommyminds/bugfix/ws_malformed_package

Fix websocket malformed packet bug
Merge branch 'master' into bugfix/ws_malformed_package
Merge pull request #119 from mochi-co/fix-on-published

Fix mis-typed onpublished hook, update version, fanpool defaults
Fix mis-typed onpublished hook, update version, fanpool defaults

Fix websocket malformed packet bug

Update README.md
Simplify Client construction, add NewClient method to Server, add Publish convenience method

Add newline for godoc formatting

Update badges to use v2 references
Cleanup godoc formatting

Update README.md
Update go mod and imports to v2

Update go.mod
Update go.mod
Update README.md
Update README.md
Update README.md
Update README.md
Update build.yml
update github workflow go version to 1.19

Rewrite everything from scratch for mqtt v5

Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Contributions paused pending v2.0.0
Update README.md
Revert "Merge pull request #97 from alexsporn/fix/writer-full"

This reverts commit f22b8276e8c33c1e34f941beb5d59667bbda9de6, reversing
changes made to b2fc287a9885a94d14f394d84216d123220ab9d5.

Merge pull request #97 from alexsporn/fix/writer-full

Instead of waiting for the writing buffer to have enough space, skip writing and return an error
Merge branch 'mochi-co:master' into fix/writer-full

Merge pull request #99 from mochi-co/fix-inflight-race

Fix concurrent map access for clients and inflights causes data race 
Return copies of client and inflight maps to avoid missed locks

Increase inlinepub messages buffer

Instead of waiting for the writing buffer to have enough space, skip writing and return an error

Check against the correct clean session var for abandoning old inflights

Keep in sync server.System.Inflight (#92)

* Keep in sync server.System.Inflight

* Fix args order in tests
Update README.md
Update README.md
Abandon inflights at the end of clean-session connections

Merge pull request #90 from mochi-co/resend-inflights

Adds Inflight TTL and Period Resend
Adds Inflight TTL and Period Resend

Merge pull request #84 from mochi-co/goreport-fixes

Goreport fixes
remove ineffective assignments

apply gofmt -s

Merge pull request #83 from mochi-co/tls-client-auth

Expose tls.Config to Listeners
Merge pull request #82 from mochi-co/expose-event-client-username

Add CleanSession and Username to events.Client struct
use TLSConfig instead of deprecated TLS field

Add TLSConfig field to allow direct tls.Config setting

update TLS example to use TLSConfig field

Add CleanSession and Username to events.Client struct

Add OnSubscribe, OnUnsubscribe events examples

Extend onsusbcribe, onunsubscribe events

Merge pull request #74 from muXxer/feat/topic-subscription-events


Add topic un-/subscribe events

Merge pull request #72 from BoskyWSMFN/master

fix-panic
fix-panic

fixed runtime panic in server/internal/circ/pool.go occurring on 32-bits architectures caused by misalignment of BytesPool struct members.

https://github.com/golang/go/issues/36606#issue-551005857

fix comments

Add auth controller example

Add Docker info
Merge pull request #69 from mochi-co/v1.2.0

V1.2.0
use NewServer instead of New

update readme for new events

Merge pull request #68 from mochi-co/fix-store-retained

Fix Store Retained Messages
Merge branch 'v1.2.0' of https://github.com/mochi-co/mqtt into fix-store-retained

Merge pull request #67 from mochi-co/release-client-buffers

Release client buffers
only check final outcome due to races

accept any error for invalid protocol due to races

Check for protocol violation errors

Add comments

Remove unused code

Abandon client state if the existing client specified a cleansession

Expose CleanSession value for checking

Store retained message based on corrected r value

Expect correct r values for RetainMessage

Correctly return R value of retainMessage

Update EstablishConnection tests to ensure buffers and pool are correctly released after use

Export R/W buffer values so they can be assessed in tests without causing races

Track number of pool blocks in use

Use package errors instead of strings

test clarbuffers

clear buffers after deferred stop

refactor clients for buffer releasing

Refactor establishconnection to prevent same-id disconnects

refactor connSetup for clarity

Clarify error messages

clarify error checking

Use defer to release buffers and decrease stats on any client closure

Merge pull request #61 from mochi-co/server-options

Configurable Server Options
Merge pull request #63 from mochi-co/add-drop-packet-error

Add ErrRejectPacket to OnProcessMessage
Merge pull request #62 from mochi-co/fix-inflight-key

Fix Inflight Persistence Key
track logged error

Update test to check for packet rejection

Ensure OnError is set before using it

Update OnProcessMessage documentation

Optionally drop a packet if the ErrRejectPacket error is returned from OnProcessMessage

Add ErrRejectPacket error to abandon packet processing from OnMessageProcess

Merge pull request #53 from stffabi/feature/onprocessmessage-event

Events: Add OnProcessMessage event
fix inflight key reference

Fix code block formatting

Update readme with server options

Add example implementation

add tests for new NewServer function

remove deprecated log message

Update code to use new NewServer function instead of deprecated New

Update example code to use new NewServer function instead of deprecated New

Use internal default values instead of relying on passed value

Add Server Options

Adds a new struct of server options which can be used to override default properties. A new options-accepting NewServer function has been created to supersede the New method, which is now deprecated.

Update go mod to ensure bolt is using 1.3.5

Bolt 1.3.6 fails to build correctly and has been removed, so rollback to bolt 1.3.5. Also upgrade to Go 1.18

Merge pull request #57 from hybridgroup/v1.2.0-docker

docker: add initial simple Dockerfile
Merge pull request #58 from soyoo/patch-1

typo
typo
docker: add initial simple Dockerfile

Merge pull request #51 from jmacd/jmacd/noracefix

Two no-functional-change cleanups combined
Events: Add OnProcessMessage event

This event gets called right after ACL checking but before any other
Fields of the packet get evaluated.

Combines two fixes

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

Update README.md
Update README.md
Merge pull request #46 from stffabi/bugfix/acls-retain

Subscribe: Only send retained messages if ACLs has allowed subscription to the topic
Subscribe: Only send retained messages if ACLs has allowed subscription to the topic

Fix incorrect test

The previous publish inline test incorrectly approved retain packets without retain=true fixedheader values.

Publish: Set the retain flag in the fixedheader (#42)

* Publish: Set the retain flag in the fixedheader

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

# Conflicts:
#	server/internal/clients/clients.go

Update README.md
Update README.md
Replace Travis with Github Actions (#41)

* Remove Travis CI

* Add Github Actions Workflow

* Update badges for build status, coverage, report card, doc reference

* use actions for all pull requests and pushes

* test all files for coverage

* Apply gofmt -s to simplify code

* Fix typos

* Cleanup comments

* Cleanup comments

Co-authored-by: mochi <mochimou@icloud.com>
Fix typo

Add Keyed fields to events.Client for readability and go vet

Add missing method comments

Add an OnError handler; report the reason for disconnects. (#38)


Wrap packet errors with cause information (#39)


Move two WaitGroup.Add calls (#36)


Merge pull request #29 from jmacd/jmacd/payload_not_utf8

Support non-UTF8 payloads (per MQTT specification)
Support non-UTF8 payloads per MQTT specification

revert redis update
revert server version
Merge pull request #27 from mochi-co/revert-26-master

Revert "added redis persistence mode"
Revert "added redis persistence mode"

Update server version
Update README.md
Merge pull request #26 from wind-c/master

added redis persistence mode
redis and trie

add redis persistence mode and example

update server version

Merge pull request #24 from mochi-co/feature/optimise-struct-fields

Optimise Struct Fields + Fixes
optimise Server struct

pass byte pool by address

remove println

Pass inflight by address to avoid lock copying

Correct function signature

Update test to match new FixedHeader struct

Prevent locks from being copied

8bit align struct fields

Update comment for clarity

Update version to 1.1.0

indicate ARM32 compatibility

Merge pull request #22 from mochi-co/feature/32bit-compatibility

ARM32 Compatibility
Merge pull request #19 from rkennedy/bugfix/32-bit-atomic-alignment

Improve 32-bit compatibility
Fix encodeLength for 32-bit platforms

When `int` is 32 bits, `MaxInt64` doesn't fit. It's apparent that
`encodeLength` expects to handle 64-bit inputs, so let's make that
explicit, which allows the test to run on all platforms.

Avoid race condition when closing listeners

"Atomic load" followed by "atomic store" is not itself an atomic
operation. This commit replaces that sequence with CompareAndSwap
instead.

Make atomics work on 32-bit systems

On 32-bit systems, `atomic` requires its 64-bit arguments to have 64-bit
alignment, but the compiler doesn't help ensure that's the case. In this
commit, fields that don't need to hold large numbers have been converted
to 32-bit types, which are always aligned correctly on all platforms.
For fields that may hold large numeric values, padding has been added to
get the necessary alignment, and tests have been added to avoid
regressions.

Update server version to 1.0.5

Merge pull request #18 from mochi-co/feature/connect-disconnect-hooks

OnConnect and OnDisconnect Event Hooks
Update for OnConnect and OnDisconnect hooks

Add tests for OnConnect, OnDisconnect

Add OnConnect and OnDisconnect hooks to example

Call OnDisconnect Event if applicable

Add OnDisconnect Event Hook

Add testbolt file to ignore list

Call OnConnect Event if applicable

Add OnConnect event hook

Prevent locks being copied by passing non-pointer to FromClient

Merge pull request #15 from ClarkQAQ/master

Fixed some bugs, wish the project better and better
update tcp.go maybe this will be better

fix local variable black hole

update mock.go plase use range

fix [ST1005] strings should not be capitalized

update websocket.go fix check origin

Update README.md
Merge pull request #14 from mochi-co/feature/allow-clients-value

Add AllowClients Field to packets
Add example for AllowClients field

Add test for AllowClients field

Remove unnecessary type declarations

Add setupServerClients to inherit existing server instance

previously new clients generated a new server object, so system stats were not shared. This change ensures all test clients use the same server

Add AllowClients check in publishToSubscribers

If AllowClients has been set on a packet, ensure only clients in the slice are sent the message

use .systemInfo instead of .system for clarity

use .systemInfo instead of .system for clarity

Add AllowClients field to packets

AllowClients field can be specified during onMessage event to selectively deliver messages

Increment server version

Add tests for InSliceString

Add InSliceString function

Check if a slice of strings contains a string (until slices package available)

Revert server version

increment server version

Remove unnecessary fmt import

Increment server version

Merge pull request #12 from jphastings/remove-erroneous-print


Remove unnecessary println

fix indentation in code blocks

convert tabs to spaces
Update README.md
Update vendor

Update go mod to 1.17

fix code indents

Update go to 1.17

Increment server version to 1.0.1

Merge pull request #11 from mochi-co/feature/event-hooks-publish

Feature/event hooks publish
fix onmessage test

change scheduled message for clarity

remove redundant code

Update Readme to add Event Hooks section

Merge OnMessage and OnMessageModify

Update events example with publish hooks

Adds tests for publishing event hooks

Add Event Hooks

Adds basic event hooks (OnMessage, OnMessageModify) to the server using the new events library.

Add Events

Events library contains event hook types and related utility functions

Return packets to internal

Now that we can alias types, there's no compelling reason to expose the packets library

Merge pull request #10 from mochi-co/expose-packets

Expose packets library
Merge pull request #8 from mochi-co/feature/inline-publish

Inline Publishing
update packets library import reference

expose packets library

Add .DS_Store to ignore list

Update with direct publishing

Adds information about direct publishing and moves performance section

Add inline publishing example

Adds an example file which demonstrates the usage of the `Publish` method. This file will also be used to demonstrate event hooks.

Add tests for new inline publishing method

Directly publish messages from embedding system

When the broker is embedded in a larger Go codebase, it is beneficial to be able to publish messages directly from the system to topics. This change provides a Publish method which adds messages to an inline publishing queue in a separate goroutine, which are then processed in the standard way and issued to all clients with matching topic filters.

Update comments and rename input parameter for clarity

Update comments for clarity

Add  .gitignore

Ensure we're not committing any binaries

Remove Codacy badge
Update Readme


Update Readme


Update Chart Labels


Update Readme


Update Badges


Update Badges


Fix test races


Update travis


Fix examples


Add TravisCI


Add badges


Update Readme


Update Readme


Resort Charts


Resort Charts


Charts


Image test


Image test


Update README


Update README, better command main


Code and Comments cleanup, vendor deps


Persistence V1


Adds delete from persistence


Adds more persistence tests


Load persistence into server


Persistence and tests


Inflght and retained messages persistence


Progress on persistence


Adds TLS/SSL


Websocket Listener


Don't receive $SYS retained on #


Publish $SYS Stats to topics


Basic $SYS stats


Merge branch 'restructure-paths'
Http Sys Stats listener


Restructures code


Fix tests


Pass Paho Tests


Dont inflight secondary qos flow messages


Satisfy Keepalive, fix Keepalive 0


Small fix


Satisfy 4.7.2 - restrict $ topics


Periodic Resend of Inflight messages


Cleanup TCP Listener


Merge remote-tracking branch 'origin/master'


Merge pull request #1 from mochi-co/iobuffers

Iobuffers
Merge branch 'iobuffers'
Fix close sequence, update test coverage


LWT and Validate packet


bytes buffer to pool


refactor pointers


Publish


Process packets


Establish Tests


start establish 


client write packet


update tests


Rebuilding


New Packets


Fix CheckEmpty


Rebuild


Rebuild


Rebuild


Rebuild


Rebuild


working but bottlenecks


pre-refactor


More tests, connecting MQTT


More Tests


Fixes sync.cond deadlock


Debug func, better closers


Tests and buffer sizes


Write Bytes


Processor Read and Tests


Refactor, fixes to Circ Peek, start processor/parser


WriteTo / Tests


Read+Read Test


cleanup


AwaitFilled


Cleanup, start reader/writer model


Small fixes


WriteTo / Tests


Start on Peek


ReadFrom IO


AwaitCapacity tests


Working wait logic


Move Parser, cleanup to basic


Cleanup


All working


Adds Retained Delete


Cleanup, Tests fix, Client closers


Fix packet buffer mutation


midway various pointer bytes fixes


server cmd


Cleanup


Fix unsafe.pointer, unsub cascade bugs


Testing example


Cleanup


Fix Error nil/contains checks


Send LWT+tests


Resend unsent inFlight


Performance changes


Cleanup tests and benchmarks


Handle CleanSession


Pub/sub ACL and acks


Write Client coverage


Client Tests


Tests Cleanup


Refactor Tests


Subscribe Retain


Subscribe basic + Unsubscribe


Pubcomp


Pubrel + Pubrec


Fix Establish tests


Fix Establish test


Process Publish+Recv


Switch out bufio pools


Start processing Publish


Zero-alloc retain messages + fixes


Zero-alloc topics


Alloc free subscribers


Topics interface


Deprecate particle bucket subscribers


Trie subscribers tree


Start processing packets


Update more tests


Update more tests


Refactor Clients into Server


Refactor packets/parser to take bufio rw


Add bufio rw pools


Refactor Client read to Server


Refactor fixedheader


Auth Controllers and listener options


Client Tests


Refactor MockNetConn


Add auth controller interface


Refactor Listener into Listen()


Decode a Connect packet on connection


Divest Validation from Parser


Cleanup Packets tests


Adds Mock net.Conn, errors for establisher


Refactor listeners for performance


Reworking listeners


Error strings to errors


Remove limiter


Add Benchmarks and tests


Add README


Cleanup


alloc free encoding


Convert all packet processes to byte.buffers


Benchmarks


Cleanup


New Packets library and new benchmarks


Initial commit
## Branch: origin/prod

production code

Initial commit
## Branch: origin/pubsub

added pubsub

Merge branch 'packetchange' of https://gitlab.iserveu.tech/soundbox/mqtt_server_soundbox into pubsub

playstatus 1 client

updated_time

_ time

packet change

rm go routine in onpacketread

Revert "added worker pool"

tttt reverts commit 82fd5667c5419ac5b3efea31bd2d7d46f14866e0.

changed type for update api

added worker pool

optimise api call

added sleep

added time stamp for asia location

error handling txn insert

insert transaction api call

initial commit

Update server version

Move cl.WriteLoop() to attachClient() and call cl.Stop() in loadClients() to update client.State. (#344)

* Moving go cl.WriteLoop() out of NewClient() and placing it in server.attachClient().

* Call cl.Stop() to cancel the context, update cl.State with information such as disconnected time, and set the stopCause.

* update README-CN.md

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
feat: return tcp.Address from listener, if exists (#336)

* This is the more accurate and correct address of the listener
* Useful if you want to listen on port 0 to dynamically create
listeners (think of unit/integration tests)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Packet encoding optimization (#343)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

* Reduce double write of pk.Payload

* Use memory pool for packet encode

* Pool doesn't guarantee value between Put and Get

* Add benchmark for bufpool

* Fix issue #346

* Change default pool not to have size cap

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix data race issue with write buffer (#347)


Handle expired clients in server.loadClients(). (#341)

* Handle expired clients in server.loadClients().

* No need to call s.Clients.Delete().

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Dynamically allocate write buffer if needed. (ready for merge) (#324)

* Dynamically allocate buffer for writes if needed

* Remove unused net.Buffer

* Return bytes written to buffer instead of conn

* Dynamic write buffer

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add a Japanese version of README.md (#338)

* Add a Japanese version of README.md

* add jp link
Add a demonstration in examples/hooks on how to subscribe to a topic and publish messages directly within the hook. (#333)


Revert "improve transport performance with bufio (#321)" (#323)

This reverts commit 8e52e49b94026c3380b8c2cacce22fc565858cc7.
improve transport performance with bufio (#321)

* improve transport performance with bufio

* fix issue of unit test

* fix issue

* optimize code
Fix for unlimited maximum message expiry interval (#315)

* fix when no max msg expiry interval is set

* fix expiry handling of clearExpiredInflights

* Modify it to handle cases where the MaximumMessageExpiryInterval is set to 0 or math.MaxInt64 for no expiry, and optimize some of the code and test cases.

* Set MaximumMessageExpiryInterval to 0 or math.MaxInt64 for no expiration, and optimize some of the code and test cases.

* Addressing the issue of numeric overflow with expiration values.

* Only when server.Options.Capabilities.MaximumMessageExpiryInterval is set to math.MaxInt64 for no expiry.

* fix typo in README.md

* There is no need to verify whether 'maximumExpiry' is 'math.MaxInt64' within 'client.ClearInflight()

* Optimize the code to make it easier to understand.

* Differentiate the handling of 'expire' in MQTTv5 and MQTTv3; skip expiration checks if MaximumMessageExpiryInterval is set to 0; optimize code and test cases.

* When MaximumMessageExpiryInterval is set to 0, it should not affect the message's own expiration(for v5) evaluation.

* Adding client.ClearExpiredInflights() to clear expired messages, while client.ClearInflights() is used to clear all inflight messages.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werben <werben@aliyun.com>
Co-authored-by: werben <werben@qq.com>
Remove vendor folder (#319)

* Remove vendor folder

* Add vendor to gitignore

---------

Co-authored-by: mochi-co <moumochi@icloud.com>
Bump golang.org/x/net from 0.7.0 to 0.17.0 (#316)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.7.0 to 0.17.0.
- [Commits](https://github.com/golang/net/compare/v0.7.0...v0.17.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
update README-CN.md (#312)


Update README.md
Indicate translators wanted
Emit warning if client keepalive is less than recommended minimum (#305)

Co-authored-by: mochi-co <moumochi@icloud.com>
Add a Chinese version of README.md. (#307)

* Add a Chinese version of the README.md.

* rename README_CN.md to README-CN.md

* Optimize some aspects

* Correct some translation errors.

* Optimize some aspects.

* Initial completion of all translations.

* Optimize some aspects.

* Optimize some aspects.

* Refinement of translations.
only build docker on tag for mochi-mqtt repo

Add some error logging in Listener.Serve(). (#303)

* Add some error logging in Listener.Serve().

* Remove error logging for TCP listener Accept() calls.

* Optimize code.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update build.yml
Update build.yml

multiple platforms
Update build.yml
Update build.yml
Update build.yml

alternative tags attempt
Update build.yml
Fix docker repo name
Update build.yml

test push to docker with version
Update build.yml

test pushing directly to docker
Update build.yml
Refactor Listener WG to track clients (#301)


Update readme v2.4.0

Small fixes and cleanups (#295)

* fix typos, indicate unused returns

* Add test for publishToClient acl unauthorized

* Add Inline Client as a server option
Disconnect or return ack if unauthorized publish (#292)

* Ensure msg doesn't exceed subscription QoS

* Disconnect or return ack if unauthorized publish

* Disconnect or return ack if unauthorized publish

* Create new server for eery test case

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Another code implementation for Inline Client Subscriptions. (#284)

* Another code implementation for Inline Client Subscriptions.

* Added a few test cases.

* Changed the return value types of Server.Unsubscribe() and Subscribe() to boolean.

* Implementing the delivery of retained messages and supporting multiple callbacks per topic using different inline client IDs.

* Added validation checks for the legality of the inline client id during Subscribe and Unsubscribe.

* Added validation checks for the legality of the client during Subscribe and Unsubscribe.

* Fixed the TestServerSubscribe/invalid_client_id test case failure.

* Add Server.inlineClient and Temporarily removing test cases for better code review readability.

* Using server.inlineClient in server.InjectPacket().

* After unsubscribing, if there are other subscriptions in particle.inlineSubscriptions, particle cannot be deleted.

* Add comments to particle.inlineSubscriptions and modify to return ErrTopicFilterInvalid when the topic is invalid during subscription.

* Fixed some test case failures caused by adding inlineClient to the server.

* More test cases have been added.

* Optimization of test case code.

* Modify server.go: When used as a publisher, treat the qos of inline client-published messages as 0.

* Resolve conflict.
Migrate from zerolog to slog (#248)

* Begin adding new slog calls

* Fixed unit tests

* Add leveler example

* Add debug log level to Redis example

* Change location of server.Close() and add logs to example/hooks

* Begin removing references to zerolog

* Removed final references to zerolog

* Change where server.Close() occurs in main

* Change to 1.21 to remove x dependency

* Add slog

* Update references to 1.21

* Begin change of LogAttrs to standard logging interface

* Change the rest of LogAttrs to default

* Fix bad log

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update badger.go

Changing "data" to "key" or "id" here might be more appropriate.

* Update server.go

Not checking if err is equal to nil

* Update server.go

printing information for ID or error is missing.

* Change references of err.Error() to err in slog

* Remove missed removal of Error() references for logging

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: werbenhu <werben@qq.com>
add aclcheck in publishToClient (#287)

Co-authored-by: unknow <beunknow@outlook.com>
Fix readme example (#276)

* Update README example to better match other examples

* Fix formatting

* Fix err formatting issue

* Fix bad import in README example

---------

Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Use JSONeq to compare JSON (#267)

* WriterSize parameter is incorrectly set

The WriterSize parameter is incorrectly set in the newClient method.

* Use JSONeq to compare JSON

This ensures that test results pass even if the field order is inconsistent.

---------

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Update README.md
Fix badges
Update README.md
Update README.md
migrate imports, copyrights, etc (#270)


Update server version

Allow Publish to return custom Ack error responses (#256)

* Allow publish error returns as acks

* Add Ignore Packet, tests
fix: fix data-race in badger hook (#266)

Co-authored-by: Gabriel Sagula <gsagula@magicleap.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
method UnsubscribeClient's packet add fixedHeader (#264)


Do not retain messages if retain is not available (#261)

* Do not retain messages if retain is not available

* Add Test
Preference Write, Read, Deny filters in ledger (#262)


Retain flag should be delivered as false in v3 (#257)

* retain should be delivered as false in v3

* Forward retained flag if publish is from subscribe action
Fix websocket reads for packets > 1 buffer size (#260)


Update README.md
Ensure msg doesn't exceed subscription QoS (#253)

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
WriterSize parameter is incorrectly set (#252)

The WriterSize parameter is incorrectly set in the newClient method.
Small language clarification for non-english

Update server version

Add OnSessionEstablish hook (#247)

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update Readme

Add Healthcheck listener

Update README.md
Update SPDX annotations

Update Contribution Guidelines

Update server version

Add healthcheck listener (#244)

* Add healthcheck listener

* Update improper comments

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Fix ScanSubscribersTopicInheritanceBug (#243)

* Sub a/b should not receive msg for a/b/c...

* Add TestScanSubscribersTopicInheritanceBug test

* Ensure sharedSubscription are gathered

* Fix Unsubscribe for sharedSub and optimization

* Unsub with lower case in TestUnsubscribeShared

* Add test with # for TestScanSubscribersShared
Update Hooks List

Update Server Version

Expose SendConnack, err return on OnConnect (#240)


Add OnRetainPublished hook (#237)

* Add OnRetainPublished hook

* Skip OnRetainPublished if publish error
Update server version

Add retainMessage to LWT to properly handle message retention (#234)

* Add retainMessage to LWT to properly handle message retention if specified in connect

* Add will retain flag on missed test

---------

Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Update server version

Now when a "publish" command fails, then the publish method will throw an error (#229)

Errors in the hook when doing a publish were ignored. This caused that test cases could not be made where the publish failed and an error was thrown.

Co-authored-by: hector.oliveros@wabtec.com <hectoroliveros@MacBook-Pro-de-Hector.local>
Minimize client lock duration (#223)

* Minimize client lock duration
* Fix server option example

Fix example usage of NewHTTPStats (#231)

Co-authored-by: Dominic Plourde <plourded@amotus.ca>
Update README.md new benchmarks
update server version

Use context to exit WriteLoop (#222)

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Use context to exit WriteLoop

* Fix misspelling
update server version

refactor server keepalive for hook access (#220)


Use context to signal client open state (#218)


Add packet ID exhausted hook (#217)


Expire session if SessionExpiryInterval is 0 (#216)

If SessionExpiryInterval was not set in CONNECT, SessionExpiryIntervalFlag is also not set. According to spec:
  If the Session Expiry Interval is absent the value 0 is used. If it is set to 0, or is absent, the Session ends when the Network Connection is closed.
Update codes.go (#215)

fix typo
Update codes.go (#214)

Fix typo
Update server version

Lock on close outbound (#213)


Add lock to client writes (#212)


Add OnPacketIDExhausted hook (#211)


Correctly validate WillProperties (#210)

Co-authored-by: sukvojte <sukvojte@gmail.com>
Update build.yml (#203)


Protect close of nil outbound channel

Protect close of nil outbound channel

#78 storage hook should not execute the relevant code if the client has been reconnected (#198)

* storage hook should not execute the relevant code if the client has been reconnected #78

* add test cases for coverage decrease

add test cases for coverage decrease
Move msgToPacket to storage.Message.ToPacket

Simplified code (#195)

Simplify the code for the loadInflight and loadRetained methods.
Adjust the validation order of the processSubscribe method to ensure that it fails quickly if there is an error, since s.hooks. OnACLCheck generally takes a long time.

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Ensure to close client WriteLoop (#193)

* Ensure client WriteLoop is closed

* Ensure to close client WriteLoop
fix: common subscriptions issued by different clients at the same time may be lost (#186)


Update readme

Update server version

Configurable client bufio reader/writer sizes (#190)


Update server version

Bump golang.org/x/net from 0.0.0-20220927171203-f486391704dc to 0.7.0 (#182)

Bumps [golang.org/x/net](https://github.com/golang/net) from 0.0.0-20220927171203-f486391704dc to 0.7.0.
- [Release notes](https://github.com/golang/net/releases)
- [Commits](https://github.com/golang/net/commits/v0.7.0)

---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Skip expire cleanup for isTakenOver session (#183)

* Skip expire cleanup for isTakenOver session

* Set prev connection to isTakenOver on CleanSession

#173.
Allow 0 byte usernames if correctly formed (#181)

* Allow 0 byte usernames if correctly formed

* Allow 0 byte usernames if correctly formed
Correctly identify and clean taken-over sessions (#180)


Small style fix

Update server version

Use *packets.Packet for outbound chan (#176)

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan

* Use *packets.Packet for outbound chan
update server version

fix: correct decoding of packets including Properties exceeding 127 bytes in length (#172)


Update server version

Expose dropped publish messages count in sys info (#170)


Fix potential NextPacketID endless loop, expand tests (#169)

* Fix possible NextPacketID endless loop, expand tests

* Optimize NextPacketID

* Use math constants
Add PublishDropped metrics (#167)

* Add PublishDropped

* Add PublishDropped

* Add PublishDropped

* Update storage_test.go

* Update system.go

* Update server.go
No longer issue retained messages on session takeover (#166)


Client write buffers (#165)

* Replace fanpool with client write buffers
Add Clone to system.Info (#163)

* Add Clone using atomic operations

* Add Clone using atomic operations

* Use sysinfo.Clone

* Unit test for Clone

* Add Clone using atomic operations

* Update

* Update
Update server version

failed to delete inflight data (#162)

The s.hooks.OnQosPublish method needs to be called, otherwise the following s.hooks.OnQosComplete or processPuback(s.hooks.OnQosComplete) method will report a data not found error.
Update server version

Rename Quota methods for clarity (#159)


Move refreshDeadline to only trigger on successful transmission (#157)


Include a listener accepting an existing net.Listener (#155)


invalid config type provided (#152)

* invalid config type provided

examples/persistence/bolt/main.go: invalid config type provided

* fixed ErrReceiveMaximum(receive maximum exceeded)

No quotas of the inflight is set in the readStore method, so each quota is equal to 0. The inheritClientSession method overrides the quotas of the new client inflight, so the processPublish method reports an ErrReceiveMaximum and disconnects the client.

* reset receive quota

receive quota should be reset across connections (as specified in the spec).
Update server version

Publish retained messages only after connack (#147)


Use Atomic instead of RWMutex for Hooks concurrency (#148)

* Use Atomic instead of RWMutex for Hooks concurrency
* Lock Hooks on Add Hook
Ignore retain as published v3 (#142)

* Optimise Capabilities struct alignment

* Only use RetainAsPublished for v5 clients
Update version number

Use correct connack return codes for MQTTv3 (#140)


Update server version

Fix example imports

export client.Net.Conn for external use

Small code improvements

Make hooks safe for concurrency (#139)

Co-authored-by: thedevop <60499013+thedevop@users.noreply.github.com>

Update server version

Change inline check order (#133)


fix grammar on Closed method doc

Update version number

Refactor stored subscription value assignments

Fix Typos

Save subscription properties for mqttv5 (#131)

* Update redis.go

Save the subscription properties for mqqtv5

* Update badger.go

Save the subscription properties for mqqtv5

* Update bolt.go

Save the subscription properties for mqqtv5

Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Add Client Closed (#130)

* Add Client Closed
* Add Client Closed
* Update clients_test.go
Update README.md
Update README.md
Update readme and server version

Connect ReturnResponseInfo only applies to Connack values (#128)


Optimize inflight expiry (#127)

* Small formatting/style changes for filter existed

* Use OnQoSDropped hook instead of onInflightExpired
Merge pull request #123 from wind-c/master

Variable existed in the method processSubscribe is unstable
Merge branch 'master' into master
Merge pull request #124 from zgwit/master

Add unix socket listener
Add unix socket listener

Variable existed in the method processSubscribe is unstable

The variable existed can be changed repeatedly within a for loop. An array variable must be used to record the subscription of each filter.
Merge branch 'mochi-co:master' into master

Update server version
Add the OnUnsubscribed hook to the unsubscribeClient method (#122)

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.
Add the OnUnsubscribed hook to the unsubscribeClient method

Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.

Update version number
Enforce server max packet (#121)

* Enforce Server Maximum Packet Size on client read
* Fix tests
Merge pull request #116 from tommyminds/bugfix/ws_malformed_package

Fix websocket malformed packet bug
Merge branch 'master' into bugfix/ws_malformed_package
Merge pull request #119 from mochi-co/fix-on-published

Fix mis-typed onpublished hook, update version, fanpool defaults
Fix mis-typed onpublished hook, update version, fanpool defaults

Fix websocket malformed packet bug

Update README.md
Simplify Client construction, add NewClient method to Server, add Publish convenience method

Add newline for godoc formatting

Update badges to use v2 references
Cleanup godoc formatting

Update README.md
Update go mod and imports to v2

Update go.mod
Update go.mod
Update README.md
Update README.md
Update README.md
Update README.md
Update build.yml
update github workflow go version to 1.19

Rewrite everything from scratch for mqtt v5

Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Update README.md
Contributions paused pending v2.0.0
Update README.md
Revert "Merge pull request #97 from alexsporn/fix/writer-full"

This reverts commit f22b8276e8c33c1e34f941beb5d59667bbda9de6, reversing
changes made to b2fc287a9885a94d14f394d84216d123220ab9d5.

Merge pull request #97 from alexsporn/fix/writer-full

Instead of waiting for the writing buffer to have enough space, skip writing and return an error
Merge branch 'mochi-co:master' into fix/writer-full

Merge pull request #99 from mochi-co/fix-inflight-race

Fix concurrent map access for clients and inflights causes data race 
Return copies of client and inflight maps to avoid missed locks

Increase inlinepub messages buffer

Instead of waiting for the writing buffer to have enough space, skip writing and return an error

Check against the correct clean session var for abandoning old inflights

Keep in sync server.System.Inflight (#92)

* Keep in sync server.System.Inflight

* Fix args order in tests
Update README.md
Update README.md
Abandon inflights at the end of clean-session connections

Merge pull request #90 from mochi-co/resend-inflights

Adds Inflight TTL and Period Resend
Adds Inflight TTL and Period Resend

Merge pull request #84 from mochi-co/goreport-fixes

Goreport fixes
remove ineffective assignments

apply gofmt -s

Merge pull request #83 from mochi-co/tls-client-auth

Expose tls.Config to Listeners
Merge pull request #82 from mochi-co/expose-event-client-username

Add CleanSession and Username to events.Client struct
use TLSConfig instead of deprecated TLS field

Add TLSConfig field to allow direct tls.Config setting

update TLS example to use TLSConfig field

Add CleanSession and Username to events.Client struct

Add OnSubscribe, OnUnsubscribe events examples

Extend onsusbcribe, onunsubscribe events

Merge pull request #74 from muXxer/feat/topic-subscription-events


Add topic un-/subscribe events

Merge pull request #72 from BoskyWSMFN/master

fix-panic
fix-panic

fixed runtime panic in server/internal/circ/pool.go occurring on 32-bits architectures caused by misalignment of BytesPool struct members.

https://github.com/golang/go/issues/36606#issue-551005857

fix comments

Add auth controller example

Add Docker info
Merge pull request #69 from mochi-co/v1.2.0

V1.2.0
use NewServer instead of New

update readme for new events

Merge pull request #68 from mochi-co/fix-store-retained

Fix Store Retained Messages
Merge branch 'v1.2.0' of https://github.com/mochi-co/mqtt into fix-store-retained

Merge pull request #67 from mochi-co/release-client-buffers

Release client buffers
only check final outcome due to races

accept any error for invalid protocol due to races

Check for protocol violation errors

Add comments

Remove unused code

Abandon client state if the existing client specified a cleansession

Expose CleanSession value for checking

Store retained message based on corrected r value

Expect correct r values for RetainMessage

Correctly return R value of retainMessage

Update EstablishConnection tests to ensure buffers and pool are correctly released after use

Export R/W buffer values so they can be assessed in tests without causing races

Track number of pool blocks in use

Use package errors instead of strings

test clarbuffers

clear buffers after deferred stop

refactor clients for buffer releasing

Refactor establishconnection to prevent same-id disconnects

refactor connSetup for clarity

Clarify error messages

clarify error checking

Use defer to release buffers and decrease stats on any client closure

Merge pull request #61 from mochi-co/server-options

Configurable Server Options
Merge pull request #63 from mochi-co/add-drop-packet-error

Add ErrRejectPacket to OnProcessMessage
Merge pull request #62 from mochi-co/fix-inflight-key

Fix Inflight Persistence Key
track logged error

Update test to check for packet rejection

Ensure OnError is set before using it

Update OnProcessMessage documentation

Optionally drop a packet if the ErrRejectPacket error is returned from OnProcessMessage

Add ErrRejectPacket error to abandon packet processing from OnMessageProcess

Merge pull request #53 from stffabi/feature/onprocessmessage-event

Events: Add OnProcessMessage event
fix inflight key reference

Fix code block formatting

Update readme with server options

Add example implementation

add tests for new NewServer function

remove deprecated log message

Update code to use new NewServer function instead of deprecated New

Update example code to use new NewServer function instead of deprecated New

Use internal default values instead of relying on passed value

Add Server Options

Adds a new struct of server options which can be used to override default properties. A new options-accepting NewServer function has been created to supersede the New method, which is now deprecated.

Update go mod to ensure bolt is using 1.3.5

Bolt 1.3.6 fails to build correctly and has been removed, so rollback to bolt 1.3.5. Also upgrade to Go 1.18

Merge pull request #57 from hybridgroup/v1.2.0-docker

docker: add initial simple Dockerfile
Merge pull request #58 from soyoo/patch-1

typo
typo
docker: add initial simple Dockerfile

Merge pull request #51 from jmacd/jmacd/noracefix

Two no-functional-change cleanups combined
Events: Add OnProcessMessage event

This event gets called right after ACL checking but before any other
Fields of the packet get evaluated.

Combines two fixes

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

Update README.md
Update README.md
Merge pull request #46 from stffabi/bugfix/acls-retain

Subscribe: Only send retained messages if ACLs has allowed subscription to the topic
Subscribe: Only send retained messages if ACLs has allowed subscription to the topic

Fix incorrect test

The previous publish inline test incorrectly approved retain packets without retain=true fixedheader values.

Publish: Set the retain flag in the fixedheader (#42)

* Publish: Set the retain flag in the fixedheader

Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2

# Conflicts:
#	server/internal/clients/clients.go

Update README.md
Update README.md
Replace Travis with Github Actions (#41)

* Remove Travis CI

* Add Github Actions Workflow

* Update badges for build status, coverage, report card, doc reference

* use actions for all pull requests and pushes

* test all files for coverage

* Apply gofmt -s to simplify code

* Fix typos

* Cleanup comments

* Cleanup comments

Co-authored-by: mochi <mochimou@icloud.com>
Fix typo

Add Keyed fields to events.Client for readability and go vet

Add missing method comments

Add an OnError handler; report the reason for disconnects. (#38)


Wrap packet errors with cause information (#39)


Move two WaitGroup.Add calls (#36)


Merge pull request #29 from jmacd/jmacd/payload_not_utf8

Support non-UTF8 payloads (per MQTT specification)
Support non-UTF8 payloads per MQTT specification

revert redis update
revert server version
Merge pull request #27 from mochi-co/revert-26-master

Revert "added redis persistence mode"
Revert "added redis persistence mode"

Update server version
Update README.md
Merge pull request #26 from wind-c/master

added redis persistence mode
redis and trie

add redis persistence mode and example

update server version

Merge pull request #24 from mochi-co/feature/optimise-struct-fields

Optimise Struct Fields + Fixes
optimise Server struct

pass byte pool by address

remove println

Pass inflight by address to avoid lock copying

Correct function signature

Update test to match new FixedHeader struct

Prevent locks from being copied

8bit align struct fields

Update comment for clarity

Update version to 1.1.0

indicate ARM32 compatibility

Merge pull request #22 from mochi-co/feature/32bit-compatibility

ARM32 Compatibility
Merge pull request #19 from rkennedy/bugfix/32-bit-atomic-alignment

Improve 32-bit compatibility
Fix encodeLength for 32-bit platforms

When `int` is 32 bits, `MaxInt64` doesn't fit. It's apparent that
`encodeLength` expects to handle 64-bit inputs, so let's make that
explicit, which allows the test to run on all platforms.

Avoid race condition when closing listeners

"Atomic load" followed by "atomic store" is not itself an atomic
operation. This commit replaces that sequence with CompareAndSwap
instead.

Make atomics work on 32-bit systems

On 32-bit systems, `atomic` requires its 64-bit arguments to have 64-bit
alignment, but the compiler doesn't help ensure that's the case. In this
commit, fields that don't need to hold large numbers have been converted
to 32-bit types, which are always aligned correctly on all platforms.
For fields that may hold large numeric values, padding has been added to
get the necessary alignment, and tests have been added to avoid
regressions.

Update server version to 1.0.5

Merge pull request #18 from mochi-co/feature/connect-disconnect-hooks

OnConnect and OnDisconnect Event Hooks
Update for OnConnect and OnDisconnect hooks

Add tests for OnConnect, OnDisconnect

Add OnConnect and OnDisconnect hooks to example

Call OnDisconnect Event if applicable

Add OnDisconnect Event Hook

Add testbolt file to ignore list

Call OnConnect Event if applicable

Add OnConnect event hook

Prevent locks being copied by passing non-pointer to FromClient

Merge pull request #15 from ClarkQAQ/master

Fixed some bugs, wish the project better and better
update tcp.go maybe this will be better

fix local variable black hole

update mock.go plase use range

fix [ST1005] strings should not be capitalized

update websocket.go fix check origin

Update README.md
Merge pull request #14 from mochi-co/feature/allow-clients-value

Add AllowClients Field to packets
Add example for AllowClients field

Add test for AllowClients field

Remove unnecessary type declarations

Add setupServerClients to inherit existing server instance

previously new clients generated a new server object, so system stats were not shared. This change ensures all test clients use the same server

Add AllowClients check in publishToSubscribers

If AllowClients has been set on a packet, ensure only clients in the slice are sent the message

use .systemInfo instead of .system for clarity

use .systemInfo instead of .system for clarity

Add AllowClients field to packets

AllowClients field can be specified during onMessage event to selectively deliver messages

Increment server version

Add tests for InSliceString

Add InSliceString function

Check if a slice of strings contains a string (until slices package available)

Revert server version

increment server version

Remove unnecessary fmt import

Increment server version

Merge pull request #12 from jphastings/remove-erroneous-print


Remove unnecessary println

fix indentation in code blocks

convert tabs to spaces
Update README.md
Update vendor

Update go mod to 1.17

fix code indents

Update go to 1.17

Increment server version to 1.0.1

Merge pull request #11 from mochi-co/feature/event-hooks-publish

Feature/event hooks publish
fix onmessage test

change scheduled message for clarity

remove redundant code

Update Readme to add Event Hooks section

Merge OnMessage and OnMessageModify

Update events example with publish hooks

Adds tests for publishing event hooks

Add Event Hooks

Adds basic event hooks (OnMessage, OnMessageModify) to the server using the new events library.

Add Events

Events library contains event hook types and related utility functions

Return packets to internal

Now that we can alias types, there's no compelling reason to expose the packets library

Merge pull request #10 from mochi-co/expose-packets

Expose packets library
Merge pull request #8 from mochi-co/feature/inline-publish

Inline Publishing
update packets library import reference

expose packets library

Add .DS_Store to ignore list

Update with direct publishing

Adds information about direct publishing and moves performance section

Add inline publishing example

Adds an example file which demonstrates the usage of the `Publish` method. This file will also be used to demonstrate event hooks.

Add tests for new inline publishing method

Directly publish messages from embedding system

When the broker is embedded in a larger Go codebase, it is beneficial to be able to publish messages directly from the system to topics. This change provides a Publish method which adds messages to an inline publishing queue in a separate goroutine, which are then processed in the standard way and issued to all clients with matching topic filters.

Update comments and rename input parameter for clarity

Update comments for clarity

Add  .gitignore

Ensure we're not committing any binaries

Remove Codacy badge
Update Readme


Update Readme


Update Chart Labels


Update Readme


Update Badges


Update Badges


Fix test races


Update travis


Fix examples


Add TravisCI


Add badges


Update Readme


Update Readme


Resort Charts


Resort Charts


Charts


Image test


Image test


Update README


Update README, better command main


Code and Comments cleanup, vendor deps


Persistence V1


Adds delete from persistence


Adds more persistence tests


Load persistence into server


Persistence and tests


Inflght and retained messages persistence


Progress on persistence


Adds TLS/SSL


Websocket Listener


Don't receive $SYS retained on #


Publish $SYS Stats to topics


Basic $SYS stats


Merge branch 'restructure-paths'
Http Sys Stats listener


Restructures code


Fix tests


Pass Paho Tests


Dont inflight secondary qos flow messages


Satisfy Keepalive, fix Keepalive 0


Small fix


Satisfy 4.7.2 - restrict $ topics


Periodic Resend of Inflight messages


Cleanup TCP Listener


Merge remote-tracking branch 'origin/master'


Merge pull request #1 from mochi-co/iobuffers

Iobuffers
Merge branch 'iobuffers'
Fix close sequence, update test coverage


LWT and Validate packet


bytes buffer to pool


refactor pointers


Publish


Process packets


Establish Tests


start establish 


client write packet


update tests


Rebuilding


New Packets


Fix CheckEmpty


Rebuild


Rebuild


Rebuild


Rebuild


Rebuild


working but bottlenecks


pre-refactor


More tests, connecting MQTT


More Tests


Fixes sync.cond deadlock


Debug func, better closers


Tests and buffer sizes


Write Bytes


Processor Read and Tests


Refactor, fixes to Circ Peek, start processor/parser


WriteTo / Tests


Read+Read Test


cleanup


AwaitFilled


Cleanup, start reader/writer model


Small fixes


WriteTo / Tests


Start on Peek


ReadFrom IO


AwaitCapacity tests


Working wait logic


Move Parser, cleanup to basic


Cleanup


All working


Adds Retained Delete


Cleanup, Tests fix, Client closers


Fix packet buffer mutation


midway various pointer bytes fixes


server cmd


Cleanup


Fix unsafe.pointer, unsub cascade bugs


Testing example


Cleanup


Fix Error nil/contains checks


Send LWT+tests


Resend unsent inFlight


Performance changes


Cleanup tests and benchmarks


Handle CleanSession


Pub/sub ACL and acks


Write Client coverage


Client Tests


Tests Cleanup


Refactor Tests


Subscribe Retain


Subscribe basic + Unsubscribe


Pubcomp


Pubrel + Pubrec


Fix Establish tests


Fix Establish test


Process Publish+Recv


Switch out bufio pools


Start processing Publish


Zero-alloc retain messages + fixes


Zero-alloc topics


Alloc free subscribers


Topics interface


Deprecate particle bucket subscribers


Trie subscribers tree


Start processing packets


Update more tests


Update more tests


Refactor Clients into Server


Refactor packets/parser to take bufio rw


Add bufio rw pools


Refactor Client read to Server


Refactor fixedheader


Auth Controllers and listener options


Client Tests


Refactor MockNetConn


Add auth controller interface


Refactor Listener into Listen()


Decode a Connect packet on connection


Divest Validation from Parser


Cleanup Packets tests


Adds Mock net.Conn, errors for establisher


Refactor listeners for performance


Reworking listeners


Error strings to errors


Remove limiter


Add Benchmarks and tests


Add README


Cleanup


alloc free encoding


Convert all packet processes to byte.buffers


Benchmarks


Cleanup


New Packets library and new benchmarks


Initial commit
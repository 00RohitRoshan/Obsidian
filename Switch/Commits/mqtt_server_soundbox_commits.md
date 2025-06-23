# Unique Commit Messages for 'mqtt_server_soundbox'

  If the Session Expiry Interval is absent the value 0 is used. If it is set to 0, or is absent, the Session ends when the Network Connection is closed.
  dependency-type: indirect
 added api call part for onconnect and disconnect
"Atomic load" followed by "atomic store" is not itself an atomic
#	server/internal/clients/clients.go
# Conflicts:
#173.
#78 storage hook should not execute the relevant code if the client has been reconnected (#198)
* Add Client Closed
* Add Clone using atomic operations
* Add Github Actions Workflow
* Add Ignore Packet, tests
* Add Inline Client as a server option
* Add OnRetainPublished hook
* Add PublishDropped
* Add Server.inlineClient and Temporarily removing test cases for better code review readability.
* Add Test
* Add TestScanSubscribersTopicInheritanceBug test
* Add a Chinese version of the README.md.
* Add a Japanese version of README.md
* Add benchmark for bufpool
* Add comments to particle.inlineSubscriptions and modify to return ErrTopicFilterInvalid when the topic is invalid during subscription.
* Add debug log level to Redis example
* Add healthcheck listener
* Add leveler example
* Add retainMessage to LWT to properly handle message retention if specified in connect
* Add slog
* Add some error logging in Listener.Serve().
* Add test for publishToClient acl unauthorized
* Add test with # for TestScanSubscribersShared
* Add vendor to gitignore
* Add will retain flag on missed test
* Added a few test cases.
* Added validation checks for the legality of the client during Subscribe and Unsubscribe.
* Added validation checks for the legality of the inline client id during Subscribe and Unsubscribe.
* Adding client.ClearExpiredInflights() to clear expired messages, while client.ClearInflights() is used to clear all inflight messages.
* Addressing the issue of numeric overflow with expiration values.
* After unsubscribing, if there are other subscriptions in particle.inlineSubscriptions, particle cannot be deleted.
* Allow 0 byte usernames if correctly formed
* Allow 0 byte usernames if correctly formed
* Allow publish error returns as acks
* Another code implementation for Inline Client Subscriptions.
* Apply gofmt -s to simplify code
* Begin adding new slog calls
* Begin change of LogAttrs to standard logging interface
* Begin removing references to zerolog
* Call cl.Stop() to cancel the context, update cl.State with information such as disconnected time, and set the stopCause.
* Change default pool not to have size cap
* Change location of server.Close() and add logs to example/hooks
* Change references of err.Error() to err in slog
* Change the rest of LogAttrs to default
* Change to 1.21 to remove x dependency
* Change where server.Close() occurs in main
* Changed the return value types of Server.Unsubscribe() and Subscribe() to boolean.
* Cleanup comments
* Correct some translation errors.
* Create new server for eery test case
* Differentiate the handling of 'expire' in MQTTv5 and MQTTv3; skip expiration checks if MaximumMessageExpiryInterval is set to 0; optimize code and test cases.
* Disconnect or return ack if unauthorized publish
* Do not retain messages if retain is not available
* Dynamic write buffer
* Dynamically allocate buffer for writes if needed
* Enforce Server Maximum Packet Size on client read
* Ensure client WriteLoop is closed
* Ensure msg doesn't exceed subscription QoS
* Ensure sharedSubscription are gathered
* Ensure to close client WriteLoop
* Fix Unsubscribe for sharedSub and optimization
* Fix args order in tests
* Fix bad import in README example
* Fix bad log
* Fix err formatting issue
* Fix formatting
* Fix issue #346
* Fix misspelling
* Fix possible NextPacketID endless loop, expand tests
* Fix server option example
* Fix tests
* Fix typos
* Fixed some test case failures caused by adding inlineClient to the server.
* Fixed the TestServerSubscribe/invalid_client_id test case failure.
* Fixed unit tests
* Forward retained flag if publish is from subscribe action
* Handle expired clients in server.loadClients().
* Implementing the delivery of retained messages and supporting multiple callbacks per topic using different inline client IDs.
* Initial completion of all translations.
* Keep in sync server.System.Inflight
* Lock Hooks on Add Hook
* Minimize client lock duration
* Modify it to handle cases where the MaximumMessageExpiryInterval is set to 0 or math.MaxInt64 for no expiry, and optimize some of the code and test cases.
* Modify server.go: When used as a publisher, treat the qos of inline client-published messages as 0.
* More test cases have been added.
* Moving go cl.WriteLoop() out of NewClient() and placing it in server.attachClient().
* No need to call s.Clients.Delete().
* Only use RetainAsPublished for v5 clients
* Only when server.Options.Capabilities.MaximumMessageExpiryInterval is set to math.MaxInt64 for no expiry.
* Optimise Capabilities struct alignment
* Optimization of test case code.
* Optimize NextPacketID
* Optimize code.
* Optimize some aspects
* Optimize some aspects.
* Optimize the code to make it easier to understand.
* Pool doesn't guarantee value between Put and Get
* Publish: Set the retain flag in the fixedheader
* Reduce double write of pk.Payload
* Refinement of translations.
* Remove Travis CI
* Remove error logging for TCP listener Accept() calls.
* Remove missed removal of Error() references for logging
* Remove unused net.Buffer
* Remove vendor folder
* Removed final references to zerolog
* Replace fanpool with client write buffers
* Resolve conflict.
* Return bytes written to buffer instead of conn
* Set MaximumMessageExpiryInterval to 0 or math.MaxInt64 for no expiration, and optimize some of the code and test cases.
* Set prev connection to isTakenOver on CleanSession
* Skip OnRetainPublished if publish error
* Skip expire cleanup for isTakenOver session
* Small formatting/style changes for filter existed
* Sub a/b should not receive msg for a/b/c...
* There is no need to verify whether 'maximumExpiry' is 'math.MaxInt64' within 'client.ClearInflight()
* This is the more accurate and correct address of the listener
* Unit test for Clone
* Unsub with lower case in TestUnsubscribeShared
* Update
* Update
* Update README example to better match other examples
* Update badger.go
* Update badges for build status, coverage, report card, doc reference
* Update bolt.go
* Update clients_test.go
* Update improper comments
* Update redis.go
* Update references to 1.21
* Update server.go
* Update server.go
* Update storage_test.go
* Update system.go
* Use *packets.Packet for outbound chan
* Use *packets.Packet for outbound chan
* Use Atomic instead of RWMutex for Hooks concurrency
* Use JSONeq to compare JSON
* Use OnQoSDropped hook instead of onInflightExpired
* Use context to exit WriteLoop
* Use math constants
* Use memory pool for packet encode
* Use sysinfo.Clone
* Useful if you want to listen on port 0 to dynamically create
* Using server.inlineClient in server.InjectPacket().
* When MaximumMessageExpiryInterval is set to 0, it should not affect the message's own expiration(for v5) evaluation.
* WriterSize parameter is incorrectly set
* add jp link
* add test cases for coverage decrease
* fix expiry handling of clearExpiredInflights
* fix issue
* fix issue of unit test
* fix typo in README.md
* fix typos, indicate unused returns
* fix when no max msg expiry interval is set
* fixed ErrReceiveMaximum(receive maximum exceeded)
* improve transport performance with bufio
* invalid config type provided
* optimize code
* rename README_CN.md to README-CN.md
* reset receive quota
* retain should be delivered as false in v3
* storage hook should not execute the relevant code if the client has been reconnected #78
* test all files for coverage
* update README-CN.md
* use actions for all pull requests and pushes
- [Commits](https://github.com/golang/net/commits/v0.7.0)
- [Commits](https://github.com/golang/net/compare/v0.7.0...v0.17.0)
- [Release notes](https://github.com/golang/net/releases)
- dependency-name: golang.org/x/net
---
---------
...
8bit align struct fields
ARM32 Compatibility
Abandon client state if the existing client specified a cleansession
Abandon inflights at the end of clean-session connections
Add  .gitignore
Add .DS_Store to ignore list
Add AllowClients Field to packets
Add AllowClients check in publishToSubscribers
Add AllowClients field to packets
Add Benchmarks and tests
Add CleanSession and Username to events.Client struct
Add Client Closed (#130)
Add Clone to system.Info (#163)
Add Docker info
Add ErrRejectPacket error to abandon packet processing from OnMessageProcess
Add ErrRejectPacket to OnProcessMessage
Add Event Hooks
Add Events
Add Healthcheck listener
Add InSliceString function
Add Keyed fields to events.Client for readability and go vet
Add OnConnect and OnDisconnect hooks to example
Add OnConnect event hook
Add OnDisconnect Event Hook
Add OnPacketIDExhausted hook (#211)
Add OnRetainPublished hook (#237)
Add OnSessionEstablish hook (#247)
Add OnSubscribe, OnUnsubscribe events examples
Add PublishDropped metrics (#167)
Add README
Add Server Options
Add TLSConfig field to allow direct tls.Config setting
Add TravisCI
Add a Chinese version of README.md. (#307)
Add a Japanese version of README.md (#338)
Add a demonstration in examples/hooks on how to subscribe to a topic and publish messages directly within the hook. (#333)
Add an OnError handler; report the reason for disconnects. (#38)
Add auth controller example
Add auth controller interface
Add badges
Add bufio rw pools
Add comments
Add example for AllowClients field
Add example implementation
Add healthcheck listener (#244)
Add inline publishing example
Add lock to client writes (#212)
Add missing method comments
Add newline for godoc formatting
Add packet ID exhausted hook (#217)
Add retainMessage to LWT to properly handle message retention (#234)
Add setupServerClients to inherit existing server instance
Add some error logging in Listener.Serve(). (#303)
Add test for AllowClients field
Add testbolt file to ignore list
Add tests for InSliceString
Add tests for OnConnect, OnDisconnect
Add tests for new inline publishing method
Add the OnUnsubscribed hook to the unsubscribeClient method
Add the OnUnsubscribed hook to the unsubscribeClient method (#122)
Add the OnUnsubscribed hook to the unsubscribeClient method，and change the unsubscribeClient to externally visible. In a clustered environment, if a client is disconnected and then connected to another node, the subscriptions on the previous node need to be cleared.
Add topic un-/subscribe events
Add unix socket listener
Adds Inflight TTL and Period Resend
Adds Mock net.Conn, errors for establisher
Adds Retained Delete
Adds TLS/SSL
Adds a new struct of server options which can be used to override default properties. A new options-accepting NewServer function has been created to supersede the New method, which is now deprecated.
Adds an example file which demonstrates the usage of the `Publish` method. This file will also be used to demonstrate event hooks.
Adds basic event hooks (OnMessage, OnMessageModify) to the server using the new events library.
Adds delete from persistence
Adds information about direct publishing and moves performance section
Adds more persistence tests
Adds tests for publishing event hooks
Adjust the validation order of the processSubscribe method to ensure that it fails quickly if there is an error, since s.hooks. OnACLCheck generally takes a long time.
All working
Alloc free subscribers
Allow 0 byte usernames if correctly formed (#181)
Allow Publish to return custom Ack error responses (#256)
AllowClients field can be specified during onMessage event to selectively deliver messages
Another code implementation for Inline Client Subscriptions. (#284)
Auth Controllers and listener options
Avoid race condition when closing listeners
AwaitCapacity tests
AwaitFilled
Basic $SYS stats
Benchmarks
Bolt 1.3.6 fails to build correctly and has been removed, so rollback to bolt 1.3.5. Also upgrade to Go 1.18
Bump golang.org/x/net from 0.0.0-20220927171203-f486391704dc to 0.7.0 (#182)
Bump golang.org/x/net from 0.7.0 to 0.17.0 (#316)
Bumps [golang.org/x/net](https://github.com/golang/net) from 0.0.0-20220927171203-f486391704dc to 0.7.0.
Bumps [golang.org/x/net](https://github.com/golang/net) from 0.7.0 to 0.17.0.
Call OnConnect Event if applicable
Call OnDisconnect Event if applicable
Change inline check order (#133)
Changing "data" to "key" or "id" here might be more appropriate.
Charts
Check against the correct clean session var for abandoning old inflights
Check for protocol violation errors
Check if a slice of strings contains a string (until slices package available)
Clarify error messages
Cleanup
Cleanup Packets tests
Cleanup TCP Listener
Cleanup godoc formatting
Cleanup tests and benchmarks
Cleanup, Tests fix, Client closers
Cleanup, start reader/writer model
Client Tests
Client write buffers (#165)
Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Co-authored-by: Derek Duncan <dduncan@atlassian.com>
Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: Derek Duncan <derekduncan@gmail.com>
Co-authored-by: Dominic Plourde <plourded@amotus.ca>
Co-authored-by: Gabriel Sagula <gsagula@magicleap.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: JB <28275108+mochi-co@users.noreply.github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Co-authored-by: hector.oliveros@wabtec.com <hectoroliveros@MacBook-Pro-de-Hector.local>
Co-authored-by: mochi <mochimou@icloud.com>
Co-authored-by: mochi-co <moumochi@icloud.com>
Co-authored-by: sukvojte <sukvojte@gmail.com>
Co-authored-by: thedevop <60499013+thedevop@users.noreply.github.com>
Co-authored-by: unknow <beunknow@outlook.com>
Co-authored-by: werben <werben@aliyun.com>
Co-authored-by: werben <werben@qq.com>
Co-authored-by: werbenhu <werben@qq.com>
Code and Comments cleanup, vendor deps
Combines two fixes
Configurable Server Options
Configurable client bufio reader/writer sizes (#190)
Connect ReturnResponseInfo only applies to Connack values (#128)
Contributions paused pending v2.0.0
Convert all packet processes to byte.buffers
Correct function signature
Correctly identify and clean taken-over sessions (#180)
Correctly return R value of retainMessage
Correctly validate WillProperties (#210)
Debug func, better closers
Decode a Connect packet on connection
Deprecate particle bucket subscribers
Directly publish messages from embedding system
Disconnect or return ack if unauthorized publish (#292)
Divest Validation from Parser
Do not retain messages if retain is not available (#261)
Don't receive $SYS retained on #
Dont inflight secondary qos flow messages
Dynamically allocate write buffer if needed. (ready for merge) (#324)
Emit warning if client keepalive is less than recommended minimum (#305)
Enforce server max packet (#121)
Ensure OnError is set before using it
Ensure msg doesn't exceed subscription QoS (#253)
Ensure to close client WriteLoop (#193)
Ensure we're not committing any binaries
Error strings to errors
Errors in the hook when doing a publish were ignored. This caused that test cases could not be made where the publish failed and an error was thrown.
Establish Tests
Events library contains event hook types and related utility functions
Events: Add OnProcessMessage event
Expect correct r values for RetainMessage
Expire session if SessionExpiryInterval is 0 (#216)
Export R/W buffer values so they can be assessed in tests without causing races
Expose CleanSession value for checking
Expose SendConnack, err return on OnConnect (#240)
Expose dropped publish messages count in sys info (#170)
Expose packets library
Expose tls.Config to Listeners
Extend onsusbcribe, onunsubscribe events
Feature/event hooks publish
Fields of the packet get evaluated.
Fix CheckEmpty
Fix Error nil/contains checks
Fix Establish test
Fix Establish tests
Fix Inflight Persistence Key
Fix ScanSubscribersTopicInheritanceBug (#243)
Fix Store Retained Messages
Fix Typos
Fix badges
Fix close sequence, update test coverage
Fix code block formatting
Fix concurrent map access for clients and inflights causes data race 
Fix data race issue with write buffer (#347)
Fix docker repo name
Fix encodeLength for 32-bit platforms
Fix example imports
Fix example usage of NewHTTPStats (#231)
Fix examples
Fix for unlimited maximum message expiry interval (#315)
Fix incorrect test
Fix mis-typed onpublished hook, update version, fanpool defaults
Fix packet buffer mutation
Fix potential NextPacketID endless loop, expand tests (#169)
Fix readme example (#276)
Fix test races
Fix tests
Fix typo
Fix unsafe.pointer, unsub cascade bugs
Fix websocket malformed packet bug
Fix websocket reads for packets > 1 buffer size (#260)
Fixed some bugs, wish the project better and better
Fixes sync.cond deadlock
For fields that may hold large numeric values, padding has been added to
Goreport fixes
Handle CleanSession
Handle expired clients in server.loadClients(). (#341)
Http Sys Stats listener
If AllowClients has been set on a packet, ensure only clients in the slice are sent the message
If SessionExpiryInterval was not set in CONNECT, SessionExpiryIntervalFlag is also not set. According to spec:
Ignore retain as published v3 (#142)
Image test
Improve 32-bit compatibility
Include a listener accepting an existing net.Listener (#155)
Increase inlinepub messages buffer
Increment server version
Increment server version to 1.0.1
Indicate translators wanted
Inflght and retained messages persistence
Initial commit
Initial commitInitial commitlatest code for csc
Initial commitadded pubsub
Initial commitcabank prod code
Initial commitchanged certs
Initial commitchanged ssl certs
Initial commitchanged username , psswrd for uat bob
Initial commitinitial commit
Initial commitmade changes in http
Initial commitno ssl code added
Initial commitplaystatus 1 client
Initial commitproduction code
Inline Publishing
Instead of waiting for the writing buffer to have enough space, skip writing and return an error
Iobuffers
Keep in sync server.System.Inflight (#92)
LWT and Validate packet
Load persistence into server
Lock on close outbound (#213)
Make atomics work on 32-bit systems
Make hooks safe for concurrency (#139)
Merge OnMessage and OnMessageModify
Merge branch 'iobuffers'
Merge branch 'master' into bugfix/ws_malformed_package
Merge branch 'master' into master
Merge branch 'master' of https://github.com/mochi-co/mqtt into v1.1.2
Merge branch 'mochi-co:master' into fix/writer-full
Merge branch 'mochi-co:master' into master
Merge branch 'packetchange' of https://gitlab.iserveu.tech/soundbox/mqtt_server_soundbox into pubsub
Merge branch 'restructure-paths'
Merge branch 'v1.2.0' of https://github.com/mochi-co/mqtt into fix-store-retained
Merge pull request #1 from mochi-co/iobuffers
Merge pull request #10 from mochi-co/expose-packets
Merge pull request #11 from mochi-co/feature/event-hooks-publish
Merge pull request #116 from tommyminds/bugfix/ws_malformed_package
Merge pull request #119 from mochi-co/fix-on-published
Merge pull request #12 from jphastings/remove-erroneous-print
Merge pull request #123 from wind-c/master
Merge pull request #124 from zgwit/master
Merge pull request #14 from mochi-co/feature/allow-clients-value
Merge pull request #15 from ClarkQAQ/master
Merge pull request #18 from mochi-co/feature/connect-disconnect-hooks
Merge pull request #19 from rkennedy/bugfix/32-bit-atomic-alignment
Merge pull request #22 from mochi-co/feature/32bit-compatibility
Merge pull request #24 from mochi-co/feature/optimise-struct-fields
Merge pull request #26 from wind-c/master
Merge pull request #27 from mochi-co/revert-26-master
Merge pull request #29 from jmacd/jmacd/payload_not_utf8
Merge pull request #46 from stffabi/bugfix/acls-retain
Merge pull request #51 from jmacd/jmacd/noracefix
Merge pull request #53 from stffabi/feature/onprocessmessage-event
Merge pull request #57 from hybridgroup/v1.2.0-docker
Merge pull request #58 from soyoo/patch-1
Merge pull request #61 from mochi-co/server-options
Merge pull request #62 from mochi-co/fix-inflight-key
Merge pull request #63 from mochi-co/add-drop-packet-error
Merge pull request #67 from mochi-co/release-client-buffers
Merge pull request #68 from mochi-co/fix-store-retained
Merge pull request #69 from mochi-co/v1.2.0
Merge pull request #72 from BoskyWSMFN/master
Merge pull request #74 from muXxer/feat/topic-subscription-events
Merge pull request #8 from mochi-co/feature/inline-publish
Merge pull request #82 from mochi-co/expose-event-client-username
Merge pull request #83 from mochi-co/tls-client-auth
Merge pull request #84 from mochi-co/goreport-fixes
Merge pull request #90 from mochi-co/resend-inflights
Merge pull request #97 from alexsporn/fix/writer-full
Merge pull request #99 from mochi-co/fix-inflight-race
Merge remote-tracking branch 'origin/master'
Migrate from zerolog to slog (#248)
Minimize client lock duration (#223)
More Tests
More tests, connecting MQTT
Move Parser, cleanup to basic
Move cl.WriteLoop() to attachClient() and call cl.Stop() in loadClients() to update client.State. (#344)
Move msgToPacket to storage.Message.ToPacket
Move refreshDeadline to only trigger on successful transmission (#157)
Move two WaitGroup.Add calls (#36)
New Packets
New Packets library and new benchmarks
No longer issue retained messages on session takeover (#166)
No quotas of the inflight is set in the readStore method, so each quota is equal to 0. The inheritClientSession method overrides the quotas of the new client inflight, so the processPublish method reports an ErrReceiveMaximum and disconnects the client.
Not checking if err is equal to nil
Now that we can alias types, there's no compelling reason to expose the packets library
Now when a "publish" command fails, then the publish method will throw an error (#229)
On 32-bit systems, `atomic` requires its 64-bit arguments to have 64-bit
OnConnect and OnDisconnect Event Hooks
Optimise Struct Fields + Fixes
Optimize inflight expiry (#127)
Optionally drop a packet if the ErrRejectPacket error is returned from OnProcessMessage
Packet encoding optimization (#343)
Pass Paho Tests
Pass inflight by address to avoid lock copying
Performance changes
Periodic Resend of Inflight messages
Persistence V1
Persistence and tests
Preference Write, Read, Deny filters in ledger (#262)
Prevent locks being copied by passing non-pointer to FromClient
Prevent locks from being copied
Process Publish+Recv
Process packets
Processor Read and Tests
Progress on persistence
Protect close of nil outbound channel
Pub/sub ACL and acks
Pubcomp
Publish
Publish $SYS Stats to topics
Publish retained messages only after connack (#147)
Publish: Set the retain flag in the fixedheader (#42)
Pubrel + Pubrec
Read+Read Test
ReadFrom IO
Rebuild
Rebuilding
Refactor Client read to Server
Refactor Clients into Server
Refactor Listener WG to track clients (#301)
Refactor Listener into Listen()
Refactor MockNetConn
Refactor Tests
Refactor establishconnection to prevent same-id disconnects
Refactor fixedheader
Refactor listeners for performance
Refactor packets/parser to take bufio rw
Refactor stored subscription value assignments
Refactor, fixes to Circ Peek, start processor/parser
Release client buffers
Remove Codacy badge
Remove limiter
Remove unnecessary fmt import
Remove unnecessary println
Remove unnecessary type declarations
Remove unused code
Remove vendor folder (#319)
Rename Quota methods for clarity (#159)
Replace Travis with Github Actions (#41)
Resend unsent inFlight
Resort Charts
Restructures code
Retain flag should be delivered as false in v3 (#257)
Return copies of client and inflight maps to avoid missed locks
Return packets to internal
Revert "Merge pull request #97 from alexsporn/fix/writer-full"
Revert "added redis persistence mode"
Revert "added worker pool"
Revert "improve transport performance with bufio (#321)" (#323)
Revert server version
Reworking listeners
Rewrite everything from scratch for mqtt v5
Satisfy 4.7.2 - restrict $ topics
Satisfy Keepalive, fix Keepalive 0
Save subscription properties for mqttv5 (#131)
Save the subscription properties for mqqtv5
Send LWT+tests
Signed-off-by: dependabot[bot] <support@github.com>
Simplified code (#195)
Simplify Client construction, add NewClient method to Server, add Publish convenience method
Simplify the code for the loadInflight and loadRetained methods.
Skip expire cleanup for isTakenOver session (#183)
Small code improvements
Small fix
Small fixes
Small fixes and cleanups (#295)
Small language clarification for non-english
Small style fix
Start on Peek
Start processing Publish
Start processing packets
Store retained message based on corrected r value
Subscribe Retain
Subscribe basic + Unsubscribe
Subscribe: Only send retained messages if ACLs has allowed subscription to the topic
Support non-UTF8 payloads (per MQTT specification)
Support non-UTF8 payloads per MQTT specification
Switch out bufio pools
Testing example
Tests Cleanup
Tests and buffer sizes
The WriterSize parameter is incorrectly set in the newClient method.
The WriterSize parameter is incorrectly set in the newClient method.
The previous publish inline test incorrectly approved retain packets without retain=true fixedheader values.
The s.hooks.OnQosPublish method needs to be called, otherwise the following s.hooks.OnQosComplete or processPuback(s.hooks.OnQosComplete) method will report a data not found error.
The variable existed can be changed repeatedly within a for loop. An array variable must be used to record the subscription of each filter.
This ensures that test results pass even if the field order is inconsistent.
This event gets called right after ACL checking but before any other
This reverts commit 8e52e49b94026c3380b8c2cacce22fc565858cc7.
This reverts commit f22b8276e8c33c1e34f941beb5d59667bbda9de6, reversing
Topics interface
Track number of pool blocks in use
Trie subscribers tree
Two no-functional-change cleanups combined
Update Badges
Update Chart Labels
Update Contribution Guidelines
Update EstablishConnection tests to ensure buffers and pool are correctly released after use
Update Hooks List
Update OnProcessMessage documentation
Update README
Update README, better command main
Update README.md
Update README.md new benchmarks
Update Readme
Update Readme to add Event Hooks section
Update SPDX annotations
Update Server Version
Update badges to use v2 references
Update build.yml
Update build.yml (#203)
Update code to use new NewServer function instead of deprecated New
Update codes.go (#214)
Update codes.go (#215)
Update comment for clarity
Update comments and rename input parameter for clarity
Update comments for clarity
Update events example with publish hooks
Update example code to use new NewServer function instead of deprecated New
Update for OnConnect and OnDisconnect hooks
Update go mod and imports to v2
Update go mod to 1.17
Update go mod to ensure bolt is using 1.3.5
Update go to 1.17
Update go.mod
Update more tests
Update readme
Update readme and server version
Update readme v2.4.0
Update readme with server options
Update server version
Update server version to 1.0.5
Update test to check for packet rejection
Update test to match new FixedHeader struct
Update travis
Update vendor
Update version number
Update version to 1.1.0
Update with direct publishing
Use *packets.Packet for outbound chan (#176)
Use Atomic instead of RWMutex for Hooks concurrency (#148)
Use JSONeq to compare JSON (#267)
Use context to exit WriteLoop (#222)
Use context to signal client open state (#218)
Use correct connack return codes for MQTTv3 (#140)
Use defer to release buffers and decrease stats on any client closure
Use internal default values instead of relying on passed value
Use package errors instead of strings
V1.2.0
Variable existed in the method processSubscribe is unstable
Websocket Listener
When `int` is 32 bits, `MaxInt64` doesn't fit. It's apparent that
When the broker is embedded in a larger Go codebase, it is beneficial to be able to publish messages directly from the system to topics. This change provides a Publish method which adds messages to an inline publishing queue in a separate goroutine, which are then processed in the standard way and issued to all clients with matching topic filters.
Working wait logic
Wrap packet errors with cause information (#39)
Write Bytes
Write Client coverage
WriteTo / Tests
WriterSize parameter is incorrectly set (#252)
Zero-alloc retain messages + fixes
Zero-alloc topics
_ time
`encodeLength` expects to handle 64-bit inputs, so let's make that
accept any error for invalid protocol due to races
add aclcheck in publishToClient (#287)
add redis persistence mode and example
add test cases for coverage decrease
add tests for new NewServer function
added api call for publish and call_back
added auth and tls part
added code for bob
added log part for onconnect and disconnect
added redis persistence mode
added sleep
added time stamp for asia location
added worker pool
alignment, but the compiler doesn't help ensure that's the case. In this
alloc free encoding
alternative tags attempt
apply gofmt -s
bytes buffer to pool
cabank prod code
change scheduled message for clarity
changed certs for bob_uat
changed certs to add uat domain
changed ssl certs
changed type for update api
changed uname and password
changed username , psswrd for uat bob
changes made to b2fc287a9885a94d14f394d84216d123220ab9d5.
clarify error checking
cleanup
clear buffers after deferred stop
client write packet
commit, fields that don't need to hold large numbers have been converted
convert tabs to spaces
docker: add initial simple Dockerfile
error handling txn insert
examples/persistence/bolt/main.go: invalid config type provided
explicit, which allows the test to run on all platforms.
export client.Net.Conn for external use
expose packets library
failed to delete inflight data (#162)
feat: return tcp.Address from listener, if exists (#336)
fix [ST1005] strings should not be capitalized
fix code indents
fix comments
fix grammar on Closed method doc
fix indentation in code blocks
fix inflight key reference
fix local variable black hole
fix onmessage test
fix typo
fix-panic
fix: common subscriptions issued by different clients at the same time may be lost (#186)
fix: correct decoding of packets including Properties exceeding 127 bytes in length (#172)
fix: fix data-race in badger hook (#266)
fixed runtime panic in server/internal/circ/pool.go occurring on 32-bits architectures caused by misalignment of BytesPool struct members.
get the necessary alignment, and tests have been added to avoid
https://github.com/golang/go/issues/36606#issue-551005857
improve transport performance with bufio (#321)
increment server version
indicate ARM32 compatibility
initial commit
insert transaction api call
instead.
invalid config type provided (#152)
listeners (think of unit/integration tests)
made changes for prod bob
made changes in http
method UnsubscribeClient's packet add fixedHeader (#264)
midway various pointer bytes fixes
migrate imports, copyrights, etc (#270)
multiple platforms
only build docker on tag for mochi-mqtt repo
only check final outcome due to races
operation. This commit replaces that sequence with CompareAndSwap
optimise Server struct
optimise api call
packet change
pass byte pool by address
playstatus 1 client
pre-refactor
previously new clients generated a new server object, so system stats were not shared. This change ensures all test clients use the same server
printing information for ID or error is missing.
production code
receive quota should be reset across connections (as specified in the spec).
redis and trie
refactor clients for buffer releasing
refactor connSetup for clarity
refactor pointers
refactor server keepalive for hook access (#220)
regressions.
remove deprecated log message
remove ineffective assignments
remove println
remove redundant code
revert redis update
revert server version
rm go routine in onpacketread
server cmd
start establish 
test clarbuffers
test push to docker with version
test pushing directly to docker
to 32-bit types, which are always aligned correctly on all platforms.
track logged error
tttt reverts commit 82fd5667c5419ac5b3efea31bd2d7d46f14866e0.
typo
update README-CN.md (#312)
update TLS example to use TLSConfig field
update github workflow go version to 1.19
update mock.go plase use range
update packets library import reference
update readme for new events
update server version
update tcp.go maybe this will be better
update tests
update websocket.go fix check origin
updated-dependencies:
updated_time
use .systemInfo instead of .system for clarity
use NewServer instead of New
use TLSConfig instead of deprecated TLS field
working but bottlenecks

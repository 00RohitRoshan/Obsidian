golang Grpc interview questions at MAANG 


ChatGPT said:
Here is a list of Go (Golang) gRPC interview questions that are commonly asked or expected in technical interviews at MAANG companies (Meta, Apple, Amazon, Netflix, Google), especially when the role involves microservices, backend systems, or distributed architectures:

🚀 Core gRPC Concepts
What is gRPC and how does it work?

Can you explain how gRPC uses HTTP/2 and Protocol Buffers?

Why is gRPC preferred over REST in certain applications?

Explain the gRPC lifecycle in Go.

How does a gRPC request flow from client to server?

What is a .proto file?

What are services, messages, and RPC methods in a .proto file?

How is gRPC different from REST?

Compare gRPC and REST in terms of performance, code generation, streaming, etc.

📦 Practical Usage in Golang
How do you define a gRPC server in Go?

What packages do you import?

How do you register services?

How do you generate Go code from .proto files?

What is protoc? What plugins are needed for Go?

How do you implement a gRPC client in Go?

How do you create a connection and make a request?

Explain Unary vs Streaming RPCs in Go.

What are client-side streaming, server-side streaming, and bidirectional streaming in gRPC?

How do you handle deadlines/timeouts in gRPC with Go?

How does context propagation work?

How do you secure gRPC services in Go?

TLS/SSL setup?

Authentication and authorization?

🧠 Advanced Topics
How would you implement middleware/interceptors in gRPC with Go?

UnaryInterceptor vs StreamInterceptor

Logging, metrics, tracing

How do you do error handling in gRPC?

What are status and codes packages used for?

Custom error propagation

Explain how to do service discovery with gRPC in Go.

How can you integrate with Consul or etcd?

Use of grpc.Dial with load balancing

How do retries and backoff work in gRPC?

Configuring retry policies in the client

What are reflection and health checks in gRPC?

Use of grpc-health-probe or grpc_reflection_v1alpha

🛠️ System Design / Architecture-Level Questions
Design a microservice using gRPC that handles file uploads and downloads.

Would you use streaming or unary RPC?

How would you handle large files?

How do you make a gRPC service backward compatible?

Adding/removing fields in .proto

Versioning strategies

How would you monitor and trace gRPC calls across services?

Use of OpenTelemetry / Jaeger / Prometheus

How would you test a gRPC service in Go?

Unit testing

Integration testing with test servers

How would you scale a gRPC-based service?

Load balancing (client-side, Envoy, etc.)

Kubernetes + gRPC integration

🔥 Bonus (Real-World & Behavioral)
Have you migrated a service from REST to gRPC? What were the tradeoffs?

Tell me about a time you debugged a tricky issue in a gRPC system.

How do you handle backward compatibility across teams working on different services using shared .proto definitions?

Would you like me to provide answers or sample code for any of these questions, or tailor these to a specific MAANG company (e.g., Netflix or Google)?
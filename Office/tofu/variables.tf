variable "app_name" {
  description = "Map of application names to container image paths"
  type        = list(string)
  default = ["tofuredirect","tofuauth","tofukong","tofukennethreitz"]
}


  variable "image" {
    description = "The container image to deploy with tag"
    type        = map(string)
    default = {
      tofuredirect     = "gcr.io/iserveustaging/readytodeploy-redirect-app:latest"
      tofuauth          = "gcr.io/iserveustaging/readytoddeploy-ext-authz:latest"
      tofukong          = "kong/httpbin"
      tofukennethreitz  = "kennethreitz/httpbin"
    }
  }

  variable "port" {
    description = "The container image to deploy"
    type        = map(list(number))
    default = {
      tofuredirect     = [8080]
      tofuauth          = [8000,9000]
      tofukong          = [80]
      tofukennethreitz  = [80]
    }
  }

  variable "svcType" {
    description = "The service type to expose"
    type        = map(string)
    default = {
      tofuredirect      = "LoadBalancer"
      tofuauth          = "ClusterIP"
      tofukong          = "ClusterIP"
      tofukennethreitz  = "ClusterIP"
    }
  }

  variable "env" {
    description = "env values for respective deployment"
    type    = map(map(string))
    default = {
      tofuredirect     = {SecretNameRedis:"",SecretNameMongo:"",ISSUES:"",ISSUESWHITELIST:""}
      tofuauth          = {targetURL:""}
    }
  }

variable "repo" {
  description = "Git repo URLs and branches"
  type = map(object({
    url    = string
    branch = string
  }))
  default = {
    tofuredirect = {
      url    = "https://gitlab.txninfra.com/api-gateway/api-gateway-dev/extauth-istio.git"
      branch = "ta-bbps-sdk"
    },
    tofuauth = {
      url    = "https://gitlab.txninfra.com/api-gateway/api-gateway-dev/redirect_application.git"
      branch = "sdk-redirect-deployed"
    }
  }
}


  variable "grpcprovider" {
    type = string
    default = "tofu-grpc-authprovider"
  }

  variable "project_id" {
    default = "iserveustaging"
  }

  variable "zone" {
    default = "asia-south1"
  }

  variable "region" {
    default = "asia-south"
  }

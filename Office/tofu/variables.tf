variable "app_name" {
  description = "Map of application names to container image paths"
  type        = map(string)
  default = {
    tofukong          = "kong/httpbin"
    tofukennethreitz  = "kennethreitz/httpbin"
    tofuredicrect     = "gcr.io/iserveustaging/readytodeploy-redirect-app@sha256:c9b929a54ee055ee5b23bee229907c1b1e54b2a19db81a6fefaebacd4fd4b95a"
    tofuauth          = "gcr.io/iserveustaging/readytoddeploy-ext-authz@sha256:785cd3865f9dd9a188e31caa56d7a1f595b2cf5c3727afd2436dbb1aa79b34c6"
  }
}


  # variable "image" {
  #   description = "The container image to deploy"
  #   type        = string
  #   default = "kong/httpbin"
  # }

  variable "project_id" {
    default = "iserveustaging"
  }

  variable "zone" {
    default = "asia-south1"
  }

  variable "region" {
    default = "asia-south"
  }

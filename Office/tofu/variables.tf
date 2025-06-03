variable "app_name" {
  description = "Map of application names to container image paths"
  type        = map(string)
  default = {
    kong          = "kong/httpbin"
    kennethreitz  = "kennethreitz/httpbin"
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

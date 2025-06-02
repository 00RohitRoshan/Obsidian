  variable "app_name" {
    description = "The name of the application to deploy"
    type        = list(string)
    default = ["httpbin"]
  }

  variable "image" {
    description = "The container image to deploy"
    type        = string
    default = "kong/httpbin"
  }

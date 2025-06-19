  variable "app_name" {
    type = list(string)
  }

  variable "image" {
    description = "The container image to deploy"
    type        = map(string)
  }

  variable "port" {
    type    = map(list(number))
    default = {}
  }

  variable "env" {
    type    = map(map(string))
    default = {}
  }

  variable "grpcprovider" {
    type = string
  }

  # variable "host" {
  #   type = string
  # }

  # variable "client_certificate" {
  #   type = string
  # }

  # variable "client_key" {
  #   type = string
  # }

  # variable "cluster_ca_certificate" {
  #   type = string
  # }

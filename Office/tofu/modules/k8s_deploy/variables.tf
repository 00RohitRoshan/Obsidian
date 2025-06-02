  variable "app_name" {
    type = list(string)
  }

  variable "image" {
    type = string
  }

  variable "port" {
    type    = number
    default = 80
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

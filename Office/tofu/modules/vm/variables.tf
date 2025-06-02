  variable "vm_name" {}
  variable "machine_type" {}
  variable "zone" {}
  variable "image" {}
  variable "subnet_self_link" {}
  variable "tags" {
    default = []
  }
  variable "project_id" {}

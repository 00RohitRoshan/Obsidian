  # terraform {
  #   required_providers {
  #     minikube = {
  #       source = "scott-the-programmer/minikube"
  #       version = "0.5.0"
  #     }
  #   }
  # }

  # provider minikube {
  #   # kubernetes_version = "v1.30.0"
  # }

  # resource "minikube_cluster" "cluster" {
  #   vm      = true
  #   driver  = "docker"
  #   cluster_name = "minikube"
  #   cni     = "bridge"
  #   addons  = [
  #     "dashboard",
  #     "default-storageclass",
  #     "ingress",
  #     "storage-provisioner"
  #   ]
  # }

  provider "google" {
    project     = "iserveustaging"
    # region      = "us-central1"
  }

  # module "vm" {
  #   source           = "./modules/vm"
  #   project_id       = var.project_id
  #   vm_name          = "vm-instance"
  #   machine_type     = "e2-medium"
  #   zone             = var.zone
  #   image            = "debian-cloud/debian-12"
  #   subnet_self_link = module.network.subnet_self_link
  #   tags             = ["ssh"] # Ensure firewall tag matches
  # }

  # module "network" {
  #   source       = "./modules/network"
  #   network_name = "vm-vpc"
  #   subnet_name  = "vm-subnet"
  #   subnet_cidr  = "10.10.0.0/24"
  #   region       = var.region
  # }


  module "k8s_deploy" {
    source           = "./modules/k8s_deploy"
    app_name         = var.app_name
    grpcprovider     = grpcprovider
    # image            = "${var.image}:latest"
    # host             = minikube_cluster.cluster.host
    # client_certificate = minikube_cluster.cluster.client_certificate
    # client_key         = minikube_cluster.cluster.client_key
    # cluster_ca_certificate = minikube_cluster.cluster.cluster_ca_certificate
  }

  # module "vm" {
  #   source           = "./modules/vm"
  #   project_id       = var.project_id
  #   vm_name          = "vm-instance"
  #   machine_type     = "e2-medium"
  #   zone             = var.zone
  #   image            = "debian-cloud/debian-12"
  #   subnet_self_link = module.network.subnet_self_link
  #   tags             = ["ssh"] # Ensure firewall tag matches
  # }

  # module "network" {
  #   source       = "./modules/network"
  #   network_name = "vm-vpc"
  #   subnet_name  = "vm-subnet"
  #   subnet_cidr  = "10.10.0.0/24"
  #   region       = var.region
  # }


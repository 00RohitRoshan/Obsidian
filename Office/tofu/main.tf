  terraform {
    required_providers {
      minikube = {
        source = "scott-the-programmer/minikube"
        version = "0.5.0"
      }
    }
  }

  provider minikube {
    # kubernetes_version = "v1.30.0"
  }

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

  module "k8s_deploy" {
    for_each = var.app_name
    source           = "./modules/k8s_deploy"
    app_name         = var.app_name
    image            = "${var.image}:latest"
    # host             = minikube_cluster.cluster.host
    # client_certificate = minikube_cluster.cluster.client_certificate
    # client_key         = minikube_cluster.cluster.client_key
    # cluster_ca_certificate = minikube_cluster.cluster.cluster_ca_certificate
  }


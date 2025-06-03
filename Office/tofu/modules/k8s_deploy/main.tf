  # Retrieve an access token as the Terraform runner
  data "google_client_config" "provider" {}

  data "google_container_cluster" "my_cluster" {
    name     = "cluster-1"
    location = "asia-south1"
  }

  provider "kubernetes" {
    host  = "https://${data.google_container_cluster.my_cluster.endpoint}"
    token = data.google_client_config.provider.access_token
    cluster_ca_certificate = base64decode(
      data.google_container_cluster.my_cluster.master_auth[0].cluster_ca_certificate,
    )
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      command     = "gke-gcloud-auth-plugin"
    }
  }

  
  # provider "kubernetes" {
  #   host                   = var.host
  #   client_certificate     = var.client_certificate
  #   client_key             = var.client_key
  #   cluster_ca_certificate = var.cluster_ca_certificate
  # }

  # provider "kubernetes" {
  #   config_path = "~/.kube/config"
  # }

  resource "kubernetes_deployment" "app" {
    for_each = var.app_name
    metadata {
      name = each.key
      labels = {
        app = each.key
      }
    }

    spec {
      replicas = 2
      selector {
        match_labels = {
          app = each.key
        }
      }
      template {
        metadata {
          labels = {
            app = each.key
          }
        }
        spec {
          container {
            name  = each.key
            image = each.value
            image_pull_policy = "Always"
            port {
              container_port = var.port
            }
          }
          
        }
      }
    }
  }

  # resource "kubernetes_service" "hello" {
  #   for_each = var.app_name
  #   metadata {
  #      name = each.key
  #   }
  #   spec {
  #     port {
  #       port = 8080
  #       target_port = 80
  #     }
  #     selector = {"app" : each.key}
  #   }
  # }


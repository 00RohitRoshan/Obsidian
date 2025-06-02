  # provider "kubernetes" {
  #   host                   = var.host
  #   client_certificate     = var.client_certificate
  #   client_key             = var.client_key
  #   cluster_ca_certificate = var.cluster_ca_certificate
  # }

  provider "kubernetes" {
    config_path = "~/.kube/config"
  }

  resource "kubernetes_deployment" "app" {
    for_each = var.app_name
    metadata {
      name = each.value
      labels = {
        app = each.value
      }
    }

    spec {
      replicas = 2
      selector {
        match_labels = {
          app = each.value
        }
      }
      template {
        metadata {
          labels = {
            app = each.value
          }
        }
        spec {
          container {
            name  = each.value
            image = var.image
            image_pull_policy = "Never"
            port {
              container_port = var.port
            }
          }
          
        }
      }
    }
  }

  resource "kubernetes_service" "hello" {
    for_each = var.app_name
    metadata {
       name = each.value
    }
    spec {
      port {
        port = 8080
        target_port = 80
      }
      selector = {"app" : each.value}

    }
  }


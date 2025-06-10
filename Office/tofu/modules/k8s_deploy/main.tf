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
            image = var.image[each.value]
            image_pull_policy = "Always"
            dynamic "port" {
              for_each = var.port[each.value]
              content {
                container_port = port.value
              }
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
      dynamic "port" {
        for_each = var.port[each.value]
        content {
          port        = port.value
          target_port = port.value
        }
      }
      selector = {"app" : each.value}
      type = "LoadBalancer"
    }
  }

resource "kubernetes_manifest" "istio_auth_policy" {
  manifest = {
    apiVersion = "security.istio.io/v1beta1"
    kind       = "AuthorizationPolicy"
    metadata = {
      name      = "allow-public-get"
      namespace = "default"
    }
    spec = {
      selector = {
        matchLabels = {
          app = var.app_name[0]
        }
      }
      action = "CUSTOM"
      provider = var.grpcprovider
      rules = [ 
        {
          # to = [
          #   {
          #     operation = {
          #       methods = ["*"]
          #       paths   = ["*"]
          #     }
          #   }
          # ]
        },
        {}
      ]
    }
  }
}

# resource "kubernetes_config_map" "istio_mesh_config" {
#   metadata {
#     name      = "istio"
#     namespace = "istio-system"
#     labels = {
#       install.operator.istio.io/owning-resource            = "installed-state"
#       install.operator.istio.io/owning-resource-namespace  = "istio-system"
#       istio.io/rev                                         = "default"
#       operator.istio.io/component                          = "Pilot"
#       operator.istio.io/managed                            = "Reconcile"
#       operator.istio.io/version                            = "1.20.1"
#       release                                              = "istio"
#     }
#   }

#   data = {
#     mesh = yamlencode({
#       defaultConfig = {
#         discoveryAddress = "istiod.istio-system.svc:15012"
#         proxyMetadata    = {}
#         tracing = {
#           zipkin = {
#             address = "zipkin.istio-system:9411"
#           }
#         }
#       }
#       defaultProviders = {
#         metrics = ["prometheus"]
#       }
#       enablePrometheusMerge = true
#       extensionProviders = [
#         {
#           name = "ext-auth-grpc"
#           envoyExtAuthzGrpc = {
#             service = "unified-gateway-auth.gateway.svc.cluster.local"
#             port    = "9000"
#           }
#         },
#         {
#           name = "ext-auth-http"
#           envoyExtAuthzHttp = {
#             service = "unified-gateway-auth.gateway.svc.cluster.local"
#             port    = "8000"
#           }
#         },
#         {
#           name = grpcprovider
#           envoyExtAuthzHttp = {
#             service = app_name[1]+".default.svc.cluster.local"
#             port    = "8080"
#           }
#         }
#       ]
#       rootNamespace = "istio-system"
#       trustDomain   = "cluster.local"
#     })

#     meshNetworks = "networks: {}"
#   }
# }



  resource "google_compute_instance" "default" {
    name         = var.vm_name
    machine_type = var.machine_type
    zone         = var.zone

    boot_disk {
      initialize_params {
        image = var.image
      }
    }

    network_interface {
      subnetwork = var.subnet_self_link
      access_config {}
    }

    service_account {
      email  = google_service_account.vm_sa.email
      scopes = ["cloud-platform"]
    }
    tags = var.tags
  }

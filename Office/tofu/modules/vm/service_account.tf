  resource "google_service_account" "vm_sa" {
    account_id   = "${var.vm_name}-sa"
    display_name = "Service Account for ${var.vm_name}"
  }

  resource "google_project_iam_member" "log_writer" {
    project = var.project_id
    role    = "roles/logging.logWriter"
    member  = "serviceAccount:${google_service_account.vm_sa.email}"
  }

  resource "google_project_iam_member" "monitoring_writer" {
    project = var.project_id
    role    = "roles/monitoring.metricWriter"
    member  = "serviceAccount:${google_service_account.vm_sa.email}"
  }

  output "network_self_link" {
    value = google_compute_network.vpc_network.self_link
  }

  output "subnet_self_link" {
    value = google_compute_subnetwork.subnet.self_link
  }

  #output "firewall_rules" {
  #  value = [
  #    google_compute_firewall.allow_ssh.name,
  #    google_compute_firewall.allow_internal.name
  #  ]
  #}

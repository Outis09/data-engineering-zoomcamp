terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.16.0"
    }
  }
}

provider "google" {
  project = "nimble-volt-413114"
  region  = "us-west4"
}


resource "google_storage_bucket" "de-zoomcamp-demo-bucket" {
  name          = "nimble-volt-413114-terra-bucket"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
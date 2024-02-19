variable "credentials" {
  description = "My credentials"
  default = "path/to/my/credentials"
}

variable "project" {
    description = "Project"
    default = "nimble-volt-413114"
}

variable "region" {
  description = "Project region"
  default = "us-west4"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery"
  default = "terra_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket"
  default = "nimble-volt-413114-terra-bucket"
}

variable "gsc_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}
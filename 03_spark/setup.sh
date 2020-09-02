#!/bin/bash

# Create a CloudSQL instance to be the recommendation database
gcloud sql instances create recsys-db --database-version MYSQL_5_7 --tier db-f1-micro --region us-west1

# Create recommendation database
gcloud sql databases create rec-db --instance recsys-db

# Create recommendation user
gcloud sql users create rec-db --instance recsys-db --password rec-db

# Create a Dataproc cluster to run the algorithm
gcloud dataproc clusters create ml-cluster --region us-west1

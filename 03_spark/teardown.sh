#!/bin/bash

# Delete CloudSQL instance
gcloud sql instances delete recsys-db --async

# Delete Dataproc cluster
gcloud dataproc clusters delete ml-cluster --region us-west1

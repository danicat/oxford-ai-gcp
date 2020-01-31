#!/bin/bash

PROJECT=$(gcloud config get-value project)
TOKEN=$(gcloud auth print-access-token)
curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -X POST https://compute.googleapis.com/compute/v1/projects/$PROJECT/zones/us-west1-a/instances \
    -d @instance.json

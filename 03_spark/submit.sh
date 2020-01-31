#!/bin/bash

CLOUDSQL_IP=$(gcloud sql instances describe recsys-db | grep ipAddress | tail -n 1 | awk '{print $3}')

gcloud dataproc jobs submit pyspark als.py --cluster ml-cluster \
    --region us-west1 \
    --jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar \
    -- ${CLOUDSQL_IP:-localhost} rec-db rec-db rec-db

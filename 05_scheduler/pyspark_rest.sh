PROJECT=$(gcloud config get-value project)
TOKEN=$(gcloud auth print-access-token)
curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -X POST https://dataproc.googleapis.com/v1/projects/danicat/regions/us-west1/jobs:submit \
    -d @job.json
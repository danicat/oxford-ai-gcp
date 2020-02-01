#!/bin/bash
PROJECT=$(gcloud config get-value project)
# Triggers a beam job using the DirectRunner
python pageviews.py --runner Dataflow \
    --topic projects/$PROJECT/topics/pageviews \
    --table $PROJECT:oxford.pageviews \
    --project $PROJECT \
    --region us-west1 \
    --temp_location gs://danicat/temp #replace with your own bucket!

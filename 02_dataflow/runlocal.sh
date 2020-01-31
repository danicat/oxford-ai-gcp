#!/bin/bash
PROJECT=$(gcloud config get-value project)
# Triggers a beam job using the DirectRunner
python pageviews.py --topic projects/$PROJECT/topics/pageviews --table danicat:oxford.pageviews

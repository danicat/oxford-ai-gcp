#!/bin/bash

# delete subscription
gcloud pubsub subscriptions delete pageviews_datalake

# delete topic
gcloud pubsub topics delete pageviews

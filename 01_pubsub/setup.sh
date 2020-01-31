#!/bin/bash

# create topic
gcloud pubsub topics create pageviews

# create subscription
gcloud pubsub subscriptions create --topic pageviews pageviews_datalake
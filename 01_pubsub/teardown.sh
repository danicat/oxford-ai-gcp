#!/bin/bash

# delete subscription
gcloud pubsub subscriptions delete pageviews_console

# delete topic
gcloud pubsub topics delete pageviews

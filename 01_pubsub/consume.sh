#!/bin/bash

# consume message
gcloud pubsub subscriptions pull pageviews_console --auto-ack

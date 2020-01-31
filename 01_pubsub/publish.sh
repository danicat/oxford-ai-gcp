#!/bin/bash

# publish message
gcloud pubsub topics publish pageviews --message '{"user_id":1,"doc_id":1}'

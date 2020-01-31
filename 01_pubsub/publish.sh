#!/bin/bash

# publish message
gcloud pubsub topics publish pageviews --message '{"userid":1,"docid":1}'

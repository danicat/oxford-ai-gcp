#!/bin/bash

# This scripts create the following utility matrix:
#
#     1 2 3 4 5 6
#   --------------
# 1 | 1 1   1
# 2 | 1 1 1
# 3 |   1     1
# 4 |         1
# 5 |            1
#

# publish all messages
gcloud pubsub topics publish pageviews --message '{"user_id":1,"doc_id":1}'
gcloud pubsub topics publish pageviews --message '{"user_id":1,"doc_id":2}'
gcloud pubsub topics publish pageviews --message '{"user_id":1,"doc_id":4}'
gcloud pubsub topics publish pageviews --message '{"user_id":2,"doc_id":1}'
gcloud pubsub topics publish pageviews --message '{"user_id":2,"doc_id":2}'
gcloud pubsub topics publish pageviews --message '{"user_id":2,"doc_id":3}'
gcloud pubsub topics publish pageviews --message '{"user_id":3,"doc_id":2}'
gcloud pubsub topics publish pageviews --message '{"user_id":3,"doc_id":5}'
gcloud pubsub topics publish pageviews --message '{"user_id":4,"doc_id":5}'
gcloud pubsub topics publish pageviews --message '{"user_id":5,"doc_id":6}'

#!/bin/bash

ENDPOINT=$(gcloud functions describe recommend | grep url | awk '{print $2}')
curl -X POST $ENDPOINT -H "Content-Type:application/json" --data '{"user_id":"5"}'
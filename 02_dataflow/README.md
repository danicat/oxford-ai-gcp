# Pub/Sub and Dataflow Streaming

## Setup

First create a topic on Pub/Sub as explained in the previous session, then run the setup script to create a BigQuery dataset at the current project. Please beware that at the time of this writing, the `bq` command required python 2.

## Running the example

After creating the dataset, run one of the following scripts to start the streaming job: `rundataflow.sh` or `runlocal.sh`.

Please not that `runlocal.sh` will use the DirectRunner, so it will run from your machine, while `rundataflow.sh` will trigger a dataflow job on GCP, so it will not be running locally.
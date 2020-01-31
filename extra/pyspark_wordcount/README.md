# PySpark / Dataproc

To run locally:

```sh
spark-submit wordcount.py
```

To run in Dataproc, first you need to create a cluster:

```sh
gcloud dataproc clusters create --region us-west1 $CLUSTER_NAME
```

Then submit the job:

```sh
gcloud dataproc jobs submit pyspark --region us-west1 --cluster $CLUSTER_NAME wordcount.py
```

Remember to delete the cluster afterwards!

```sh
gcloud dataproc clusters delete --region us-west1 $CLUSTER_NAME
```

## Adding NLTK to Dataproc

Login to the Dataproc master using SSH and run:

```sh
sudo apt-get install python3-nltk
```

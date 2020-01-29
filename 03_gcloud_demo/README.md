# GCP Demo

Managing resources with the `gcloud` command line interface.

```sh
gcloud auth login
```

```sh
gcloud config set project $PROJECT
```


```sh
gcloud compute instances create $INSTANCE_NAME --zone us-west1-a --machine-type f1-micro
```

```sh
gcloud compute ssh $INSTANCE_NAME
```

```sh
gcloud compute instances delete $INSTANCE_NAME
```
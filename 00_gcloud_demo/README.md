# GCP Demo

## Creating instances using the gcloud CLI

Authenticating your user:

```sh
gcloud auth login
```

Setting the active project:

```sh
gcloud config set project $PROJECT
```

Creating a compute instance of type `f1-micro` in `us-west1-a`:

```sh
gcloud compute instances create $INSTANCE_NAME --zone us-west1-a --machine-type f1-micro
```

Connecting to the instance:

```sh
gcloud compute ssh $INSTANCE_NAME
```

Deleting the instance:

```sh
gcloud compute instances delete $INSTANCE_NAME
```

## Creating instances using the REST API

If you want to use the REST API you need to pay extra attention to the resource names, e.g., instead of machine type `f1-micro` you need to specify its full path in the given zone, like `zones/us-west1-a/machineTypes/f1-micro`.

The same is valid for disks and other resources. See the example below.

```sh
PROJECT=$(gcloud config get-value project)
TOKEN=$(gcloud auth print-access-token)
curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -X POST https://compute.googleapis.com/compute/v1/projects/$PROJECT/zones/us-west1-a/instances \
    -d @instance.json
```

With `instance.json` being:

```json
{
    "name": "ubuntu-micro",
    "machineType": "zones/us-west1-a/machineTypes/f1-micro",
    "networkInterfaces": [
        {
            "accessConfigs": [
                {
                    "type": "ONE_TO_ONE_NAT",
                    "name": "External NAT"
                }
            ],
            "network": "global/networks/default"
        }
    ],
    "disks": [
        {
            "boot":"true",
            "initializeParams": {
                "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-minimal-1804-lts"
            }
        }
    ]
}
```

# PubSub Demonstration

In this demo you will create a PubSub topic and a subscription to this topic. We'll see how to publish and consume messages from the command line.

## Setup

To create the subscription and topic run the `setup.sh` file.

```sh
./setup.sh
```

This file will run the commands `gcloud pubsub topic create` and `gcloud pubsub subscription create` to create a topic called `pageviews` and a subscription on that topic called `pageviews_console`.

## Publishing and consuming messages

When you publish to PubSub you publish to a topic. The `publish_one.sh` script will publish one message to the `pageviews` topic we've just created.

The subscription is the structure that keeps track of the offset of the message we are currently reading. We can have as many consumers as we want for a given subscription, but it is important to remember that PubSub has at least once message delivery guarantees. That means that we must provide additional logic to handle duplicates if that is undesirable.

The `consume.sh` script will take one message from the `pageviews_console` subscription. Please note that message delivery order is also not guaranteed, but at low volumes it may seem sequential.

## Other scripts

The `publish_all.sh` script is provided to generate some data for the next examples.

Finally, the `_publish_forever.sh` script runs an infinite loop publishing the same message over and over so you can see a bit of load in the Dataflow example on the next sesion.

## Cleaning Up

After you are done with the PubSub topic and subscription you can clean your environment by running `teardown.sh`.

```sh
./teardown.sh
```

Please note that this topic will be used in the examples for the next sessions so you should only run `teardown.sh` after you.

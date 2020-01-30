# PubSub

This is a simple pubsub CLI demo on how to create topics, publish and consume messages.

Create a topic:

```sh
gcloud pubsub topics create meetup-topic
```

Create a subscription:

```sh
gcloud pubsub subscriptions create --topic meetup-topic meetup-subs
```

List subscriptions:

```sh
gcloud pubsub topics list-subscriptions meetup-topic
```

Publish a message:

```sh
gcloud pubsub topics publish meetup-topic --message "hello world"
```

Retrieve a message:

```sh
gcloud pubsub subscriptions pull meetup-subs --auto-ack
```

## Pubsub Snapshots

Publish a message:

```sh
gcloud pubsub topics publish meetup-topic --message "hello world"
```

Create a snapshot:

```sh
gcloud pubsub snapshots create test-snap --subscription=meetup-subs
```

Pull the message:

```sh
gcloud pubsub subscriptions pull meetup-subs --auto-ack
```

Pull it again (nothing should come out of it!):

```sh
gcloud pubsub subscriptions pull meetup-subs --auto-ack
```

Rewind the subscription using the snapshot:

```sh
gcloud pubsub subscriptions seek --snapshot test-snap meetup-subs
```

Try pulling the message again (may take a few tries!):

```sh
gcloud pubsub subscriptions pull meetup-subs --auto-ack
```

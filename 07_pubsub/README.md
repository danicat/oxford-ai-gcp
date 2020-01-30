# Pub/Sub and Dataflow Streaming

First create a topic on Pub/Sub, then start the streaming job:

```sh
python pubsubtotext.py --topic topic-name --output local-filename
```

This must be run using DirectRunner as Dataflow can't write a local file!

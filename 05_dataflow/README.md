# Apache Beam / Dataflow

To run the wordcount example just type:

```sh
python wordcount.py
```

You can toggle between line 32 and 33 to write a local file or a gs one. Make sure you update the destination bucket to one you have write permissions.

Also, Dataflow uses application-default credentials. You may need to re-authorize using:

```sh
gcloud auth application-default login
```

To run it on Dataflow you need to specify the Dataflow runner and related parameters:

```sh
python wordcount.py --runner Dataflow --project danicat --temp_location gs://danicat/temp --region us-west1
```

from __future__ import absolute_import
import argparse

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--topic',
        type=str,
        help='Pub/Sub topic to read from',
        required=True)
    parser.add_argument(
        '--output',
        type=str,
        help='BigQuery table name',
        required=True)
    args, pipeline_args = parser.parse_known_args(argv)
    options = PipelineOptions(pipeline_args)
    options.view_as(SetupOptions).save_main_session=True
    options.view_as(StandardOptions).streaming=True

    p = beam.Pipeline(options=options)
    (p | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=args.topic)
       | 'Convert to JSON' >> beam.Map(lambda message: {"message": message})
       | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
            args.output,
            schema='message:STRING',
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
    
    result = p.run()
    result.wait_until_finish()

if __name__ == "__main__":
    run()

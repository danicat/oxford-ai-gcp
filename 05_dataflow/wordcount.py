import apache_beam as beam

from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import WriteToText

def run():
    pipeline_options = PipelineOptions()
    pipeline_options.view_as(SetupOptions).save_main_session = True
    p = beam.Pipeline(options=pipeline_options)

    lines = p | 'read' >> ReadFromText("gs://apache-beam-samples/shakespeare/hamlet.txt")

    def count_ones(word_ones):
        (word, ones) = word_ones
        return (word, sum(ones))

    counts = (lines
                | 'split' >> beam.FlatMap(lambda line: line.split())
                | 'pair_with_one' >> beam.Map(lambda x: (x, 1))
                | 'group' >> beam.GroupByKey()
                | 'count' >> beam.Map(count_ones))

    # Format the counts into a PCollection of strings.
    def format_result(word_count):
        (word, count) = word_count
        return '%s: %d' % (word, count)

    output = counts | 'format' >> beam.Map(format_result)

    # output | 'write' >> WriteToText("wordcount.txt")
    output | 'write' >> WriteToText("gs://danicat/wordcount.txt")

    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
  run()
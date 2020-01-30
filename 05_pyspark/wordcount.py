import pyspark
from pyspark.sql import SparkSession

sc = pyspark.SparkContext()
spark = SparkSession(sc)

text = sc.textFile("hamlet.txt")
# use the line below when running on Dataproc
# text = sc.textFile("gs://apache-beam-samples/shakespeare/hamlet.txt")
words = text.flatMap(lambda line: line.split())
ones = words.map(lambda word: (word, 1))
counts = ones.reduceByKey(lambda x, y : x + y)

print(counts.toDebugString().decode('utf-8'))

counts.take(10)

sorted = counts.sortBy(lambda x: -x[1])
sorted.take(10)

print(sorted.toDebugString().decode('utf-8'))

local = sorted.collect()

type(local)
type(sorted)

df = counts.toDF(["word","count"])

df.show()

df.describe().show()

from pyspark.sql.functions import col
df.orderBy(col("count").desc()).show()

df.createOrReplaceTempView("wordcount")
df2 = spark.sql("select upper(word), sum(count) from wordcount group by upper(word) order by 2 desc")

print(df2.rdd.toDebugString().decode('utf-8'))

df2.show()

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

sw = stopwords.words('english')
stopwordsDf = sc.parallelize(sw).map(lambda x: str(x)).map(str.upper).map(lambda word: (word,)).toDF(["word"])
stopwordsDf.createOrReplaceTempView("stopwords")

filtered = spark.sql("select upper(word), sum(count) from wordcount where upper(word) not in (select * from stopwords) group by upper(word) order by 2 desc")
filtered.show()

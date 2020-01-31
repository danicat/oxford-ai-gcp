import logging
import sys
from pyspark.sql import SparkSession, SQLContext
from pyspark.mllib.recommendation import ALS
from pyspark.sql.types import StructType, StructField, StringType, FloatType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CLOUDSQL_INSTANCE_IP = sys.argv[1]
CLOUDSQL_DB_NAME = sys.argv[2]
CLOUDSQL_USER = sys.argv[3]
CLOUDSQL_PWD = sys.argv[4]

spark = SparkSession.builder.appName('ALS Recommender').getOrCreate()

# Load data from BigQuery.
df = spark.read \
    .format("bigquery") \
    .option("table", "danicat.oxford.pageviews") \
    .load()

df.createOrReplaceTempView("pageviews")

df_pageviews = spark.sql("select distinct user_id, doc_id, 1 as rating from pageviews")

df_pageviews.show()

rank = 8
seed = 5L
iterations = 10
regularization_parameter = 0.1

logger.info("Training the ALS model...")
model = ALS.train(df_pageviews.rdd.map(lambda r: (int(r[0]), int(r[1]), r[2])).cache(),
    rank=rank,
    seed=seed,
    iterations=iterations,
    lambda_=regularization_parameter)

logger.info("ALS model built!")

# Calculate all predictions
predictions = model.recommendProductsForUsers(10) \
    .flatMap(lambda pair: pair[1]) \
    .map(lambda rating: (rating.user, rating.product, rating.rating))

TABLE_RECOMMENDATIONS = 'RECOMMENDATIONS'
jdbcUrl = 'jdbc:mysql://%s:3306/%s?user=%s&password=%s' % (CLOUDSQL_INSTANCE_IP, CLOUDSQL_DB_NAME, CLOUDSQL_USER, CLOUDSQL_PWD)

schema = StructType([StructField("user_id", StringType(), True), StructField("doc_id", StringType(), True), StructField("prediction", FloatType(), True)])
dfToSave = spark.createDataFrame(predictions, schema)

dfToSave.show()

dfToSave.write.jdbc(url=jdbcUrl, table=TABLE_RECOMMENDATIONS, mode='overwrite', properties={"useSSL": "false"})

# BigQuery

In [BigQuery console](https://console.cloud.google.com/bigquery) run the following query to find all occurences of the phrase hello world! :D

```sql
SELECT COUNT(*)
  FROM `bigquery-public-data.github_repos.sample_contents`
 WHERE LOWER(content) LIKE '%hello world%';
```

Expected result: about 23.6 GB processed in 2.2 seconds. Total occurences as of 30/01/2020: 8976.

If you feel in the mood of spending you free credits, you may as well replace the sample table with the full table:

```sql
SELECT COUNT(*)
  FROM `bigquery-public-data.github_repos.contents`
 WHERE LOWER(content) LIKE '%hello world%';
```

That will scan over 2 TB and cost you about $10.

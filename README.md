# AWS Data Project

1. Create the first Lambda function to generate mock data, deploy the code, add test event to test the code and test the code.
2. Create an Event Bridge Scheduler to trigger first Lambda function that will generate mock data at a specific interval and add it to the first lambda function as Trigger.
3. Create a S3 bucket.
4. Create the second lambda function to insert data into S3 bucket, provide relevant IAM Role to connect S3 and lambda.
5. Add the second lambda as the destination to the first lambda.
6. Create a Glue crawler to read data from S3, add a glue database to store the metadata of the mock data.
7. Add Classifiers in the Crawler so that crawler identifies the json data and then run the crawler.
8. Create a table in DynamoDB, mention desired column names from mock data as partition_key and sorting_key.
9. Create a Glue Job, enable job bookmarking and write pyspark script to read data incrementally.
10. Run the Glue job and observe the output logs printing the output.
11. Go to the DynamoDB table, execute the command 'select * from table_name' and observe the unique records are inserted.
(Provide IAM Roles wherever required)

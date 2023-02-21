import json, boto3, datetime

def lambda_handler(event, context):
    project_data = event['responsePayload']
    print(project_data)
    current_epoch_time = datetime.datetime.now().timestamp()
    bucket_name = 'project1-data'
    print('Start data write in s3')
    s3 = boto3.resource('s3')
    s3object = s3.Object(bucket_name, f'inbox/{str(current_epoch_time)}_project_data.json')
    s3object.put(
        Body=(bytes(json.dumps(project_data).encode('UTF-8')))
        )
    print('Data write successful in s3')

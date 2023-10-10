import boto3
import requests
import json

# Initialize clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
secretsmanager = boto3.client('secretsmanager')

# Configuration constants
TABLE_NAME = 'FHV_Ingestion_Metadata'
BUCKET_NAME = 'fhv-active-dataset'
KEY_PREFIX = "data/fhv_data_"
ENDPOINT = "https://data.cityofnewyork.us/resource/8wbx-tsch.json"
LIMIT = 50000
SECRET_NAME = "FHV_APP_TOKEN"  # Assuming the token stored under this name in Secrets Manager

# Retrieve app token from Secrets Manager
response = secretsmanager.get_secret_value(SecretId=SECRET_NAME)
secret_string = response['SecretString']
secret_data = json.loads(secret_string)
APP_TOKEN = secret_data['APP_TOKEN']

def fetch_and_store_data():

    # Retrieve the last ingested timestamp from DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'MetadataID': 'LastIngestedTimestamp'})
    
    last_ingested_date = response.get('Item', {}).get('LastDateUpdated', '1900-01-01')  # Default to a very old date if not found
    last_ingested_time = response.get('Item', {}).get('LastTimeUpdated', '00:00:00')    # Default to midnight if not found

    all_data = []
    offset = 0

    while True:
        # API params to fetch updated records with pagination
        PARAMS = {
            "$where": f"Last Date Updated > '{last_ingested_date}' OR (Last Date Updated = '{last_ingested_date}' AND Last Time Updated > '{last_ingested_time}')",
            "$order": "Last Date Updated DESC, Last Time Updated DESC",
            "$limit": LIMIT,
            "$offset": offset,
            "$$app_token": APP_TOKEN
        }

        data = requests.get(ENDPOINT, params=PARAMS).json()

        if not data:  # exit loop if no more data is returned
            break

        all_data.extend(data)

        if len(data) < LIMIT:  # exit loop if less than the limit
            break

        offset += LIMIT

    # If there's new data, store it in S3
    if all_data:
        s3_key = KEY_PREFIX + all_data[0]['Last Date Updated'] + ".json"
        s3.put_object(Body=json.dumps(all_data), Bucket=BUCKET_NAME, Key=s3_key)

        # Update the last ingested timestamp in DynamoDB
        most_recent_date = all_data[0]['Last Date Updated']
        most_recent_time = all_data[0]['Last Time Updated']
        table.put_item(Item={'MetadataID': 'LastIngestedTimestamp', 'LastDateUpdated': most_recent_date, 'LastTimeUpdated': most_recent_time})

fetch_and_store_data()

import boto3
# Get the service resource.
import key_config as keys

dynamodb = boto3.resource('dynamodb',
                  ACCESS_KEY_ID='AKIA2L33ENFC2WPWG3M4'
                  ACCESS_SECRET_KEY='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'
                  region_name           = "ap-south-1")

#dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='userdata',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        }
         
    ],
    AttributeDefinitions=[
             {
            'AttributeName': 'email',
            'AttributeType': 'S'
        } 
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='userdata')

# Print out some data about the table.
print(table.item_count)

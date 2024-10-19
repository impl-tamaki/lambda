import boto3

from boto3.dynamodb.conditions import Key, Attr
 
print('Loading function')
 
dynamodb = boto3.resource('dynamodb')
 
def lambda_handler(event, context):
    table_name = "testdb"
    partition_key = {"id": event["id"]}
    dynamotable = dynamodb.Table(table_name)
    res = dynamotable.get_item(Key=partition_key)
    item = res["Item"]
    
    return item


# {
#   "id" : $input.params('id')
# }



# {
#   "id": "1001"
# }

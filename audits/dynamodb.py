import boto3

def audit_dynamodb():
    results = []
    dynamodb = boto3.client("dynamodb")
    tables = dynamodb.list_tables()
    for table_name in tables.get("TableNames", []):
        desc = dynamodb.describe_table(TableName=table_name)["Table"]
        status = desc.get("TableStatus", "N/A")
        item_count = desc.get("ItemCount", "N/A")
        size = desc.get("TableSizeBytes", "N/A")
        arn = desc.get("TableArn", "N/A")
        region = arn.split(":")[3] if arn != "N/A" else "N/A"
        results.append(f"DynamoDB Table: {table_name} (Status: {status}, Items: {item_count}, Size: {size} bytes, Region: {region})")
    return results

import boto3

def audit_rds():
    results = []
    rds = boto3.client("rds")

    instances = rds.describe_db_instances()
    for db in instances["DBInstances"]:
        engine = db.get("Engine", "N/A")
        status = db.get("DBInstanceStatus", "N/A")
        instance_class = db.get("DBInstanceClass", "N/A")
        storage = db.get("AllocatedStorage", "N/A")
        arn = db.get("DBInstanceArn", "N/A")
        region = arn.split(":")[3] if arn != "N/A" else "N/A"
        if status == "stopped":
            results.append(f"Stopped RDS instance: {db['DBInstanceIdentifier']} (Engine: {engine}, Status: {status}, Class: {instance_class}, Storage: {storage} GB, Region: {region})")
        else:
            results.append(f"Active RDS instance: {db['DBInstanceIdentifier']} (Engine: {engine}, Status: {status}, Class: {instance_class}, Storage: {storage} GB, Region: {region})")
    return results

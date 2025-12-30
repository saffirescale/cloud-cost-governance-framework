import boto3

def audit_s3():
    results = []
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()
    for b in buckets.get("Buckets", []):
        name = b["Name"]
        creation_date = b.get("CreationDate", "N/A")
        # Get region
        try:
            region = s3.get_bucket_location(Bucket=name)["LocationConstraint"] or "us-east-1"
        except Exception:
            region = "N/A"
        # Get number of objects and total size (may be slow for large buckets)
        s3_resource = boto3.resource("s3", region_name=region)
        bucket = s3_resource.Bucket(name)  # type: ignore
        obj_count = 0
        total_size = 0
        try:
            for obj in bucket.objects.all():
                obj_count += 1
                total_size += obj.size
        except Exception:
            obj_count = "N/A"
            total_size = "N/A"
        results.append(f"S3 Bucket: {name} (Created: {creation_date}, Region: {region}, Objects: {obj_count}, Size: {total_size} bytes)")
    return results

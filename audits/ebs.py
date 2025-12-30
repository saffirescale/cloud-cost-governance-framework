import boto3

def audit_ebs():
    results = []
    ec2 = boto3.client("ec2")

    volumes = ec2.describe_volumes()
    for v in volumes["Volumes"]:
        if not v["Attachments"]:
            results.append(f"Unattached EBS volume: {v['VolumeId']} ({v['Size']} GB)")

    return results

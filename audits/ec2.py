import boto3

def audit_ec2():
    results = []
    ec2 = boto3.client("ec2")

    instances = ec2.describe_instances()
    running = []
    stopped = []
    for r in instances["Reservations"]:
        for i in r["Instances"]:
            instance_id = i["InstanceId"]
            instance_type = i.get("InstanceType", "N/A")
            state = i["State"]["Name"]
            launch_time = i.get("LaunchTime", "N/A")
            public_ip = i.get("PublicIpAddress", "N/A")
            tags = {t['Key']: t['Value'] for t in i.get('Tags', [])}
            region = ec2.meta.region_name
            details = f"InstanceId: {instance_id}, Type: {instance_type}, State: {state}, LaunchTime: {launch_time}, PublicIP: {public_ip}, Tags: {tags}, Region: {region}"
            if state == "running":
                running.append(f"Running EC2 instance: {details}")
            elif state == "stopped":
                stopped.append(f"Stopped EC2 instance: {details}")
    if running:
        results.append("Active EC2 Instances:")
        results.extend(running)
    if stopped:
        results.append("Unused EC2 Instances:")
        results.extend(stopped)
    return results

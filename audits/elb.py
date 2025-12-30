import boto3

def audit_elb():
    results = []
    elb = boto3.client("elbv2")

    lbs = elb.describe_load_balancers()
    for lb in lbs.get("LoadBalancers", []):
        lb_type = lb.get("Type", "N/A")
        lb_name = lb.get("LoadBalancerName", "N/A")
        lb_dns = lb.get("DNSName", "N/A")
        lb_state = lb.get("State", {}).get("Code", "N/A")
        lb_scheme = lb.get("Scheme", "N/A")
        vpc_id = lb.get("VpcId", "N/A")
        arn = lb.get("LoadBalancerArn", "N/A")
        region = arn.split(":")[3] if arn != "N/A" else "N/A"
        # Get listeners
        try:
            listeners = elb.describe_listeners(LoadBalancerArn=arn)["Listeners"]
            listener_ports = [str(l["Port"]) for l in listeners]
        except Exception:
            listener_ports = []
        results.append(f"{lb_type} Load Balancer: {lb_name} (DNS: {lb_dns}, State: {lb_state}, Scheme: {lb_scheme}, VPC: {vpc_id}, Listeners: {listener_ports}, Region: {region})")

    return results

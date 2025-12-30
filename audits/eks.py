import boto3

def audit_eks():
    results = []
    eks = boto3.client("eks")
    clusters = eks.list_clusters()
    for cluster_name in clusters.get("clusters", []):
        desc = eks.describe_cluster(name=cluster_name)["cluster"]
        version = desc.get("version", "N/A")
        status = desc.get("status", "N/A")
        endpoint = desc.get("endpoint", "N/A")
        region = desc.get("arn", "N/A").split(":")[3] if "arn" in desc else "N/A"
        results.append(f"EKS Cluster: {cluster_name} (Version: {version}, Status: {status}, Endpoint: {endpoint}, Region: {region})")
    return results

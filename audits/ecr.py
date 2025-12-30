import boto3

def audit_ecr():
    results = []
    ecr = boto3.client("ecr")
    repos = ecr.describe_repositories()
    for repo in repos.get("repositories", []):
        name = repo.get("repositoryName", "N/A")
        uri = repo.get("repositoryUri", "N/A")
        arn = repo.get("repositoryArn", "N/A")
        region = arn.split(":")[3] if arn != "N/A" else "N/A"
        # Get image count
        try:
            images = ecr.list_images(repositoryName=name)
            image_count = len(images.get("imageIds", []))
        except Exception:
            image_count = "N/A"
        results.append(f"ECR Repository: {name} (URI: {uri}, Images: {image_count}, Region: {region})")
    return results

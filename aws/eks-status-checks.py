import boto3

client = boto3.client('eks', region_name='us-east-2')
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.list_clusters(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_version = cluster_info['version']
    cluster_endpoint = cluster_info['endpoint']

    print(f"Cluster {cluster} is {cluster_status}")
    print(f"Cluster Version: {cluster_version}")
    print(f"Cluster Endpoint: {cluster_endpoint}")

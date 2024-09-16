import boto3

ec2_client_ohio = boto3.client('ec2', region_name="us-east-2")
ec2_resource_ohio = boto3.resource('ec2', region_name="us-east-2")

ec2_client_mumbai = boto3.client('ec2', region_name="ap-south-1")
ec2_resource_mumbai = boto3.resource('ec2', region_name="ap-south-1")

instance_ids_ohio = []
instance_ids_mumbai = []

reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
for reservation in reservations_ohio:
    instances = reservation['Instances']
    for instance in instances:
        instance_ids_ohio.append(instance['InstanceId'])

response = ec2_resource_ohio.create_tags(
    Resources=instance_ids_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


reservations_mumbai = ec2_client_mumbai.describe_instances()['Reservations']
for reservation in reservations_mumbai:
    instances = reservation['Instances']
    for instance in instances:
        instance_ids_mumbai.append(instance['InstanceId'])

response = ec2_resource_mumbai.create_tags(
    Resources=instance_ids_mumbai,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
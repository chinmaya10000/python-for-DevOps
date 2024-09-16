import boto3

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2', region_name='us-east-2')

"""new_vpc = ec2_resource.create_vpc(
    CidrBlock='10.0.0.0/16'
)
new_vpc.create_subnet(
    CidrBlock='10.0.1.0/24'
)
new_vpc.create_subnet(
    CidrBlock='10.0.2.0/24'
)
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-new-vpc'
        }
    ]
)"""



all_available_vpcs = ec2_client.describe_vpcs()
subnets = ec2_client.describe_subnets()

vpcs = all_available_vpcs['Vpcs']

for vpc in vpcs:
    print(f"VPC ID: {vpc['VpcId']}")
    cidr_block_assoc_set = vpc['CidrBlockAssociationSet']
    for assoc_set in cidr_block_assoc_set:
        print(assoc_set['CidrBlockState'])

for subnet in subnets['Subnets']:
    if subnet['DefaultForAz']:
        print(f"Subnet ID: {subnet['SubnetId']}")
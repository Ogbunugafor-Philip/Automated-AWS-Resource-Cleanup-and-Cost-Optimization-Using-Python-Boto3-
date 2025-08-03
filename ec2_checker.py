import boto3
from botocore.exceptions import EndpointConnectionError

# Store results here
stopped_instances = []

# Get all AWS regions dynamically
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    try:
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_instances()
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                state = instance['State']['Name']
                instance_id = instance['InstanceId']
                name = ''
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                
                if state == 'stopped':
                    stopped_instances.append({
                        'Region': region,
                        'InstanceID': instance_id,
                        'Name': name
                    })
    except EndpointConnectionError:
        print(f"⚠️ Skipping region {region} (cannot connect).")

# Print results
if stopped_instances:
    print("\n🔹 Stopped EC2 Instances Found:")
    for instance in stopped_instances:
        print(f"Region: {instance['Region']}, ID: {instance['InstanceID']}, Name: {instance['Name']}")
else:
    print("\n✅ No stopped EC2 instances found in reachable regions.")

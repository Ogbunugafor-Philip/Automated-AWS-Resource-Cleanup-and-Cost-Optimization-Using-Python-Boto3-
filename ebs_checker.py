import boto3
from botocore.exceptions import EndpointConnectionError

# Store results here
unused_volumes = []

# Get all AWS regions dynamically
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    try:
        ec2 = boto3.client('ec2', region_name=region)
        volumes = ec2.describe_volumes()['Volumes']
        
        for volume in volumes:
            if volume['State'] == 'available':
                unused_volumes.append({
                    'Region': region,
                    'VolumeID': volume['VolumeId'],
                    'Size_GB': volume['Size']
                })
    except EndpointConnectionError:
        print(f"⚠️ Skipping region {region} (cannot connect).")

# Print results
if unused_volumes:
    print("\n🔹 Unattached EBS Volumes Found:")
    for vol in unused_volumes:
        print(f"Region: {vol['Region']}, ID: {vol['VolumeID']}, Size: {vol['Size_GB']}GB")
else:
    print("\n✅ No unused EBS volumes found in reachable regions.")

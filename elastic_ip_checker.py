import boto3
from botocore.exceptions import EndpointConnectionError

# Store results here
unused_eips = []

# Get all AWS regions dynamically
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    try:
        ec2 = boto3.client('ec2', region_name=region)
        addresses = ec2.describe_addresses()['Addresses']
        
        for address in addresses:
            if 'InstanceId' not in address and 'NetworkInterfaceId' not in address:
                unused_eips.append({
                    'Region': region,
                    'PublicIP': address['PublicIp'],
                    'AllocationId': address.get('AllocationId', 'N/A')
                })
    except EndpointConnectionError:
        print(f"⚠️ Skipping region {region} (cannot connect).")

# Print results
if unused_eips:
    print("\n🔹 Unused Elastic IPs Found:")
    for eip in unused_eips:
        print(f"Region: {eip['Region']}, IP: {eip['PublicIP']}, AllocationID: {eip['AllocationId']}")
else:
    print("\n✅ No unused Elastic IPs found in reachable regions.")

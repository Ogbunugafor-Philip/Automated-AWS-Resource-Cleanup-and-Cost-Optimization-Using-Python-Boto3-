import csv

# Import functions from other scripts
from ec2_checker import stopped_instances
from ebs_checker import unused_volumes
from elastic_ip_checker import unused_eips
from s3_checker import unused_buckets

# Create CSV report
with open('unused_resources_report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ResourceType", "Region/Bucket", "ID/Name", "ExtraInfo"])
    
    # Write EC2 data
    for ec2 in stopped_instances:
        writer.writerow(["EC2", ec2['Region'], ec2['InstanceID'], ec2['Name']])
    
    # Write EBS data
    for ebs in unused_volumes:
        writer.writerow(["EBS", ebs['Region'], ebs['VolumeID'], f"Size: {ebs['Size_GB']}GB"])
    
    # Write Elastic IP data
    for eip in unused_eips:
        writer.writerow(["Elastic IP", eip['Region'], eip['PublicIP'], eip['AllocationId']])
    
    # Write S3 data
    for s3 in unused_buckets:
        writer.writerow(["S3 Bucket", s3.get('Region', 'us-east-1'), s3['BucketName'], f"Inactive for: {s3['DaysInactive']} days"])

print("✅ Report generated successfully: unused_resources_report.csv")

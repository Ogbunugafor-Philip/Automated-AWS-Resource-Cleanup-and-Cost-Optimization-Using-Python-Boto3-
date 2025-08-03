import boto3
from datetime import datetime, timezone
from botocore.exceptions import EndpointConnectionError

# Store results here
unused_buckets = []

REGION = "us-east-1"
s3 = boto3.client('s3', region_name=REGION)
buckets = s3.list_buckets()['Buckets']

for bucket in buckets:
    bucket_name = bucket['Name']
    try:
        objects = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in objects:
            last_modified = max(obj['LastModified'] for obj in objects['Contents'])
            days_inactive = (datetime.now(timezone.utc) - last_modified).days
            if days_inactive > 30:
                unused_buckets.append({
                    'Region': REGION,
                    'BucketName': bucket_name,
                    'DaysInactive': days_inactive
                })
        else:
            unused_buckets.append({
                'Region': REGION,
                'BucketName': bucket_name,
                'DaysInactive': 'No objects (empty)'
            })
    except EndpointConnectionError:
        print(f"⚠️ Skipping bucket {bucket_name} (cannot connect).")
    except Exception as e:
        print(f"⚠️ Could not process bucket {bucket_name}: {str(e)}")

# Print results
if unused_buckets:
    print("\n🔹 Potentially Unused S3 Buckets Found:")
    for b in unused_buckets:
        print(f"Bucket: {b['BucketName']}, Inactive for: {b['DaysInactive']} days")
else:
    print("\n✅ No unused S3 buckets found in region us-east-1.")

import csv
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ================================
# 1️⃣ Import Functions (Lists from your scripts)
# ================================
from ec2_checker import stopped_instances
from ebs_checker import unused_volumes
from elastic_ip_checker import unused_eips
from s3_checker import unused_buckets

# ================================
# 2️⃣ Generate Report
# ================================
def generate_report():
    filename = 'unused_resources_report.csv'
    with open(filename, 'w', newline='') as file:
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
    
    print("✅ Report generated successfully:", filename)
    return filename

# ================================
# 3️⃣ Send Email
# ================================
def send_email(attachment_file):
    sender_email = "eloraosita@gmail.com"           # Sender Gmail
    app_password = "bxtj kdnr scqk tuam"            # Gmail App Password
    receiver_email = "pogbunugafor@gmail.com"       # Receiver email
    subject = "AWS Cost Optimization Report"
    body = "Hello,\n\nPlease find attached the latest AWS unused resources report.\n\nRegards,\nAWS Monitoring Bot"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the CSV file
    with open(attachment_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={attachment_file}")
    message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("✅ Email sent successfully with the AWS unused resources report!")

# ================================
# 4️⃣ Main Workflow
# ================================
if __name__ == "__main__":
    report_file = generate_report()  # Step 1: Generate the CSV
    send_email(report_file)          # Step 2: Send the CSV via email

# Automated AWS Resource Cleanup and Cost Optimization Using Python (Boto3)

## Introduction
Cloud computing has become the backbone of modern IT infrastructure, providing organizations with scalable resources and flexible services on demand. Among the leading providers, Amazon Web Services (AWS) offers a wide range of services such as compute, storage, networking, and databases that can be provisioned within minutes.
However, as cloud environments grow, organizations often face challenges in effectively managing these resources. Idle virtual machines, unused storage volumes, and other orphaned resources can accumulate over time, leading to increased operational costs and reduced efficiency.
This project focuses on leveraging Python automation to manage AWS resources more effectively. Using the AWS SDK for Python (Boto3), the project provides an automated way to identify and manage resources that are no longer in active use, ensuring cost optimization and better cloud hygiene.

## Statement of Problem
In AWS environments, it's common for resources like EC2 instances, EBS volumes, and Elastic IPs to be left running or unused after deployments and tests. These forgotten resources lead to unnecessary costs, resource sprawl, and manual cleanup burdens.
Without an automated system to detect and manage idle resources, organizations risk overspending and poor cloud hygiene. This project addresses that gap by providing a Python-based solution for automated detection and cleanup of unused AWS resources.


## Project Objectives
- To automatically detect idle or unused AWS resources such as EC2 instances, EBS volumes, and Elastic IPs.
- To reduce cloud infrastructure costs by identifying and reporting wasteful resource usage.
- To improve infrastructure hygiene by preventing the buildup of orphaned and forgotten resources.
- To send alerts via Slack or Email when unused resources are found, ensuring timely action.
- To generate clean, actionable reports to help DevOps teams make informed decisions about cloud resource usage.

## Tools and Technologies
- Python 3 – For scripting and automation logic.
- Boto3 (AWS SDK for Python) – To interact with AWS services like EC2, EBS, S3, ELB, etc.
- AWS IAM Roles & Credentials – To securely authenticate the script with AWS.
- Slack Webhooks / SMTP – For sending alerts via Slack or Email.
- YAML / JSON – For configuration files and resource thresholds.
- Cron (or Task Scheduler) – To schedule the script for regular execution (daily, weekly, etc.).
- CSV / JSON Logging – To export reports of unused resources.
- Git & GitHub – For version control and project hosting.

## Project Steps
Step 1: Install Python and Boto3

Step 2: Set Up AWS Credentials (IAM User and Access Keys)

Step 3: Create EC2 Checker Script

Step 4: Create EBS Volume Checker Script

Step 5: Create Elastic IP Checker Script

Step 6: Create S3 Bucket Usage Checker Script

Step 7: Generate Report of Unused Resources

Step 8: Send Alerts via Slack or Email

Step 9: Schedule the Script to Run Automatically

## Project Implementation

### Step 1: Install Python and Boto3
In this step, you prepare your system to start the project by:

i. Making sure Python (the language we'll use) is installed.

ii. Installing Boto3, which is the Python package that allows us to talk to AWS services
    like EC2, EBS, and S3.

- Download and Install Python
    - Go to the official Python download page:
      ```bash
      https://www.python.org/downloads/
      ```
    - Click “Download Python 3.13.5” (the latest version).
      <img width="923" height="383" alt="image" src="https://github.com/user-attachments/assets/6f754491-4aab-493a-841b-f66813885fc0" />

    - When the installer opens:
      
      Check the box that says; “Add Python to PATH”
      
    - Then click Install Now

      Wait for it to finish, then click Close

- Confirm installation by running the command;
  ```bash
  py –version
  ```
  <img width="691" height="163" alt="image" src="https://github.com/user-attachments/assets/e935536b-bd85-4a86-8d75-e319068003d7" />

- Now, let’s install boto3. This will install the AWS SDK for Python, which we’ll use to interact with EC2, EBS, and others. Run the command;
  ```bash
  py -m pip install boto3
  ```
   <img width="975" height="396" alt="image" src="https://github.com/user-attachments/assets/d42e2b01-4bb9-4e0f-b10e-b9b4e1a2275d" />


### Step 2: Set Up AWS Credentials (IAM User and Access Keys)
This step gives your Python script secure access to your AWS account using IAM access keys.
- Create an IAM User for Python in AWS Console
  - Go to IAM → Users → create user
  - Name it something like: aws-cleaner-bot
  - Enable Programmatic access only
  - Attach policy: AdministratorAccess (for project/testing purpose only; limit access in production)
  - Create access key. Download the .csv file with Access Key ID and Secret Access Key

- Configure AWS CLI on Your System. Run this command in your terminal aws configure

  Fill the following
    - Access Key ID: downloaded in your csv file
    - Secret Access Key: downloaded in your csv file
    - Default region name (e.g., us-east)
    - Default output format: json or table

- To confirm that your AWS CLI is properly configured, run the command
  ```bash
  aws configure list
  ```
  <img width="928" height="253" alt="image" src="https://github.com/user-attachments/assets/6bb247a5-861e-4067-830f-65e5921516dd" />

### Step 3: Create EC2 Checker Script

This step scans all AWS regions to find stopped EC2 instances that may still incur storage costs, helping identify unused resources for cleanup and cost savings.

- In your project folder, create a python file named ec2_checker.py
- Paste the below script in the just created ec2_checker.py file Script
  
  [EC2 Checker Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/ec2_checker.py)

  <img width="975" height="366" alt="image" src="https://github.com/user-attachments/assets/6a5b3914-ab79-4aa0-b0aa-3658df14f3ee" />










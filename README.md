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

#### Summary of what the script does
* Connects to AWS EC2.
* Scans all reachable regions dynamically.
* Lists stopped EC2 instances by Region, Instance ID, and Name.
* Helps detect unused instances for manual review or termination.
* Skips unreachable regions automatically to avoid script failure.



- To confirm our script runs properly, run the command;
  ```bash
  py ec2_checker.py
    ```
  <img width="748" height="155" alt="image" src="https://github.com/user-attachments/assets/cee20ea9-c274-4cd3-8ab6-237159b65e1a" />


### Step 4: Create EBS Volume Checker Script
This step scans all AWS regions for unattached EBS volumes, listing their IDs, sizes, and regions to help identify unused storage resources that still incur costs.
- In your project folder, create a python file named ebs_checker.py
- Paste the below script in the just created ebs_checker.py file
  
  [EBS Checker Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/ebs_checker.py)
  
  <img width="975" height="413" alt="image" src="https://github.com/user-attachments/assets/5c98d302-5c76-4bbb-80cd-eb222995201e" />

#### Summary of what the script does
* Connects to AWS EC2.
* Scans all reachable regions dynamically.
* Lists unattached EBS volumes by Region, Volume ID, and Size.
* Helps detect unused storage still incurring costs



- To confirm our script runs properly, run the command;
  ```bash
  py ebs_checker.py
  ```
  <img width="714" height="131" alt="image" src="https://github.com/user-attachments/assets/649892c7-3cf3-4f74-af20-1374524c8ea4" />

### Step 5: Create Elastic IP Checker Script
Elastic IPs are public IPv4 addresses that AWS charges for when they are allocated but not associated with a running instance. Unused Elastic IPs can quietly add to costs. This step creates a script to detect idle Elastic IPs across all regions for review and release.

- In your project folder, create a python file named elastic_ip_checker.py
- Paste the below script in the just created elastic_ip_checker.py file

  [Elastic IP Checker Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/elastic_ip_checker.py)

<img width="975" height="532" alt="image" src="https://github.com/user-attachments/assets/4e127fe4-daab-48c9-8af7-6ef35debd052" />

#### Summary of what the script does
* Connects to AWS EC2.
* Scans all reachable regions dynamically.
* Finds Elastic IPs not associated with any resource.
* Helps identify idle IPs that are still costing money.



- To confirm our script runs properly, run the command;
  ```bash
  py elastic_ip_checker.py
  ```
  <img width="823" height="134" alt="image" src="https://github.com/user-attachments/assets/1bb29e80-e235-40ef-beae-938e912964db" />

### Step 6: Create S3 Bucket Usage Checker Script
Amazon S3 buckets can remain unused for long periods, storing objects that are not accessed but still incur storage costs. This step creates a script to scan all S3 buckets, list their name, region, size, and last modified date, helping identify buckets that may be inactive or unnecessary.

- In your project folder, create a python file named s3_checker.py
- Paste the below script in the just created s3_checker.py file

  [S3 Checker Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/s3_checker.py)

  <img width="975" height="584" alt="image" src="https://github.com/user-attachments/assets/5b46e3b4-440d-42cf-afde-216a6c93b67c" />

#### Summary of what the script does
* Connects to AWS S3.
* Scans all buckets for activity.
* Flags buckets that are empty or inactive for >30 days.
* Helps detect unused storage to reduce costs.


- To confirm our script runs properly, run the command;
  ```bash
  py s3_checker.py
  ```
  <img width="722" height="148" alt="image" src="https://github.com/user-attachments/assets/706fca3f-783a-4774-abed-e0a1d8642b8b" />


### Step 7: Generate Report of Unused Resources
After identifying unused EC2 instances, unattached EBS volumes, idle Elastic IPs, and inactive S3 buckets, it’s important to compile the findings into a single report. This step focuses on generating a centralized CSV or text report containing all unused resources across AWS, making it easier to review, share with teams, and plan cost-saving actions.

- In your project folder, create a python file named generate_report.py
- Paste the below script in the just created generate_report.py file

  [Generate Report Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/generate_report.py)

  <img width="975" height="647" alt="image" src="https://github.com/user-attachments/assets/0cfda1dd-d586-40c8-9981-00ba8f681d4e" />
  

#### Summary of what the script does
##### Gather Results

Takes the findings from:
- EC2 Checker (all stopped instances)
- EBS Checker (all unattached volumes)
- Elastic IP Checker (all unused Elastic IPs)
- S3 Checker (all inactive buckets)

##### Combine Everything
- Puts all unused resources into one collection for easy reference.

##### Generate a Report File
- Creates a CSV file named unused_resources_report.csv.

##### Organize Data in the Report
Each row in the file will have:
- Resource type (EC2, EBS, Elastic IP, S3)
- Region or bucket name
- Resource ID or name
- Extra details (like size, inactivity days, or allocation ID)

##### Confirm Completion
- Shows a message on your terminal that the report is successfully generated and saved in your project folder.



- To confirm our script runs properly, run the command;
  ```bash
  py generate_report.py
  ```
  <img width="973" height="239" alt="image" src="https://github.com/user-attachments/assets/6e89879d-9927-4d0f-a40e-a5950c07d29b" />

  <img width="416" height="204" alt="image" src="https://github.com/user-attachments/assets/cc30138e-194e-4fe8-b3d7-fb5a85fd5b05" />


### Step 8: Send Alerts via Slack or Email
After generating a unified report of unused AWS resources, it’s important to alert relevant stakeholders so they can take action. This step focuses on sending an automated email notification with the report attached, ensuring that cost optimization findings are delivered promptly.

We would consider that there is already an existing Gmail account


#### Enable 2-Step Verification (One Time Only)
Google blocks scripts that log in with just your password unless you do this:

- Go to Google My Account – Security.
- Scroll to “Signing in to Google” → Turn ON "2-Step Verification".
- Verify with your phone number.
  
#### Create an App Password (One Time Only)
Go to Google App Passwords.
- Select:
    - App: Mail
    - Device: Windows Computer (or Other)
- Click Generate.
- Copy the 16-character password Google gives you.
  - Example: abcd efgh ijkl mnop
  - This will replace your normal password in the script.


- Create the Email script File named send_email_alert.py
- Paste the below script in the just created send_email_alert.py file

  [Send Email Alert Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/send_email_alert.py)

  <img width="975" height="301" alt="image" src="https://github.com/user-attachments/assets/e80f91b4-aa06-48fc-bdbf-ac35452a3bc8" />

- To confirm our script runs properly, run the command;
  ```bash
  py send_email_alert.py
  ```
  <img width="839" height="128" alt="image" src="https://github.com/user-attachments/assets/73f97679-25a0-4268-aff0-58107b35d53f" />

Email sent and received.


Now that we have configured our email, we would need to write a script so that once the report is generated, it would automatically send the email to us. To achieve this,

- Create a file named auto_report_email.py and paste the below script inside

  [Auto Report Email Script](https://github.com/Ogbunugafor-Philip/Automated-AWS-Resource-Cleanup-and-Cost-Optimization-Using-Python-Boto3-/blob/main/auto_report_email.py)

<img width="975" height="543" alt="image" src="https://github.com/user-attachments/assets/a434184b-4530-4bad-ab5c-34c85f40b0d6" />

Now, let us run the script to confirm everything works correctly. Run
```bash
py auto_report_email.py
```
<img width="975" height="269" alt="image" src="https://github.com/user-attachments/assets/f7327eb7-fd41-4f3e-9377-77faf3272857" />

<img width="975" height="100" alt="image" src="https://github.com/user-attachments/assets/fab27120-bfbf-4a46-b377-c5b9bccbafb7" />

Everything is successful, report generated, csv file created and email sent.


### Step 9: Schedule the Script to Run Automatically
This step sets up an automatic schedule for the AWS resource monitoring script to run at regular intervals (daily, weekly, or custom times). Automation ensures you receive alerts on unused resources without having to run the script manually each time.
Before we run the schedule, we would need to build our .bat script. A .bat script (Batch file) is a text file containing a list of commands that Windows executes automatically in the Command Prompt.

- Open Notepad and paste this code
  ```bash
  @echo off
  py auto_report_email.py
  pause
  ```
Save this with all file format and in the folder where you have your python scripts saved

#### Summary of Why this is needed and what it does
- Automates your Python script execution.
- Allows one-click operation.
- Enables Windows Task Scheduler automation.
  

- Test the just created .bat by going to the folder where you saved it and double clicking on in. It should run your python script in your command prompt

  <img width="975" height="235" alt="image" src="https://github.com/user-attachments/assets/3bdb5879-3456-4f76-a40c-155121aa3a32" />

Now, let us schedule our script

- Press Windows + R on your keyboard. Type:
  ```bash
  taskschd.msc
  ```
  then enter
  <img width="975" height="359" alt="image" src="https://github.com/user-attachments/assets/867bccd4-2a4c-4068-ad5f-cef57679f04d" />

The Task Scheduler window will open, showing your system's scheduled tasks.


#### Create a Basic Task. On the right panel, click Create Basic Task...
  A wizard will open:
  - Name: AWS_Report_Automation
  - Description: Generates a daily report of unused AWS resources
  - Click Next.
  - Select Daily (recommended for regular AWS checks).
  - Click Next.
    
#### On the next screen:
   - Set the Start date and time (e.g., 08:00 AM).
   - Ensure Recur every: 1 days is selected.
   - Click Next to proceed.
   - Keep "Start a program" selected (this allows you to run your Python script).
   - Click Next.

#### On the next screen:
   - Program/script → cmd.exe
   - Add arguments → /c "C:\Users\SURFACE PRO 7PLUS\Python-\run_aws_report.bat"
   - Start in → C:\Users\SURFACE PRO 7PLUS\Python-
   - Click next and the click finish


Now, we need to test our scheduler to confirm its working correctly
- Press Windows + R on your keyboard. Type:
  ```bash
  taskschd.msc
  ```
  then enter

- Select the AWS Automation just created and click run
  <img width="975" height="462" alt="image" src="https://github.com/user-attachments/assets/c1e70f8f-4a2f-4fa5-82f2-74b394cb449b" />

- Outcome of the test
  <img width="975" height="401" alt="image" src="https://github.com/user-attachments/assets/e8db57bc-4ad3-4cf9-9532-8f33f9e9d922" />

  <img width="975" height="291" alt="image" src="https://github.com/user-attachments/assets/a9dcc624-6ea4-4d43-b99f-3033ecd66b0d" />

Everything is successful, report generated, csv file created and email sent.


### Conclusion
This project successfully demonstrates how to automate AWS cost optimization by identifying unused cloud resources and sending timely alerts. Through a combination of Python scripts, Boto3 for AWS interactions, and email notifications, the solution enables proactive resource monitoring and cost savings. The addition of a .bat file and Windows Task Scheduler ensures the entire process runs automatically without manual intervention, making it a reliable and scalable approach for continuous cloud resource management.











  

























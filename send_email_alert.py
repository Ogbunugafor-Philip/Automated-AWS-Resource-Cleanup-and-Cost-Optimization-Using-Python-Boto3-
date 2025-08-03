import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- CONFIGURATION ---
sender_email = "eloraosita@gmail.com"           # Your Gmail address
app_password = "bxtj kdnr scqk tuam"            # Your Gmail App Password
receiver_email = "pogbunugafor@gmail.com"       # Recipient email address
subject = "AWS Cost Optimization Report"
body = "Hello,\n\nPlease find attached the latest AWS unused resources report.\n\nRegards,\nAWS Monitoring Bot"

# --- CREATE EMAIL ---
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Attach the CSV file
filename = "unused_resources_report.csv"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")
message.attach(part)

# --- SEND EMAIL ---
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls(context=context)
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("✅ Email sent successfully with the AWS unused resources report!")

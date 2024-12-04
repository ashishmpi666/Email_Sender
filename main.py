import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(to_email, subject, body, attachment_path, sender_email, sender_password):
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Add the body
        message.attach(MIMEText(body, 'plain'))

        # Add the attachment
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={attachment_path.split("/")[-1]}'
            )
            message.attach(part)

        # Connect to the server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Sender details
sender_email = "email"
sender_password = "your-password"

# Email details
recipients = [
""
]

subject = "Immediate Joiner | Java Full Stack Developer | Backend & Frontend Expertise"
body = """" 

Hi,

I am Ashish Singh, a Software Engineer with 2.5 years of experience in Java, Spring Boot, Angular, MySQL, Git, and TypeScript. At Infosys, I built enterprise applications with robust backends and dynamic frontends.

I am actively seeking new opportunities and available to join immediately. Key details:

Experience: 2.5 years
Location: Pune, Maharashtra
Notice Period: Immediate

Thank you for your time and consideration.

Best regards,
Ashish Singh
Mob: 6397646869
    """
attachment_path = "C:/Users/abhis/Downloads/Ashish_Resume.pdf"


# Send emails to each recipient
for recipient in recipients:
    send_email(recipient, subject, body, attachment_path, sender_email, sender_password)

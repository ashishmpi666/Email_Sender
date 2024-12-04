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
sender_email = "ashishmpi00012@gmail.com"
sender_password = "jfwy omgq gyca nrtd"

# Email details
recipients = [
    # "careers@appsteamtechnologies.com",
    # "sandhyav9823@gmail.com",
    # "ankit.malik@vlinkinfo.com",
    # "muskan.tiwari@myvirtualteams.com",
    # "sujana.s@twsol.com",
    # "kshitij.wairagade@techbulls.com",
    # "prakiran@teksystems.com",
    # "sarvagya.upadyay@mphatek.com",
    # "laxmanchavan014@gmail.com",
    # "parul.c@otomeyt.ai",
    # "aswinirout@kpmg.com",
    # "deepak.salwan@stova.io",
    # "trupti@jforcesolutions.com",
    # "neha.gupta02@irissoftware.com",
    # "sahla.rahim@antal.com",
    # "taniya.cn@ellow.io",
    # "mkushwaha@teksystems.com",
    # "vinay@tanishasystems.com",
    # "sranganathan11494@altimetrik.com",
    # "lokesh.b@eslabs.net",
    # "yuvraj.kumawat@impetus.com",
    # "nandamath097@gmail.com",
    # "nanda.n@tidalsoftt.com",
    # "soumya@qpactsolutions.com",
    # "rani@srivensys.com",
    # "arvind@technodeedsolutions.com",
    # "bshanspal@gmail.com",
    # "swapna.sayagoni@appitsoftware.com",
    # "contact@techstack.se",
    # "deepika.sharma@nisvan.co.in",
    # "srishti@rediansoftware.com",
    # "talent@rediansoftware.com",
    # "anoop.pv@njclabs.com",
    # "ramadevi.gedela@vantagerms.com",
    # "himanshu.jain@nlbtech.in",
    # "talentsupport@fastlinejobs.net",
    # "srajendran@sageitinc.net",
    # "panpatidar180@gmail.com",
    # "poojyata@peoplestaff.in",
    # "santosh.kumar@amanziconsulting.co.in",
    # "supriya.waghmare@bluethinkinc.com",
    # "hr@durapid.com",
    # "swati.gaur@hirextream.com",
    # "recruitment@elpopulo.com",
    # "pavithra.s@xforia.com",
    # "sofia.safa@sonata-software.com",
    # "harshitha.krishnan@careernet.in",
    # "rajiv.singh@encora.com",
    # "bansalitadvisory@gmail.com",
    # "aisha.nurbasha@sysintelli.com",
    # "talent.acquisition@qpactsolutions.com",
    # "sharmistha.d@twsol.com",
    # "madhu@exceltechcomputers.com",
    # "amrita.kumari@hnmsolutions.eu",
    # "alphabitinfoway2018@gmail.com",
    # "rmishra@deqode.com",
    # "shalini.garya@centific.com",
    # "madhavi.naik@alikethoughts.com",
    # "srivastava.19.acs@gmail.com",
    # "gaurav.saxena@zodiac-solutions.com",
    # "soham.barot@spec-india.com",
    # "praveen.tmvus@gmail.com",
    # "nehaljain@msgclub.co.in",
    # "subharanjan@infininza.com",
    # "boomika.s@xforia.com",
    # "jyothi.a@episdata.com",
    # "sakthivel.mahendran@wipro.com",
    # "mishratanu2222@gmail.com"

    "abhisheksinha5066@gmail.com"
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
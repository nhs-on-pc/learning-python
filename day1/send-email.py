# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "nguyenhaison18@gmail.com"
toaddr = "nhs.vnu@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Email từ nguyenhaison18@gmail.com"

# string to store the body of the mail
body = "<h1>This is Ferarrio from Australia</h1>"

# attach the body with the msg instance
# msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(body, 'html'))

# open the file to be sent
filename = "Ferrario.jpg"
attachment = open("D:\\learning-python\\source data\\sample\\Ferrario.jpg", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)


# Converts the Multipart msg into a string
text = msg.as_string()


try:
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "logitechg400s")  # cho password xịn vào đây
    s.sendmail(fromaddr, toaddr, text)
    print('email sent')
except Exception as error:
    print(f'Error sending mail \n {error}')
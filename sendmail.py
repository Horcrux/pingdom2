import smtplib
from email.mime.text import MIMEText

            #from, subject, body, recipients
def sendmail(sender,subject,body,recipients):
    # me == the sender's email address
    # you == the recipient's email address
    msg=MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost', 25)
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()

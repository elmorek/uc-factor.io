import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(self, server=None, sender=None, destination=None, subject=None, body=None):
    for i in [server, sender, destination, subject, body]:
        if i is not isinstance(i, str):
            raise TypeError('{} is not a string'.format(i))
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = destination
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s = smtplib.SMTP(server)
    try:
        s.sendmail(sender.destination, text)
    except smtplib.SMTPException as e:
        raise e
    s.quit()

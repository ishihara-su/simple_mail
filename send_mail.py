# send_mail.py - simple SMTP client in python 3
#    Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#
import smtplib
from email.message import EmailMessage
import sys

def prompt(prompt):
    return input(prompt).strip()

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} smtp_server", file=sys.stderr)
smtp_server_name = sys.argv[1]

from_addr = prompt("From: ")
to_addrs = prompt("To: ").split()
subject = prompt("Subject: ")
print("Enter message, and with EOF (^D: Unix, ^Z: Windows) or a blank line: ")

msg_body = ''
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg_body += line

msg = EmailMessage()
msg.set_content(msg_body)
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = ', '.join(to_addrs)

s = smtplib.SMTP(smtp_server_name)
s.send_message(msg)
s.quit()

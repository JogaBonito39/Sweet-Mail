import os
from email.message import EmailMessage
import ssl
import smtplib
import datetime as dt
import time
import io


email_sender = #os.environ.get("EMAIL_SENDER")
email_password = #os.environ.get("EMAIL_PASSWORD")
email_receiver = #os.environ.get("EMAIL_RECEIVER")  

subject = "Morning From Sweet Mail"

#--get rid of double quotation marks
with io.open("lovely messages.txt", "r", encoding='utf-8-sig') as f:
    #f_contents = f.readline()
    lines = f.readlines()

quotless_lines_list = []
for line in lines:
    quotless_lines=line.replace('"','')
    quotless_lines_list.append(quotless_lines)
#print(quotless_lines_list)

with io.open("lovely messages.txt", "w",encoding='utf-8-sig') as f:
    for qline in quotless_lines_list:
        f.write(qline)
        

#--send single messages and quote from both text files and then removing them from the files
with io.open("lovely messages.txt", "r",encoding='utf-8-sig') as f:
    f_lovely_contents = f.readline()
    lovely_lines = f.readlines()

with io.open("quotes.txt", 'r',encoding='utf-8-sig') as f:
    f_quotes_contents = f.readline()
    quotes_lines = f.readlines()

#print(f_lovely_contents+"\nToday's motivational quote:\n"+f_quotes_contents)

with io.open("lovely messages.txt", "w",encoding='utf-8-sig') as f:
    for line in lovely_lines:
        if line.strip("\n") != f_lovely_contents:
            f.write(line)

with io.open("quotes.txt", "w",encoding='utf-8-sig') as f:
    for line in quotes_lines:
        if line.strip("\n") != f_quotes_contents:
            f.write(line)
     
body = f"""
Good morning! 🌞

{f_lovely_contents}
Today's motivational quote:
{f_quotes_contents}
--
Warmly, 
Sweet Mail
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

#use pickle to save and then access the file the next day with updated variables
time_var = dt.datetime.now()

year = time_var.year
month = time_var.month
day = time_var.day
hour = time_var.hour
minute = time_var.minute
second = time_var.second
#send_time = dt.datetime(year, month, day+1, 8, 0, 0)

send_time = dt.datetime(year, month, day, hour, minute, second+3)

current_time = dt.datetime.now()
time.sleep(send_time.timestamp() - current_time.timestamp())
#print(v)
#print("complete!")

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #465 587
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("email sent")


#--




'''
algo:-
1. import smtplib
2. open mail connection(mail port no.)
3. login using username and password
4. send mail
5. close connection
'''

import smtplib as m

sender_id = "hixeyi4732@qmailers.com"
password = ""
receiver_id = "hixeyi4732@qmailers.com"

con = m.SMTP("SMTP.https://temp-mail.org/en/.com",587)
con.starttls()
con.login(sender_id,password)
msg = "ur history is public/n now ur ass is whooped"
con.sendmail(sender_id,receiver_id,msg)
print("mail sent")
con.close()



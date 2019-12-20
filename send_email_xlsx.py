import smtplib
import codecs
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def send_email_xlsx(sender, receivers, sub, msg):

	today = datetime.now()
	subject = '[' + sub + ']' +  ' Overdue Loan Reminder ' + today.strftime('%Y-%m-%d')

	msg.reset_index(drop=True, inplace=True)
	msg_html = msg.to_html()
	with open(subject+'.html', "w", encoding="utf-8") as file:
		file.write(msg_html)

	f=codecs.open(subject+'.html', 'r', encoding="utf-8")
	
	html = """\
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>儀器催還</title>
<body>
<div id="container">
  <p><strong>Hi """+ sub +""",</p>
  <p><strong>以下設備已逾期，請業務盡速與客戶聯繫，謝謝</strong></p>
  <div id="content">
  """+ f.read() + """
  </div>
</div>
</div>
</body>
</html>
        """
	message = MIMEText(html, 'html')
	message['Subject'] = subject

	try:
		#print(message.as_string())
		smtpObj = smtplib.SMTP('devmail.natinst.com')
		#smtpObj = smtplib.SMTP("smtp.gmail.com:587")
		smtpObj.sendmail(sender, receivers, message.as_string())
		smtpObj.quit() 
		print ("Sent successfully")
		f.close()
		os.remove(subject+'.html')
	except smtplib.SMTPException as e:
		smtpObj.quit() 
		print ("Error: not sent, reason:",e)
		f.close()
		os.remove(subject+'.html')

if __name__ == '__main__':
	send_email('welly180@gmail.com',['welly.huang@ni.com'],'testing title',['test content'])
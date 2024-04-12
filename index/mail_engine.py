import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail_Engine:
	def __init__(self):
		self.from_="sarusmandu92@gmail.com"

	
	def envoyer_email(self,objet, message, destinataire):
		msg = MIMEMultipart()
		msg['From'] = self.from_
		msg['To'] = destinataire
		msg['Subject'] = objet
		msg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()  
		server.login(self.from_, self.password)
		text = msg.as_string()  
		server.sendmail(self.from_, destinataire, text)
		server.quit()  

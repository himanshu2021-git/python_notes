# kivy imports
from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

#functionality imports
import smtplib as mail
import threading as th

# MODULES FOR EMAIL PREPARTIONS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class ScManager(ScreenManager):pass
sm = ScManager()

class EmailComposer(Screen):
	file = None
	def send(self,from_email=0,to_email=0,pswrd=0,matter=0):
		print(EmailComposer.file)
		if EmailComposer.file == None:
			try:
				#create connection
				self.status.text ="Creating Connection with Server"
				server = mail.SMTP(host="smtp.gmail.com",port=587)
					
				#enable security
				self.status.text ="Enabling the Security Layers"
				server.starttls()
				server.ehlo()
			
				#login
				self.status.text ="Loggin in to the Account"
				server.login(
					from_email,
					pswrd
				)
				
				#send email
				self.status.text = "Email Sending"
				server.sendmail(
					from_email,
					to_email,
					matter
				)
				
				#logout
				server.quit()
				self.status.text = "Email Sent"
			except Exception as e:
				self.status.text = str(e)
			else:
				self.from_email.text = "From Email"
				self.to_email.text = "To Email"
				self.matter.text = "Enter Msg Here..."
				self.pswrd.text = "Enter Password"
		else:
			#create connection
			self.status.text ="Creating Connection with Server"
			server = mail.SMTP(host="smtp.gmail.com",port=587)
				
			#enable security
			self.status.text ="Enabling the Security Layers"
			server.starttls()
			server.ehlo()
			#login
			self.status.text ="Loggin in to the Account"
			server.login(
				from_email,
				pswrd
			)
			# creating email
			msg = MIMEMultipart()
			msg['From'] = from_email
			msg['To'] = to_email
			msg['Subject'] = "PYTHON TESTING EMAILS"
			body = matter
			msg.attach(MIMEText(body,'plain'))
			# attaching a file
			file = open(EmailComposer.file,"rb") # opening a file
			p = MIMEBase("application",'octet-stream')	
			p.set_payload((file).read())
			encoders.encode_base64(p)
			p.add_header('Content-Disposition','attachment; filename=%s'%file.name.split("\\")[-1])
			msg.attach(p)
			text = msg.as_string()
			server.sendmail(
				from_email, # from email address
				[to_email], # list of to emails list
				text
			)

	
	def sendbythread(self,from_email,to_email,pswrd,matter):
		thread = th.Thread(
			target = self.send,
			args = (from_email,to_email,pswrd,matter,),
			name = "EmailSender"
		)
		thread.start()
#obj = EmailComposer()

#obj.send()
kv = Builder.load_file("mainscreen.kv")
class FileChoose(Screen):
	def find(self):
		#print(self.choosen_file)
		#print(dir(self.choosen_file))
		#print(self.choosen_file.selection)
		#print(dir(self.choosen_file.selection))
		try:
			EmailComposer.file = self.choosen_file.selection[0]
		except:
			EmailComposer.file = None
			sm.current="email"
		else:
			sm.current="email"





sm.add_widget(EmailComposer(name = "email"))
sm.add_widget(FileChoose(name = "file"))
sm.current = "email"


class MainScreen(App):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.title = "PYTHON EMAIL COMPOSER"
	def build(self):
		return sm

if __name__ == "__main__":
	MainScreen().run()
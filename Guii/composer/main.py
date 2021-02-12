# kivy imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#functionality imports
import smtplib as mail
import threading as th

class EmailComposer(BoxLayout):
	def send(self,from_email=0,to_email=0,pswrd=0,matter=0):
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
			self.status.text = str(e[:50])
		else:
			self.from_email.text = "From Email"
			self.to_email.text = "To Email"
			self.matter.text = "Enter Msg Here..."
			self.pswrd.text = "Enter Password" 
	
	def sendbythread(self,from_email,to_email,pswrd,matter):
		thread = th.Thread(
			target = self.send,
			args = (from_email,to_email,pswrd,matter,),
			name = "EmailSender"
		)
		thread.start()
#obj = EmailComposer()

#obj.send()

class MainScreenApp(App):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.title = "PYTHON EMAIL COMPOSER"
	def build(self):
		return EmailComposer()

if __name__ == "__main__":
	MainScreenApp().run()

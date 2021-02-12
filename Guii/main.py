from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class EmailComposer(BoxLayout):
	def send(self,from_email,to_email,matter):
		print(from_email,to_email,matter)

class MainScreenApp(App): #app suffix is mandatory
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.title="Email Composer"
	def build(self):
		return EmailComposer()

if __name__=="__main__":
	MainScreenApp().run()

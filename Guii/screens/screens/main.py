from kivy.app import App

from kivy.uix.screenmanager import Screen,ScreenManager

from kivy.lang import Builder

class Screen1(Screen):pass

class Screen2(Screen):pass

class Screen3(Screen):pass

class ScManager(ScreenManager):pass

#LINK THE KIVY FILE

kv = Builder.load_file('design.kv')

sm = ScManager()

# ADDED ALL THE SCREENS INTO THE SCREEN MANAGER
sm.add_widget(Screen1(name="sc1"))
sm.add_widget(Screen2(name="sc2"))
sm.add_widget(Screen3(name="sc3"))

sm.current = "sc1"

class MyApplication(App):
	def build(self):
		return sm


if __name__ == "__main__":
	MyApplication().run()


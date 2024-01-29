from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from datetime import datetime

class Container(FloatLayout):
	
	text_input = ObjectProperty()
	label_widget = ObjectProperty()
	time_widget = ObjectProperty()
	
	date_time = datetime.now()
	time_widget.text = str(datetime.now())
	
	def change_label(self):
		self.label_widget.text = self.text_input.text
		
	def clear_label(self):
		self.label_widget.text = ''
		self.text_input.text = ''
	
class myApp_2(App):
	def build(self):
		return Container()
		
if __name__ == '__main__':
	myApp_2().run()
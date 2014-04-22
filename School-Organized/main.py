from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder

class RootWidget(TabbedPanel):
    monday = ObjectProperty(None)
    tuesday = ObjectProperty(None)
    wednesday = ObjectProperty(None)
    thursday = ObjectProperty(None)
    friday = ObjectProperty(None)
    text1 = '1'
    text2 = '2'
    text3 = '3'
    text4 = '4'
    text5 = '5'
    label1 = ObjectProperty(None)
    label2 = ObjectProperty(None)
    label3 = ObjectProperty(None)
    label4 = ObjectProperty(None)
    label5 = ObjectProperty(None)
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    MainApp().run()

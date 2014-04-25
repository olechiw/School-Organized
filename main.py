from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from pickle import load, dump
from kivy.uix.button import Button
from kivy.uix.label import Label
class RootWidget(TabbedPanel):
    opened = False
    try:
        tmp = open('data', 'r')
        opened=True
    except: pass
    if opened:
        data = load(tmp)
        tmp.close()
    else:
        data = {'Monday':[['First Hour', '', '', '', '', """"""],['Second Hour', '', '', '', '', """"""],['Third Hour','','','','',""""""],['Fourth Hour','','','','',""""""],['Fifth Hour','','','','',""""""]],
                'Tuesday':[['First Hour', '', '', '', '', """"""],['Second Hour', '', '', '', '', """"""],['Third Hour','','','','',""""""],['Fourth Hour','','','','',""""""],['Fifth Hour','','','','',""""""]],
                'Wednesday':[['First Hour', '', '', '', '', """"""],['Second Hour', '', '', '', '', """"""],['Third Hour','','','','',""""""],['Fourth Hour','','','','',""""""],['Fifth Hour','','','','',""""""]],
                'Thursday':[['First Hour', '', '', '', '', """"""],['Second Hour', '', '', '', '', """"""],['Third Hour','','','','',""""""],['Fourth Hour','','','','',""""""],['Fifth Hour','','','','',""""""]],
                'Friday':[['First Hour', '', '', '', '', """"""],['Second Hour', '', '', '', '', """"""],['Third Hour','','','','',""""""],['Fourth Hour','','','','',""""""],['Fifth Hour','','','','',""""""]]}
    def edit(self,label,day,hour):
        self.label = label
        self.day = day
        self.hour = hour
        self.editback = BoxLayout(orientation='vertical')
        self.label1 = Label(text='Assignment')
        self.label2 = Label(text='Duedate')
        self.label3 = Label(text= 'Assignment')
        self.label4 = Label(text='Duedate')
        self.label5 = Label(text='Class Name')
        self.hour_name = TextInput(text_hint='Class Name',text=self.data[day][hour][0],multiline=False)
        self.assignment1in = TextInput(text_hint='Assignment',text=self.data[day][hour][1],multiline=False)
        self.assignment2in = TextInput(text_hint='Assignment',text=self.data[day][hour][3],multiline=False)
        self.duedate1in = TextInput(text_hint='Duedate',text=self.data[day][hour][2],multiline=False)
        self.duedate2in = TextInput(text_hint='Duedate',text=self.data[day][hour][4],multiline=False)
        self.okbutton = Button(text='Ok')
        self.cancelbutton = Button(text='Cancel')
        self.editback.add_widget(self.label5)
        self.editback.add_widget(self.hour_name)
        self.editback.add_widget(self.label1)
        self.editback.add_widget(self.assignment1in)
        self.editback.add_widget(self.label2)
        self.editback.add_widget(self.duedate1in)
        self.editback.add_widget(self.label3)
        self.editback.add_widget(self.assignment2in)
        self.editback.add_widget(self.label4)
        self.editback.add_widget(self.duedate2in)
        self.editback.add_widget(self.okbutton)
        self.editback.add_widget(self.cancelbutton)
        self.popup = Popup(content=self.editback,auto_dismiss=False,size_hint=(.75,.75),title='Edit')
        self.okbutton.bind(on_press=self.dismissok)
        self.cancelbutton.bind(on_press=self.popup.dismiss)
        self.popup.open()
    def dismissok(self,instance):
        self.data[self.day][self.hour][0] = self.hour_name.text
        self.data[self.day][self.hour][1] = self.assignment1in.text
        self.data[self.day][self.hour][2] = self.duedate1in.text
        self.data[self.day][self.hour][3] = self.assignment2in.text
        self.data[self.day][self.hour][4] = self.duedate2in.text
        self.label.text = self.data['Monday'][0][0] + '\n' + self.data['Monday'][0][1] + ' ' + self.data['Monday'][0][2] + '\n' + self.data['Monday'][0][3] + ' ' + self.data['Monday'][0][4]
        data = open('data','w')
        dump(self.data,data)
        data.close()
        self.popup.dismiss()
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__' or '__android__':
    MainApp().run()
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from pickle import load, dump

class RootWidget(TabbedPanel):
    opened = False
    try:
        myfile = open('data', 'r')
        opened = True

        text11,text12,text13,text14,text15=data['Monday']
        text21,text22,text23,text24,text25=data['Tuesday']
        text31,text32,text33,text34,text35=data['Wednesday']
        text41,text42,text43,text44,text45=data['Thursday']
        text51,text52,text53,text54,text55=data['Friday']

    except:
        pass
    if opened:
        data = load(myfile)
        myfile.close()
    else:
        data = {'Monday':[["First Hour",'','','','',""""""],["Second Hour", '', '', '', '', """"""],["Third Hour",'','','','',""""""],["Fourth Hour",'','','','',""""""],["Fifth Hour",'','','','',""""""]], 'Tuesday':[["First Hour",'','','','',""""""],["Second Hour",'','','','',""""""],["Third Hour",'','','','',""""""],["Fourth Hour",'','','','',""""""],["Fifth Hour",'','','','',""""""]], 'Wednesday':[["First Hour",'','','','',""""""],["Second Hour",'','','','',""""""],["Third Hour",'','','','',""""""],["Fourth Hour",'','','','',""""""],["Fifth Hour",'','','','',""""""]], 'Thursday':[["First Hour",'','','','',""""""],["Second Hour",'','','','',""""""],["Third Hour",'','','','',""""""],["Fourth Hour",'','','','',""""""],["Fifth Hour",'','','','',""""""]], 'Friday':[["First Hour",'','','','',""""""],["Second Hour",'','','','',""""""],["Third Hour",'','','','',""""""],["Fourth Hour",'','','','',""""""],["Fifth Hour",'','','','',""""""]]}

        text11,text12,text13,text14,text15=data['Monday']
        text21,text22,text23,text24,text25=data['Tuesday']
        text31,text32,text33,text34,text35=data['Wednesday']
        text41,text42,text43,text44,text45=data['Thursday']
        text51, text52, text53, text54, text55=data['Friday']

    editback = BoxLayout(orientation='vertical')
    editlabels.add_widget(Label(text='Class Name'))
#     editlabels.add_widget(Assignment)
#     editlabels.add_widget(Duedate)
#     editlabels.add_widget(Assignement)
#     editlabels.add_widget(Duedate)

    monday = ObjectProperty(None)
    tuesday = ObjectProperty(None)
    wednesday = ObjectProperty(None)
    thursday = ObjectProperty(None)
    friday = ObjectProperty(None)
    label11 = ObjectProperty(None)
    label12 = ObjectProperty(None)
    label13 = ObjectProperty(None)
    label14 = ObjectProperty(None)
    label15 = ObjectProperty(None)
    label21 = ObjectProperty(None)
    label22 = ObjectProperty(None)
    label23 = ObjectProperty(None)
    label24 = ObjectProperty(None)
    label25 = ObjectProperty(None)
    label31 = ObjectProperty(None)
    label32 = ObjectProperty(None)
    label33 = ObjectProperty(None)
    label34 = ObjectProperty(None)
    label35 = ObjectProperty(None)
    label41 = ObjectProperty(None)
    label42 = ObjectProperty(None)
    label43 = ObjectProperty(None)
    label44 = ObjectProperty(None)
    label45 = ObjectProperty(None)
    label51 = ObjectProperty(None)
    label52 = ObjectProperty(None)
    label53 = ObjectProperty(None)
    label54 = ObjectProperty(None)
    label55 = ObjectProperty(None)
    edit11 = ObjectProperty(None)
    edit12 = ObjectProperty(None)
    edit13 = ObjectProperty(None)
    edit14 = ObjectProperty(None)
    edit15 = ObjectProperty(None)
    edit21 = ObjectProperty(None)
    edit22 = ObjectProperty(None)
    edit23 = ObjectProperty(None)
    edit24 = ObjectProperty(None)
    edit25 = ObjectProperty(None)
    edit31 = ObjectProperty(None)
    edit32 = ObjectProperty(None)
    edit33 = ObjectProperty(None)
    edit34 = ObjectProperty(None)
    edit35 = ObjectProperty(None)
    edit41 = ObjectProperty(None)
    edit42 = ObjectProperty(None)
    edit43 = ObjectProperty(None)
    edit44 = ObjectProperty(None)
    edit45 = ObjectProperty(None)
    edit51 = ObjectProperty(None)
    edit52 = ObjectProperty(None)
    edit53 = ObjectProperty(None)
    edit54 = ObjectProperty(None)
    edit55 = ObjectProperty(None)

    def edit(self, label, day):
        hr = label.text[:2]
        if hr is 'fir': data_tmp = self.data[day][0]
        elif hr is 'sec': data_tmp = self.data[day][1]
        elif hr is 'thi': data_tmp = self.data[day][2]
        elif hr is 'fou': data_tmp = self.data[day][3]
        elif hr is 'fif': data_tmp = self.data[day][4]
        hour_name = TextInput(text=data_tmp[0])
        assignment1 = TextInput(text_hint='Assignment')
        assignment2 = TextInput(text_hint='Assignment')
        duedate1 = TextInput(text_hint='DueDate')
        duedate2 = TextInput(text_hint='DueDate')
        cancelbutton = Button(text='Cancel')
        okbutton = Button(text='Ok')


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    MainApp().run()

from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from pickle import load, dump
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class RootWidget(TabbedPanel):

    day3 = map(str,range(1,32))
    month = map(str,range(1,13))
    year = map(str,range(2014,2051))

    opened = False
    try:
        tmp = open('data', 'r')
        opened=True
    except: pass
    if opened:
        data = load(tmp)
        tmp.close()
    else:
        data = {'Monday':[['First Hour', 'Assignment', 'Month/Day/Year',
                            'Assignment', 'Month/Day/Year', """"""],
                          ['Second Hour', 'Assignment', 'Month/Day/Year',
                            'Assignment', 'Month/Day/Year', """"""],
                          ['Third Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""],
                          ['Fourth Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""],
                          ['Fifth Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""]],
                'Tuesday':[['First Hour', 'Assignment', 'Month/Day/Year',
                             'Assignment', 'Month/Day/Year', """"""],
                           ['Second Hour', 'Assignment', 'Month/Day/Year',
                             'Assignment', 'Month/Day/Year', """"""],
                           ['Third Hour','Assignment','Month/Day/Year',
                            'Assignment','Month/Day/Year',""""""],
                           ['Fourth Hour','Assignment','Month/Day/Year',
                            'Assignment','Month/Day/Year',""""""],
                           ['Fifth Hour','Assignment','Month/Day/Year',
                            'Assignment','Month/Day/Year',""""""]],
                'Wednesday':[['First Hour', 'Assignment', 'Month/Day/Year',
                               'Assignment', 'Month/Day/Year', """"""],
                             ['Second Hour', 'Assignment', 'Month/Day/Year',
                               'Assignment', 'Month/Day/Year', """"""],
                             ['Third Hour','Assignment','Month/Day/Year',
                              'Assignment','Month/Day/Year',""""""],
                             ['Fourth Hour','Assignment','Month/Day/Year',
                              'Assignment','Month/Day/Year',""""""],
                             ['Fifth Hour','Assignment','Month/Day/Year',
                              'Assignment','Month/Day/Year',""""""]],
                'Thursday':[['First Hour', 'Assignment', 'Month/Day/Year',
                              'Assignment', 'Month/Day/Year', """"""],
                            ['Second Hour', 'Assignment', 'Month/Day/Year',
                              'Assignment', 'Month/Day/Year', """"""],
                            ['Third Hour','Assignment','Month/Day/Year',
                             'Assignment','Month/Day/Year',""""""],
                            ['Fourth Hour','Assignment','Month/Day/Year',
                             'Assignment','Month/Day/Year',""""""],
                            ['Fifth Hour','Assignment','Month/Day/Year',
                             'Assignment','Month/Day/Year',""""""]],
                'Friday':[['First Hour', 'Assignment', 'Month/Day/Year',
                            'Assignment', 'Month/Day/Year', """"""],
                          ['Second Hour', 'Assignment', 'Month/Day/Year',
                            'Assignment', 'Month/Day/Year', """"""],
                          ['Third Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""],
                          ['Fourth Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""],
                          ['Fifth Hour','Assignment','Month/Day/Year',
                           'Assignment','Month/Day/Year',""""""]]}

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

        self.hour_name = TextInput(text_hint='Class Name',
                                   text=self.data[day][hour][0],
                                   multiline=False)
        self.assignment1in = TextInput(text_hint='Assignment',
                                       text=self.data[day][hour][1],
                                       multiline=False)
        self.assignment2in = TextInput(text_hint='Assignment',
                                       text=self.data[day][hour][3],
                                       multiline=False)
        self.duedate1in = TextInput(text_hint='Duedate',
                                    text=self.data[day][hour][2],
                                    multiline=False)
        self.duedate2in = TextInput(text_hint='Duedate',
                                    text=self.data[day][hour][4],
                                    multiline=False)

        duedate1in = BoxLayout(orientation='horizontal')
        duedate2in = BoxLayout(orientation='horizontal')
        self.day1 = Spinner(text=self.data[day][hour][2].split('/')[0],
                            values=tuple(self.day3),
                            size_hint_x=.75,
                            pos_hint={'center_x':.5,'center_y':.5})
        self.day2 = Spinner(text=self.data[day][hour][4].split('/')[0],
                            values=tuple(self.day3),
                            size_hint_x=.75,
                            pos_hint={'center_x':.5,'center_y':.5})
        self.month1 = Spinner(text=self.data[day][hour][2].split('/')[1],
                              values=tuple(self.month),
                              size_hint_x=.75,
                              pos_hint={'center_x':.5,'center_y':.5})
        self.month2 = Spinner(text=self.data[day][hour][4].split('/')[1],
                              values=tuple(self.month),
                              size_hint_x=.75,
                              pos_hint={'center_x':.5,'center_y':.5})
        self.year1 = Spinner(text=self.data[day][hour][2].split('/')[2],
                             values=tuple(self.year),
                             size_hint_x=.75,
                             pos_hint={'center_x':.5,'center_y':.5})
        self.year2 = Spinner(text=self.data[day][hour][4].split('/')[2],
                             values=tuple(self.year),
                             size_hint_x=.75,
                             pos_hint={'center_x':.5,'center_y':.5})
        duedate1in.add_widget(self.day1)
        duedate1in.add_widget(self.month1)
        duedate1in.add_widget(self.year1)
        duedate2in.add_widget(self.day2)
        duedate2in.add_widget(self.month2)
        duedate2in.add_widget(self.year2)
        self.okbutton = Button(text='Ok',
                            size_hint_x=.75,
                            pos_hint={'center_x':.5,'center_y':.5})
        self.cancelbutton = Button(text='Cancel',
                            size_hint_x=.75,
                            pos_hint={'center_x':.5,'center_y':.5})
        self.editback.add_widget(self.label5)
        self.editback.add_widget(self.hour_name)
        self.editback.add_widget(self.label1)
        self.editback.add_widget(self.assignment1in)
        self.editback.add_widget(self.label2)
        self.editback.add_widget(duedate1in)
        self.editback.add_widget(self.label3)
        self.editback.add_widget(self.assignment2in)
        self.editback.add_widget(self.label4)
        self.editback.add_widget(duedate2in)
        self.editback.add_widget(self.okbutton)
        self.editback.add_widget(self.cancelbutton)

        self.popup = Popup(content=self.editback,auto_dismiss=False,
                           size_hint=(.75,.75),title='Edit')
        self.okbutton.bind(on_press=self.dismissok)
        self.cancelbutton.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def dismissok(self,instance):

        self.data[self.day][self.hour][0] = self.hour_name.text
        if (self.day1.text != 'Day') and (self.month1.text != 'Month') and (self.year1.text != 'Year'):
             self.data[self.day][self.hour][1] = self.assignment1in.text

        if self.assignment1in.text and (self.day1.text != 'Day') and (self.month1.text != 'Month') and (self.year1.text != 'Year'):
             self.data[self.day][self.hour][2] = self.day1.text + '/' + self.month1.text + '/' + self.year1.text

        if (self.day2.text != 'Day') and (self.month2.text != 'Month') and (self.year2.text != 'Year'):
             self.data[self.day][self.hour][3] = self.assignment2in.text

        if self.assignment2in.text and (self.day2.text != 'Day') and (self.month2.text != 'Month') and (self.year2.text != 'Year'):
             self.data[self.day][self.hour][4] = self.duedate2in.text

        self.label.text = self.data[self.day][self.hour][0] + '\n' + self.data[self.day][self.hour][1] + ' ' + self.data[self.day][self.hour][2] + '\n' + self.data[self.day][self.hour][3] + ' ' + self.data[self.day][self.hour][4]
        data = open('data','w')
        dump(self.data,data)
        data.close()
        self.popup.dismiss()

    def dismissok2(self,instance):

        self.data[self.days][self.indexs][5] = self.editin.text
        self.popup.dismiss()

    def editnotes(self,day,index):

        self.days = day
        self.indexs = index
        self.editback = BoxLayout(orientation='vertical')
        self.editin = TextInput(text_hint='Notes',
                                text=self.data[self.days][self.indexs][5],
                                multiline=True)
        self.okbutton = Button(text='Ok',size_hint=(.5,.5),
                               pos_hint={'center_x':.5,})
        self.cancelbutton = Button(text='Cancel',size_hint=(.5,.5),
                                   pos_hint={'center_x':.5,})
        self.editback.add_widget(self.editin)
        self.editback.add_widget(self.okbutton)
        self.editback.add_widget(self.cancelbutton)
        self.popup = Popup(content=self.editback,auto_dismiss=False,
                           size_hint=(.75,.75),title='Edit Notes')
        self.okbutton.bind(on_press=self.dismissok2)
        self.cancelbutton.bind(on_press=self.popup.dismiss)
        self.popup.open()



class MainApp(App):

    def build(self):
        return RootWidget()

if __name__== '__main__' or '__android__':

    MainApp().run()
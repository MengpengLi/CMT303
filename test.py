from Tkinter import *
from cmtOptions import *
from cmtQuestions import *
from addQuestions import *

import csv
import os
import re
import tkMessageBox

QuestionsRange = ["001.csv","002.csv","003.csv","004.csv","005.csv","006.csv","007.csv","008.csv","009.csv","011.csv","012.csv","013.csv","014.csv","015.csv"]
#,"010.csv"

class test(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        #self.test()
        self.Qlist = []
        self.list = []
        self.label = Label(self,text = "")
        self.text = Label(self, text = "",font = ('MS',22),wraplength = 600)
        self.varCB = IntVar()
        self.cb = []
        self.count = 0
        self.opt = []
        self.answer = [3,3,3,3,3,3,3,3,3,3]
        for i in range(0,4):
            self.cb.append(Radiobutton(self,font = ('MS',15), variable=self.varCB))

    def unwrap(self,ques,opt):
        self.opt = opt
        pattern = re.compile(r"\(\d{3}\.gif")
        if (pattern.match(ques)):
            self.text.configure(text = ques[9:])
            print ques[1:8]
            photo = PhotoImage(file = r"/Users/Angrybirdy/PycharmProjects/cmt303/questions/" + ques[1:8])
            self.label.configure(image = photo)
            self.label.image = photo
            self.label.pack()
            self.label.grid(row =1, column =3)
        else:
            self.label.configure(image = "")
            self.text.configure(text = ques)
            self.text.configure(image = "")
        self.text.grid(row = 5, column = 3,padx =150,pady = 100,sticky = E)
        for i in range(len(opt)):
            self.cb[i].configure(text = opt[i].getOption(),value = i)
            self.cb[i].grid(row = 6+i, column = 3,padx = 00,pady = 10)

    def streamer(self):
        for directory, subdirectories, files in os.walk("./questions"):
            for file in files:
                if file in QuestionsRange:
                    self.Qlist.append(reader("./questions/" + file))
                    print file

    def ranQuestions(self):
        temp = self.Qlist
        for i in range(0,10):
            tmp = random.randint(0,len(temp)-1)
            self.list.append(temp[tmp])
            print(temp[tmp].id)
            del temp[tmp]

    def display(self):
        self.ranQuestions()
        a,b = self.list[0].wrapper()
        self.unwrap(a,b)

    def prev(self):
        prev = Button(self,text = "prev",font = ("MS",15))
        prev['command'] = self.clickPrev
        prev.grid(row =15,column =2,padx = 50,pady = 15)

    def clickPrev(self):
        if(self.count > 0 ):
            self.save()
            self.count = self.count - 1
            a,b = self.list[self.count].wrapper()
            self.unwrap(a,b)
        else:
            self.save()
            tkMessageBox.showinfo("Alert","It's the first question")


    def Next(self):
        next = Button(self,text = "next", font = ("MS",15))
        next['command'] = self.clickNext
        next.grid(row = 15, column = 6,padx = 50,pady = 15)

    def clickNext(self):
        if(self.count < len(self.list)-1):
            self.save()
            self.count += 1
            a,b = self.list[self.count].wrapper()
            self.unwrap(a,b)
            print(self.answer)
        else:
            self.save()
            tkMessageBox.showinfo("Alert","It's the last question")

    def save(self):
        print self.varCB.get()
        self.answer[self.count] = self.opt[self.varCB.get()].checkCorrectness()

    def manageList(self):
        a =1

    def submitButton(self):
        submitB = Button(self,text = "submit",font = ("MS",15))
        submitB ['command'] = self.submit
        submitB.grid(row = 15,column = 3)

    def submit(self):
        if(3 in self.answer):
            tkMessageBox.showinfo("Alert","Please finish all questions")
        else:
            result = 0
            for i in self.answer:
                if i == True:
                    result += 1
            result *= 10
            for directory, subdirectories, files in os.walk("./students"):
                    ID = len(files)
                    name ="./students/" + "c" + str(ID) + ".csv"
                    with open(name, 'a+') as csvfile:
                        writer = csv.writer(csvfile,delimiter='|')
                        writer.writerow([str(result) + "%"])
                        self.master.destroy()

    def manageTest(self):
        self.questions = Listbox(self,font = ('MS',22))
        scroll = Scrollbar(self, command = self.questions.yview())
        self.questions.configure(yscrollcommand=scroll.set)
        self.questions.grid(row=0, column=2, columnspan=2, sticky=NE)
        scroll.grid(row=0, column=4, sticky=W)
        for i in QuestionsRange:
            self.questions.insert(END, i)
        self.addButton = Button(self,text = "add",font = ("MS",15))
        self.addButton ['command'] = self.appendQuestions
        self.addButton.grid(row =5,column = 0)
        self.deleteButton = Button(self,text = "delete",font = ("MS",15))
        self.deleteButton ['command'] = self.deleteQuestions
        self.deleteButton.grid(row = 5,column = 5)

    def appendQuestions(self):
        master2 = Toplevel(self.master)
        question = addQuestions(master2)
        question.content()
       # print question

    def deleteQuestions(self):
        print 2




def reader(file):
    with open(file,"rb") as csvfile:
        buffer = csv.reader(csvfile,delimiter='|')
        for row in buffer:
                temp = cmtQuestions(row[-1],row[1])
                for i in range(2,2 + int(row[0])):
                    if(i == 2):
                        tmp = cmtOptions(row[i],True)
                        temp.addOptions(tmp)
                    else:
                        tmp = cmtOptions(row[i],False)
                        temp.addOptions(tmp)
    return temp







from Tkinter import *
from cmtOptions import *
from cmtQuestions import *
from addQuestions import *

import tkMessageBox
import tkFont
import csv
import os
import re
import tkMessageBox

QuestionsRange = ["001.csv","002.csv","003.csv","004.csv","005.csv","006.csv","007.csv","008.csv","009.csv","011.csv","012.csv","013.csv","014.csv","015.csv"]
#,"010.csv"

TitleFont = ("Ariel 30 bold")

NormalFont = ("Ariel 13")

BackCol = ("#4D505B")

TextCol = ("#FFFFFF")



class test(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x = (self.ws/2) - 600
        self.y = (self.hs/2) - 300
        self.master.geometry('%dx%d+%d+%d' % (600, 300, self.x, self.y))
        self.master.geometry('{}x{}'.format(1200, 600))
        self.master.configure(background='#4D505B')
        self.master.resizable(width=TRUE, height=TRUE)
        
        #self.grid()
        self.pack(fill=BOTH, expand=1)
        self.configure(background='#4D505B')
        #self.test()
        self.Qlist = []
        self.list = []
        self.QuestionTitleString = StringVar()
        self.label = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol)
        self.text = Label(self, text = "",font = NormalFont,wraplength = 600,bg='#4D505B', fg=TextCol, justify="left")
        self.varCB = IntVar()
        self.cb = []
        self.count = 0
        self.opt = []
        self.answer = [3,3,3,3,3,3,3,3,3,3]
        for i in range(0,4):
            self.cb.append(Radiobutton(self,font = NormalFont, variable=self.varCB,bg='#4D505B',fg=TextCol ))


    #un-wrap the wrapped cmtQuestion object and display on the root
    def unwrap(self,ques,opt):
        self.opt = opt
        pattern = re.compile(r"\(\d{3}\.gif")
        if (pattern.match(ques)):
            self.text.configure(text =  ques[9:],background='#4D505B')
            print ques[1:8]
            photo = PhotoImage(file = r"./questions/" + ques[1:8])
            self.label.configure(image = photo,background='#4D505B')
            self.label.image = photo
            self.label.pack()
            self.label.place(x=570, y=200)
            #self.label.grid(row =1, column =3)
            for i in range(len(opt)):
                self.cb[i].configure(text = opt[i].getOption(),value = i,background='#4D505B')
                #self.cb[i].grid(row = 6+i, column = 3,padx = 00,pady = 10)
                self.cb[i].pack()
                self.cb[i].place(x=320, y=250+(40*i))
        else:
            self.label.configure(image = "",background='#4D505B')
            self.text.configure(text = ques,background='#4D505B')
            self.text.configure(image = "",background='#4D505B')
            for i in range(len(opt)):
                self.cb[i].configure(text = opt[i].getOption(),value = i,background='#4D505B',highlightbackground=BackCol, selectcolor="#22242a")
                #self.cb[i].grid(row = 6+i, column = 3,padx = 00,pady = 10)
                self.cb[i].pack()
                self.cb[i].place(x=560, y=250+(40*i))
                
        self.text.pack()
        self.text.place(x=320,y=80)
        #self.text.grid(row = 5, column = 3,padx =150,pady = 100,sticky = E)

            

    #read all avaliable files in the questions folder
    def streamer(self):
        for directory, subdirectories, files in os.walk("./questions"):
            for file in files:
                if file in QuestionsRange:
                    self.Qlist.append(reader("./questions/" + file))


    #random pull 10 questions out of the questions bank
    def ranQuestions(self):
        temp = self.Qlist
        for i in range(0,10):
            tmp = random.randint(0,len(temp)-1)
            self.list.append(temp[tmp])
            print(temp[tmp].id)
            del temp[tmp]

    #pass the questions list 
    def display(self):
        self.ranQuestions()
        a,b = self.list[0].wrapper()
        self.unwrap(a,b)

    #construct the previoud button
    def prev(self):
        prev = Button(self,text = "prev",bg="#80628B", fg = TextCol, font = NormalFont, padx=13)
        prev['command'] = self.clickPrev
        #prev.grid(row =15,column =2,padx = 50,pady = 15)
        prev.pack()
        prev.place(x = 130,y=500)

    #previous butoon control tool
    def clickPrev(self):
        if(self.count > 0 ):
            self.save()
            self.count -= 1
            a = self.list[self.count].question
            b = self.list[self.count].finaloptions
            self.unwrap(a,b)
        else:
            self.save()
            tkMessageBox.showinfo("Alert","It's the first question")


    #construct Next button
    def Next(self):
        next = Button(self,text = "Next", bg="#80628B", fg = TextCol, font = NormalFont, padx=13)
        next['command'] = self.clickNext
        #next.grid(row = 15, column = 6,padx = 50,pady = 15)
        next.place(x=1000, y=500)
        

    #next button control tool
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

    #save the current selected option
    def save(self):
        print self.varCB.get()
        self.answer[self.count] = self.opt[self.varCB.get()].checkCorrectness()


    #submit button construct
    def submitButton(self):
        submitB = Button(self,text = "submit",bg="#16A79D", fg = TextCol, font = NormalFont, padx=13)
        submitB ['command'] = self.submit
        #submitB.grid(row = 15,column = 3)
        submitB.pack()
        submitB.place(x=550, y=500)
        
    #submit button constructor, and store the scores in alongside with the Students info
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

    #the method to be called after admin logged in with the ability manage questions bank
    def manageTest(self):
        self.questions = Listbox(self,font = ('MS',22), fg = TextCol)
        scroll = Scrollbar(self, command = self.questions.yview())
        self.questions.configure(yscrollcommand=scroll.set,background='#4D505B')
        self.questions.pack()
        self.questions.place(x = 420, y=100)
        
        for i in QuestionsRange:
            self.questions.insert(END, i)
        self.addButton = Button(self,text = "Add",font = ("MS",15), fg=TextCol, bg ="#16A79D")
        self.addButton ['command'] = self.appendQuestions
        #self.addButton.grid(row =5,column = 0)
        self.addButton.pack()
        self.addButton.place(x=550, y=470)
        self.deleteButton = Button(self,text = "Delete", font = ("MS",15),fg=TextCol, bg ="#80628B")
        self.deleteButton ['command'] = self.deleteQuestions
        self.deleteButton.pack()
        self.deleteButton.place(x=540, y=520)
        #self.deleteButton.grid(row = 5,column = 5)
        self.QuitButton = Button(self,text ="QUIT", command=lambda: Quitting2(self,"Are you sure you want to Quit?" ), bg="#CF4858", fg = TextCol)
        self.QuitButton.place(x=1100,y=30)

        def Quitting2(self, Text):
            myExit = tkMessageBox.askyesno('Quit',Text)
            if myExit:
                self.master.destroy()

    #add more valid id for questions bank content
    def appendQuestions(self):
        master2 = Tk()
        question = addQuestions(master2)
        question.content()
        text =question.text
        print text
        global QuestionsRange
        pattern = re.compile(r"\d{3}\.csv")
        if(text not in QuestionsRange) and pattern.match(text):
            QuestionsRange.append(text)
            self.manageTest()
        else:
             tkMessageBox.showinfo("Alert","input doesn't compile",parent  = self.master)
      

    #delete one of the questions from the bank
    def deleteQuestions(self):
        selected = self.questions.curselection()[0]
        global QuestionsRange
        del QuestionsRange[selected]
        self.manageTest()




#csv reader
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







from Tkinter import *

class addQuestions(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()

    def content(self):
        self.txtComment = Text(self, height=3,width=40)
        scroll = Scrollbar(self, command=self.txtComment.yview)
        self.txtComment.configure(yscrollcommand=scroll.set)
        self.txtComment.grid(row=0, column=0,columnspan=5, sticky=E)
        scroll.grid(row=0, column=5, sticky=W)
        self.confirm = Button(self,text = "confirm",font = ('MS',15))
        self.confirm ['command'] = self.addQuestion
        self.confirm.grid(row = 3,column = 5)

    def addQuestion(self):
        text = self.txtComment.get("1.0",END)
        self.master.destroy()
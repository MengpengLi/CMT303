from Tkinter import *

TitleFont = ("Ariel 20 bold")

NormalFont = ("Ariel 13")

BackCol = ("#4D505B")

TextCol = ("#FFFFFF")

class addQuestions(Frame):

    #initial the add question pop-up window
    def __init__(self,master):
        Frame.__init__(self,master)
        
        self.ws = 600
        self.hs = 300
        self.x = 1200
        self.y = 600
        self.master.geometry('{}x{}'.format(500, 100))
        self.master.configure(background='#4D505B')
        self.master.resizable(width=TRUE, height=TRUE)
        self.grid()
        self.text = ''
        self.configure(background='#4D505B')

    def content(self):
        self.txtComment = Text(self, height=3,width=40)
        self.txtComment.grid(row=0, column=0,columnspan=5, sticky=E)
        self.confirm = Button(self,text = "confirm",font = ('MS',15))
        self.confirm ['command'] = self.addQuestion
        self.confirm.grid(row = 3,column = 10)
        self.master.mainloop()

    def addQuestion(self):
        self.text = self.txtComment.get("1.0",'end-1c')
        self.master.quit()
        self.master.destroy()

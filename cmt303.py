from Tkinter import *
from cmtOptions import *
from cmtQuestions import *

class questionnaire(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createProgSelect()
        self.createTeamExp()
        self.TextBox()
        self.testQ()

    def createProgSelect(self):
        lblprog = Label(self, text = "degree programme", font=("MS",13,"bold"))
        lblprog.grid(row = 0, column = 0, columnspan = 2, sticky=NE)

        self.listProg = Listbox(self,height = 3, font=("",13,""))
        scroll = Scrollbar(self,command = self.listProg.yview)
        self.listProg.configure(yscrollcommand = scroll.set)

        self.listProg.grid(row =0, column = 2, columnspan = 2, sticky = NE)
        scroll.grid(row = 0, column = 4, sticky = W)
        for item in ["CS", "CS with", "BIS", "SE", "Joints",""]:
            self.listProg.insert(END,item)
        self.listProg.selection_set(END)
    def createTeamExp(self):
        i = 0
        agreeButton = []
        for item in ["strongly \n agree","partly \n agree","partly \n disagree","strongly \n disagree"]:
            agreeButton.append(Label(self, text = item, font = ("MS",13,"bold")))
            agreeButton[i].grid(row= 3, column = 4 + i, rowspan =2, sticky = NE)
            i += 1
        TeamExp = Label(self, text = """
        Team Experience:
        1.our team worked together effectively

        2.our team produced good qualityproducts

        3.I enjoy working in our Team
        """,font=("MS",13,"bold"),justify = "left")
        TeamExp.grid(row= 4,column = 0,rowspan = 6, columnspan = 4)
        self.varQ = [IntVar(),IntVar(),IntVar()]
        rq = {}
        for i in range(3):
            rq[i]= {}
            for j in range(4):
               # print(type(RADIOBUTTON))
                rq[i][j] = Radiobutton(self,variable = self.varQ[i],value = 4-j)
                rq[i][j].grid(row=5+i, column = 4+j)
        butt = Button(self,text = "something")
        butt['command'] = self.printsomeything
        butt.grid(row = 10,column = 10)
    def printsomeything(self):
        for var in self.varQ:
             print(var.get())
    def TextBox(self):
        self.txtcomment = Text(self,height = 3,width = 40)
        scroll = Scrollbar(self,command = self.txtcomment.yview,borderwidth = 1)
        self.txtcomment.configure(yscrollcommand = scroll.set)
        self.txtcomment.grid(row =12, column = 2,columnspan = 5, sticky =E)
        scroll.grid(row = 12,column = 7, sticky =W)
        self.enterName = Entry(self)
        self.enterName.grid(row = 15,column =4, columnspan =2, sticky =E)

    def testQ(self):
        Q1 = cmtQuestions("Q1")
        o1 = cmtOptions.cmtOptions("a1",True)
        Q1.addOptions(o1)
        o2 = cmtOptions.cmtOptions("b1",False)
        Q1.addOptions(o2)
        a,b = Q1.wrapper(10,10)


root = Tk()
root.title("team work")
app = questionnaire(root)
root.mainloop()

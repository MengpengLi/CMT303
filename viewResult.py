from Tkinter import *
import os
import csv
import tkMessageBox

TitleFont = ("Ariel 20 bold")

NormalFont = ("Ariel 13")

BackCol = ("#4D505B")

TextCol = ("#FFFFFF")

def Quitting(CurrentWindow, title, message):
    if tkMessageBox.askyesno(title, message,parent = CurrentWindow):
        CurrentWindow.destroy()


class viewResult(Frame):
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

        self.pack(fill=BOTH, expand=1)
        self.configure(background='#4D505B')
        self.info = []
        self.count = 0
        for directory, subdirectories, files in os.walk("./students"):
            self.length = len(files)
        
        self.StudentName = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol)
        self.StudentName.pack()
        self.StudentName.place(x=250, y=100)
        
        self.StudentEmail = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol)
        self.StudentEmail.pack()
        self.StudentEmail.place(x=250, y=130)
    
        self.StudentTel = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol)
        self.StudentTel.pack()
        self.StudentTel.place(x=250, y=160)
       
        self.showScore = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol )
        self.showScore.pack()
        self.showScore.place(x=250, y=190)
        
        self.recCourse = Label(self,text = "", font = TitleFont,bg='#4D505B', fg=TextCol)
        self.recCourse.pack()
        self.recCourse.place(x=250, y=220)
    
        self.QuitButton = Button(self.master,text ="Exit", command=lambda: Quitting(self.master, "Quit","Are you sure you want to Return to the Home Page?" ), bg="#16A79D", fg = TextCol, font="Ariel 20 bold")
        self.QuitButton.place(x= 550, y=450)

    #student entry for file reading, the program only read file that related to this student
    def StudentReadFile(self):
        for directory, subdirectories, files in os.walk("./students"):
            ID = len(files)
            name ="./students/" + "c" + str(ID) + ".csv"
            with open(name, 'rb') as csvfile:
                reader = csv.reader(csvfile,delimiter='|')
                for row in reader:
                    if reader.line_num == 1:
                        self.info = row
                        print self.info
                    elif reader.line_num == 2:
                        self.score = row
                        print self.score
                    elif reader.line_num == 3:
                        self.recommandCourse = row
                        print self.recommandCourse

    #admin entry for file reading, that the program read all students' detail in the students folder
    def adminEntry(self):
        for directory, subdirectories, files in os.walk("./students"):
            name = "./students/" + str(files[self.count])
            with open(name, 'rb') as csvfile:
                reader = csv.reader(csvfile,delimiter='|')
                for row in reader:
                    if reader.line_num == 1:
                        self.info = row
                    elif reader.line_num == 2:
                        self.score = row
                    elif reader.line_num == 3:
                        self.recommandCourse = row

    #display for admin user that allow user browsing through all students
    def staffDisplay(self):
        self.StudentName.configure(text ="""Name: """ + str(self.info[0]) + " " + str(self.info[1]) )
        self.StudentEmail.configure(text = """Email:  """ + str(self.info[2]))
        self.StudentTel.configure(text = """Tel: """ + str(self.info[3]))
        self.showScore.configure(text = """Logic Test Score:  """ + str(self.score)[2:-2])
        self.recCourse.configure(text = "Recommanded Course:  "+ str(self.recommandCourse)[4:-4])
        self.Next = Button(self,text = "Next", bg="#80628B", fg = TextCol, font = "Ariel 20 bold")
      
        self.Next ['command'] = self.clickNext
 
        self.Next.place(x=545, y=400)
        
    #next button controler
    def clickNext(self):
        if self.count < self.length - 1:
            self.count += 1
            self.adminEntry()
            self.staffDisplay()
        else:
            tkMessageBox.showinfo("Alert","It's the last student")
    
    #display the student own info
    def StudentDisplay(self):

        self.StudentName.configure(text = """Name: """ + str(self.info[0]) + " " + str(self.info[1]))
        self.StudentEmail.configure(text = """Email:  """ + str(self.info[2]))
        self.StudentTel.configure(text =  """Tel: """ + str(self.info[3]))
        self.showScore.configure(text = """Logic Test Score:  """ + str(self.score)[2:-2])
        self.recCourse.configure(text ="Recommanded Course:  "+ str(self.recommandCourse)[4:-4] )

       
    #exit
    def exitProgram(self):
        self.master.destroy()


from Tkinter import *
import os
import csv
import tkMessageBox

class viewResult(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.info = []
        self.count = 0
        for directory, subdirectories, files in os.walk("./students"):
            self.length = len(files)
        self.StudentName = Label(self,text = "", font = ("MS",20))
        self.StudentName.grid(row = 1, column =1)
        self.StudentEmail = Label(self,text = "", font = ("MS",20))
        self.StudentEmail.grid(row = 2, column = 1)
        self.StudentTel = Label(self,text = "", font = ("MS",20))
        self.StudentTel.grid(row = 3, column = 1)
        self.showScore = Label(self,text = "", font = ("MS",20) )
        self.showScore.grid(row = 4, column = 1)
        self.recCourse = Label(self,text = "", font = ("MS",20))
        self.recCourse.grid(row = 5, column = 1)

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

    def staffDisplay(self):
        self.StudentName.configure(text ="""Name: """ + str(self.info[0]) + " " + str(self.info[1]) )
        self.StudentEmail.configure(text = """Email:  """ + str(self.info[2]))
        self.StudentTel.configure(text = """Tel: """ + str(self.info[3]))
        self.showScore.configure(text = """Logic Test Score:  """ + str(self.score))
        self.recCourse.configure(text = "Recommanded Course:  "+ str(self.recommandCourse))
        self.Next = Button(self,text = "next", font = ("MS",15))
        self.Next.grid(row = 6, column = 1)
        self.Next ['command'] = self.clickNext
        self.exit = Button(self,text = "Exit")
        self.exit.grid(row = 7, column = 1)
        self.exit ["command"] = self.exitProgram

    def clickNext(self):
        if self.count < self.length - 1:
            self.count += 1
            self.adminEntry()
            self.staffDisplay()
        else:
            tkMessageBox.showinfo("Alert","It's the last student")


    def StudentDisplay(self):

        self.StudentName.configure(text = """Name: """ + str(self.info[0]) + " " + str(self.info[1]))
        self.StudentEmail.configure(text = """Email:  """ + str(self.info[2]))
        self.StudentTel.configure(text =  """Tel: """ + str(self.info[3]))
        self.showScore.configure(text = """Logic Test Score:  """ + str(self.score))
        self.recCourse.configure(text ="Recommanded Course:  "+ str(self.recommandCourse) )

        self.exit = Button(self,text = "Exit")
        self.exit.grid(row = 6, column = 1)
        self.exit ["command"] = self.exitProgram

    def exitProgram(self):
        self.master.destroy()


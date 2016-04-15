import sys
from Tkinter import *
import tkMessageBox
import tkFont

#---COMMON FUNCTIONS AND VARIABLES---

TitleFont = ("Ariel 30 bold")

NormalFont = ("Ariel 13")

BackCol = ("#4D505B")

TextCol = ("#FFFFFF")

#---Student Details Variables---

StudentFirstName = None
StudentSurname = None
StudentEmail = None
StudentTel = None

#Exit Warning Box

def Quitting(CurrentWindow, title, message):
    myExit = tkMessageBox.askyesno(title, message)
    if myExit > 0:
        CurrentWindow.destroy()
        return
# Alert Box

def Alert(CurrentWindow, title, message):
    tkMessageBox.showwarning(title, message)
    return


#----WELCOME PAGE -----

class WelcomePage:
    def __init__(self, master):

        #General Layout Information
        frame = Frame(master)
        frame.pack()
        self.master=master
        self.master.geometry('{}x{}'.format(1200, 600))
        self.master.resizable(width=TRUE, height=TRUE)
        self.master.configure(background='#4D505B')
        self.master.title("Welcome")

        #Adding Cardiff Uni Logo using canvas
        self.canvas = Canvas(width = 300, height = 300, bg = BackCol)
        self.canvas.pack()
        self.Logo = PhotoImage(file = "")#r'/Users/Angrybirdy/PycharmProjects/cmt303/CardiffRecolour.png')
        self.resizeLogo = self.Logo.subsample(5,5)
        self.canvas.create_image(100, 100, image = self.resizeLogo, anchor = CENTER)
        self.canvas.place(x=260, y=230, anchor=CENTER)
        self.canvas.config(highlightbackground=BackCol)

        #Adding Title and Description
        self.HelloLabel = Label(self.master,text="Welcome!",bg=BackCol,fg=TextCol, font=TitleFont)
        self.HelloLabel.place(x=400,y=75)
        self.DescriptionLabel = Label(self.master,text="This excercise is designed to test your logic and reasoning skills\
 to see \nwhether one of the courses available within the Cardiff School \nof Computer Science and Informatics are for you!",bg=BackCol,fg=TextCol,font=NormalFont, justify="left")
        self.DescriptionLabel.place(x=400,y=130)

        #Student Details Entry
        self.DetailsLabel = Label(self.master,text="Please enter your details below and click enter to begin the app. Alternatively, \nif you wish to remain anonymous, you can leave these fields blank.",bg=BackCol,fg=TextCol,font=NormalFont, justify="left")
        self.DetailsLabel.place(x=400,y=200)

        self.UserFirstName = StringVar()
        self.UserSurname = StringVar()
        self.UserEmail = StringVar()
        self.UserTel = StringVar()

        #First Name
        self.UserFirstNameLabel = Label(self.master, text = "First Name(s): ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.UserFirstNameLabel.place(x = 400, y = 300)
        self.UserFirstNameEntry = Entry(self.master,textvariable=self.UserFirstName, bg = "#757a8a", fg = TextCol, width = 35)
        self.UserFirstNameEntry.place(x = 580, y = 300)
        #Surname
        self.UserSurnameLabel = Label(self.master, text = "Surname: ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.UserSurnameLabel.place(x = 400, y = 330)
        self.UserSurnameEntry = Entry(self.master,textvariable=self.UserSurname, bg = "#757a8a", fg = TextCol, width = 35)
        self.UserSurnameEntry.place(x = 580, y = 330)
        #Email Address
        self.UserEmailLabel = Label(self.master, text = "Email Address: ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.UserEmailLabel.place(x = 400, y = 360)
        self.UserEmailEntry = Entry(self.master,textvariable=self.UserEmail, bg = "#757a8a", fg = TextCol, width = 35)
        self.UserEmailEntry.place(x = 580, y = 360)
        #Telephone Number
        self.UserTelLabel = Label(self.master, text = "Telephone Number: ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.UserTelLabel.place(x = 400, y = 390)
        self.UserTelEntry = Entry(self.master,textvariable=self.UserTel, bg = "#757a8a", fg = TextCol, width = 35)
        self.UserTelEntry.place(x = 580, y = 390)

        #Quit Button
        self.QuitButton = Button(self.master,text ="QUIT", command=lambda: Quitting(self.master, "Quit","Are you sure you want to Quit?" ), bg="#CF4858", fg = TextCol)
        self.QuitButton.place(x=1100,y=30)

        #Enter Button
        self.StartButton = Button(self.master,text = "ENTER", command = lambda: NextPage(self), bg="#16A79D", fg = TextCol, font = "Ariel 20 bold")
        self.StartButton.place(x= 550, y=450)


        #--Admin Section--


        #Admin Section Heading
        self.AdminTitle = Label(self.master, text = "ADMIN",bg=BackCol,fg="#d6d7dc", font="Ariel 15")
        self.AdminTitle.place(x = 120, y = 445)

        #Storing Username and Password Locally
        self.Username = StringVar()
        self.Password = StringVar()

        #Admin Username Entry
        self.AdminUser = Label(self.master, text = "Username: ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.AdminUser.place(x = 30, y = 478)
        self.SubmittedUsername = Entry(self.master,textvariable=self.Username, bg = "#464953", fg = TextCol)
        self.SubmittedUsername.place(x = 130, y = 480)

        #Admin Password Entry
        self.AdminPass = Label(self.master, text = "Password: ",bg=BackCol,fg=TextCol, font=NormalFont)
        self.AdminPass.place(x = 30, y = 508)
        self.SubmittedPassword = Entry(self.master,textvariable=self.Password, bg = "#464953", fg = TextCol, show="*")
        self.SubmittedPassword.place(x = 130, y = 510)

        #Button to Progress to Admin Console
        self.AdminButton = Button(self.master,text ="Go", command = lambda: ToAdmin(self),bg="#464953", fg = TextCol)
        self.AdminButton.place(x=130,y=540)

        #Local Function to go to Admin Console
        def ToAdmin(self):
            if self.SubmittedUsername.get() == "admin" and self.SubmittedPassword.get() == "password":
                root3 = Toplevel(self.master)
                root3.geometry('%dx%d+%d+%d' % (600, 300, x, y))
                goto = AdminConsole(root3)
            else: Alert(self, "Invalid Details", "Username or Password Incorrect")

        #Local Function to Progress to Home Page
        def NextPage(self):
            root2 = Toplevel(self.master)
            StudentFirstName = self.UserFirstNameEntry.get()
            StudentSurname = self.UserSurnameEntry.get()
            StudentEmail = self.UserEmailEntry.get()
            StudentTel = self.UserTelEntry.get()
            print(StudentFirstName)
            print(StudentSurname)
            print(StudentEmail)
            print(StudentTel)
            root2.geometry('%dx%d+%d+%d' % (600, 300, x, y))
            goto = MainNav(root2)


#----MAIN NAVIGATION PAGE----


class MainNav:
    def __init__(self, master2):
        #Layout Info
        frame = Frame(master2)
        frame.pack()
        self.master2=master2
        self.master2.geometry('{}x{}'.format(1200, 600))
        self.master2.resizable(width=FALSE, height=FALSE)
        self.master2.configure(background='#4D505B')
        self.master2.title("Home Page")

        #Home Page Title and Description
        self.TopLabel = Label(self.master2,text="Home",bg=BackCol,fg=TextCol, font=TitleFont)
        self.TopLabel.place(x=300,y=75)
        self.DescriptionLabel = Label(self.master2,text="Please select what you would like to do",bg=BackCol,fg=TextCol,font=NormalFont, justify="left")
        self.DescriptionLabel.place(x=300,y=130)

        #Logic Test Button and Labels
        self.TestButton = Button(self.master2,text = "L",  bg="#16A79D", fg = TextCol, font = "Ariel 40 bold", padx=13)
        self.TestButton.place(x= 300, y=200)
        self.TestTitle = Label(self.master2, text = "Take Logic Test",bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.TestTitle.place(x= 400, y = 200)
        self.TestDescript = Label(self.master2, text = "Select this to begin the Logic and Reasoning test. There will be a few \npractice questions to get you used to the format and question types. ",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.TestDescript.place(x= 400, y = 230)

        #Questionnaire Button and Labels
        self.QuestionButton = Button(self.master2,text = "C",  bg="#16A79D", fg = TextCol, font = "Ariel 40 bold")
        self.QuestionButton.place(x= 300, y=300)
        self.QuestionTitle = Label(self.master2, text = "Take Course Selection Questionnaire",bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.QuestionTitle.place(x= 400, y=300)
        self.QuestionDescript = Label(self.master2, text = "Select this to begin the Course Selection Questionnaire. \nThis ask you a series of questions to help identify which course is right for you.",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.QuestionDescript.place(x= 400, y= 330)

        #Results Button and Labels
        self.ResultsButton = Button(self.master2,text = "R",  bg="#16A79D", fg = TextCol, font = "Ariel 40 bold")
        self.ResultsButton.place(x= 300, y=400)
        self.ResultsTitle = Label(self.master2, text = "View Your Results", bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.ResultsTitle.place(x= 400, y=400)
        self.ResultsDescript = Label(self.master2, text = "Select this to view the results for your progress so far",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.ResultsDescript.place(x= 400, y=430)

        #Quit Button
        self.QuitButton = Button(self.master2,text ="QUIT", command=lambda: Quitting(self.master2, "Quit Session", "Are you sure you want to Quit this Session?"), bg="#CF4858", fg = TextCol)
        self.QuitButton.place(x=1100,y=30)

#----ADMIN CONSOLE----

class AdminConsole:
    def __init__(self, master3):
        #Layout Info
        frame = Frame(master3)
        frame.pack()
        self.master3=master3
        self.master3.geometry('{}x{}'.format(1200, 600))
        self.master3.resizable(width=FALSE, height=FALSE)
        self.master3.configure(background='#4D505B')
        self.master3.title("NEW")

        #Admin Console Title and Description
        self.TopLabel = Label(self.master3,text="Admin Console",bg=BackCol,fg=TextCol, font=TitleFont)
        self.TopLabel.place(x=300,y=75)
        self.DescriptionLabel = Label(self.master3,text="Please select what you would like to do",bg=BackCol,fg=TextCol,font=NormalFont, justify="left")
        self.DescriptionLabel.place(x=300,y=130)

        #Logic Test Button and Labels
        self.TestButton = Button(self.master3,text = "L",  bg="#16A79D", fg = TextCol, font = "Ariel 40 bold", padx=13)
        self.TestButton.place(x= 300, y=200)
        self.TestTitle = Label(self.master3, text = "Amend Logic Test",bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.TestTitle.place(x= 400, y = 200)
        self.TestDescript = Label(self.master3, text = "Select this if you wish to change any aspects of the Logic Test.",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.TestDescript.place(x= 400, y = 230)

        #Questionnaire Button and Labels
        self.QuestionButton = Button(self.master3,text = "C", bg="#16A79D", fg = TextCol, font = "Ariel 40 bold")
        self.QuestionButton.place(x= 300, y=300)
        self.QuestionTitle = Label(self.master3, text = "Amend Questionnaire",bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.QuestionTitle.place(x= 400, y=300)
        self.QuestionDescript = Label(self.master3, text = "Select this if you wish to adjust the questionnaire.",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.QuestionDescript.place(x= 400, y= 330)

        #Results Button and Labels
        self.ResultsButton = Button(self.master3,text = "R",  bg="#16A79D", fg = TextCol, font = "Ariel 40 bold")
        self.ResultsButton.place(x= 300, y=400)
        self.ResultsTitle = Label(self.master3, text = "View Student Results", bg=BackCol,fg=TextCol, font="Ariel 15 bold")
        self.ResultsTitle.place(x= 400, y=400)
        self.ResultsDescript = Label(self.master3, text = "Select this to view results for all students who have \ntaken the test so far.S",bg=BackCol,fg=TextCol, font=NormalFont, justify ="left")
        self.ResultsDescript.place(x= 400, y=430)



        #Quit Button
        self.QuitButton = Button(self.master3,text ="QUIT", command=lambda: Quitting(self.master3, "Quit Console", "Are you sure you want to Return to the Welcome Screen?"), bg="#CF4858", fg = TextCol)
        self.QuitButton.place(x=1100,y=30)


#Defining the Root
root = Tk()

#Getting Screen Layout to Center Root
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - 600
y = (hs/2) - 300
root.geometry('%dx%d+%d+%d' % (600, 300, x, y))


go = WelcomePage(root)





mainloop()

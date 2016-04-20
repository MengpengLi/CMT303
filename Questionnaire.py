from Tkinter import *
import tkMessageBox
import random
import csv
import os
import re



TitleFont = ("Ariel 30 bold")

NormalFont = ("Ariel 13")

BackCol = ("#4D505B")

TextCol = ("#FFFFFF")

courses_file = open("courses.csv", "r")
read_courses = courses_file.read()
courses_file.close()
split_courses = re.split("\r|\n|\r\n", read_courses)
course_list = []
for i in range(len(split_courses)):
	course = split_courses[i].split(',')
	course_list.append(course)
courses = {}
for item in course_list:
	courses[int(item[0])] = item[1]	

# Reading questionnaire.txt and formatting as list to be read by createNewQuestion methods
questionText = []
csv_file = open("questionnaire.txt", "r")
whole_csv = csv_file.read()
csv_file.close()
split_csv = re.split("\r|\n|\r\n", whole_csv)
print(split_csv)

# may need to inc '\n' too for other op.systems
question_rows = []
for i in range(len(split_csv)):
 	question_split = split_csv[i].split("|")
	question_rows.append(question_split)
print(question_rows)	
for i in range(len(question_rows)):
	questionText.append([])
	questionText[i].append(question_rows[i][0])
	if len(question_rows[i]) > 1:
		questionText[i].append(int(question_rows[i][1]))
		questionText[i].append(int(question_rows[i][2]))
		questionText[i].append([])
		for x in range(len(question_rows[i][3])):
			if question_rows[i][3][x].isdigit():
				questionText[i][3].append(int(question_rows[i][3][x]))
		questionText[i].append([])		
		for x in range(len(question_rows[i][4])):
			if question_rows[i][4][x].isdigit():
				questionText[i][4].append(int(question_rows[i][4][x]))

questionNo = 0

class Questionnaire(Frame):
# GUI Setup
    def __init__(self, master):
# Initialise Questionnaire Class

		Frame.__init__(self, master)
		self.ws = self.master.winfo_screenwidth()
                self.hs = self.master.winfo_screenheight()
                self.x = (self.ws/2) - 600
                self.y = (self.hs/2) - 300
                self.master.geometry('%dx%d+%d+%d' % (600, 300, self.x, self.y))
                self.master.geometry('{}x{}'.format(1200, 600))
                self.master.configure(background='#4D505B')
		#self.grid()
		#self.text1 = Label(self,height=3, padx=80, pady=80, wraplength=600, background=BackCol, font = NormalFont, fg = TextCol)    
		self.pack(fill=BOTH, expand=1)
                self.configure(background='#4D505B')
		self.createTeamExpQuest(0)

                global butYes
		butYes = Button(self, text='YES',bg="#16A79D", fg = TextCol, font = "Ariel 25 bold")
		butYes['command']=self.createNewQuestionA     #Note: no () after the method
		#butYes.grid(row=5, column=5, columnspan=2)	
                butYes.pack()
                butYes.place(x=900, y=220)
                
                        
                global butNo
		butNo = Button(self, text='NO',bg="#80628B", fg = TextCol, font = "Ariel 25 bold",padx=20)
		butNo['command']=self.createNewQuestionB      #Note: no () after the method
		#butNo.grid(row=5, column=6, columnspan=2)	
                butNo.pack()
                butNo.place(x=900, y=290)
                self.QuitButton = Button(self,text ="QUIT", command=lambda: Quitting2(self,"Are you sure you want to Quit?" ), bg="#CF4858", fg = TextCol)
                self.QuitButton.place(x=1100,y=30)
                def Quitting2(self, Text):
                    myExit = tkMessageBox.askyesno('Quit',Text)
                    if myExit:
                        self.master.destroy()
		
	


        #display the question on the screen
    def createTeamExpQuest (self, quesionNo):
		lblProg = Label(self, text=questionText[quesionNo][0], height=3, padx=95, pady=80, wraplength=600, background=BackCol, font = "Ariel 17", fg = TextCol, justify="left")    
                lblProg.pack()
                lblProg.place(x=100, y=150)

                
	#construct manage button
    def createManageButton(self):
		# if (loggedIn):	
		butManageQs = Button(self, text='Manage Questions',font=('MS', 15,'bold'), background='green', padx=20, pady=10, highlightthickness=0)
		butManageQs['command']=self.manageQuestionnaire      #Note: no () after the method
		butManageQs.grid(row=1, column=5, columnspan=3)


        #close current window and record the recommanded course alongside with the student info
    def displayCourseInfo(self, courses):
        print courses.values()
        self.master.destroy()
        for directory, subdirectories, files in os.walk("./students"):
            ID = len(files)
            name ="./students/" + "c" + str(ID) + ".csv"
            with open(name, 'a+') as csvfile:
                        writer = csv.writer(csvfile,delimiter='|')
                        writer.writerow([str(courses.values())])


        #display the recommanded course for the current student
    def createCourseLink(self, courses):
		for key in courses:
			butCourse = Button(self, text=courses[key],bg="#16A79D", fg = TextCol, font = "Ariel 20 bold")
			butCourse['command']=lambda :self.displayCourseInfo(courses)     #Note: no () after the method
			butCourse.pack()
			butCourse.place(x= 350, y=350)
			butYes.destroy()
			butNo.destroy()
			
                        			
        #cache the next question if 'yes' button is pressed

    def createNewQuestionA(self):
		eliminate = questionText[questionNo][3]
		for i in eliminate:
			if i in courses: del courses[i]	
		nextQ = questionText[questionNo][1]
		global questionNo
		questionNo = nextQ	
		self.createTeamExpQuest(questionNo)
		if (nextQ == 7):
			self.createCourseLink(courses)	

	#cache the next question if 'no' is pressed
    def createNewQuestionB(self):
		eliminate = questionText[questionNo][4]
		for i in eliminate:
			if i in courses: del courses[i]
		nextQ = questionText[questionNo][2]
		global questionNo
		questionNo = nextQ	
		self.createTeamExpQuest(questionNo)
		if (nextQ == 7):
			self.createCourseLink(courses)

        #display the edit guidence and current question list 
    def manageQuestionnaire(self):
                butYes.destroy()
		butNo.destroy()
		
		editGuide = Text(self, height=10, background=BackCol, font = "Ariel 12", fg = TextCol,padx = 10, pady=20)
		editGuide.place(x=190, y=100)
		#editGuide.grid(row=1, column=3, columnspan=10, rowspan=2, padx=100, pady=(10,0))
		editGuide.insert("1.0", "Edit the Questionnaire below. 	All but the last Question should contain the following 5 sections seperated by '|'. The final question should only include text introducing the selected course.\n1: The Question text \n2&3: A single digit for the next question (starting at 0) on answering Yes/No respectively.\n4&5: Digit(s) (seperated by commas) relating to which course(s) can be eliminated from the list below on ansering Yes/No respectively.\n\n")
		editGuide.insert("7.0", courses)
		editGuide.config(state=DISABLED) # guide not editable
		editScreen = Text(self, height=10, background="#6a6e7c", font = "Ariel 12", fg = TextCol, padx = 10, pady=20)
		#editScreen.grid(row=3, column=3, columnspan=8, rowspan=10, padx=100)
		editScreen.place(x=190, y=320)
		new_csv_file = open("questionnaire.txt", "r")
		w_whole_csv = new_csv_file.read()
		print(w_whole_csv)
		new_whole_csv = re.split("\n|\r|\r\n", w_whole_csv)
		print(new_whole_csv)
		print(len(new_whole_csv))
                x = 1
		for i in range(len(new_whole_csv)-1):
                        editScreen.insert((str(x)+".0"), ((new_whole_csv[i])+"\n"))
			global x
			x+=1
			print(x)
		editScreen.insert((str(x)+".0"), ((new_whole_csv[-1])))	
		butSaveQs = Button(self, text='Save',bg="#16A79D", fg = TextCol, font = "Ariel 25 bold", highlightthickness=0, padx=10, pady=5, command=lambda: self.saveQuestionnaire(editScreen.get("1.0",'end-1c')))     
	 	#butSaveQs.grid(row=12, column=8, columnspan=2)
		butSaveQs.pack()

	#check if the input new question list is in a valid format. if yes , save the new list. if no, warn the user
    def saveQuestionnaire(self, input):
		verifying = input.splitlines()
		print(verifying)
		okSave = True
		for i in range(len(verifying)-2):
                        sections = verifying[i].split('|')
                        print(sections)
                        print(len(sections))
			# code below verifies requirements outlined in editGuide Textbox are met
                        if len(sections) == 5 and len(sections[1]) == 1 and sections[1].isdigit() and len(sections[2]) == 1 and sections[2].isdigit() and (y.isdigit() for y in range(len(sections[3].split(',')))) and (z.isdigit() for z in range(len(sections[4].split(',')))):	
                                a = 1
                                print("PASSED: {}".format(verifying[i]))
                                print(len(verifying))
                        else:
                                print ("FAILED: {}".format(verifying[i]))
                                tkMessageBox.showerror("Update Error", "Your changes don't comply with the format required.\n\nPlease check your updates and try again.",parent = self.master)	
                                okSave = False
                                break
		if (okSave):		
			new_file = open("questionnaire.txt", "w+")
			new_file.write(input)
			new_file.close()	
			tkMessageBox.showerror("Saved Successfully", "Your changes have successfully been recorded")	
			self.manageQuestionnaire
			self.master.destroy()




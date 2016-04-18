from Tkinter import *
import tkMessageBox
import random
import csv
import os

courses_file = open("courses.csv", "r")
read_courses = courses_file.read()
courses_file.close()
split_courses = read_courses.split('\r')
course_list = []
for i in range(len(split_courses)):
	course = split_courses[i].split(',')
	course_list.append(course)
courses = {}
for item in course_list:
	courses[int(item[0])] = item[1]	

# Reading questionnaire.csv and formatting as list to be read by createNewQuestion methods
questionText = []
csv_file = open("questionnaire.csv", "r")
whole_csv = csv_file.read()
csv_file.close()   
split_csv = whole_csv.split('\r') 
# may need to inc '\n' too for other op.systems
question_rows = []
for i in range(len(split_csv)):
 	question_split = split_csv[i].split("|")
	question_rows.append(question_split)
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
		self.grid()
		self.createTeamExpQuest(0)
		self.createButtons()
		#self.createManageButton()


    def createTeamExpQuest (self, quesionNo):
		lblProg = Label(self, text=questionText[quesionNo][0], height=3, anchor=W, font=('MS', 22), padx=50, pady=30, wraplength=600, background='#CF4858')    
		# Label(master, text=longtext, anchor=W, justify=LEFT)  
		lblProg.grid(row=1, column=4, columnspan=5, rowspan=3, padx=260, pady=100)

		# THIS CONFIG APPROACH SHOULD WORK TO HIDE EXCESS TEXT????????
		# textvariable=


    def createButtons(self):
		butYes = Button(self, text='YES',font=('MS', 24,'bold'), bd=0, padx=60, pady=30)
		butYes['command']=self.createNewQuestionA     #Note: no () after the method
		butYes.grid(row=5, column=5, columnspan=2)	

		butNo = Button(self, text='NO',font=('MS', 24,'bold'), background='green', padx=60, pady=30, highlightthickness=0)
		butNo['command']=self.createNewQuestionB      #Note: no () after the method
		butNo.grid(row=5, column=6, columnspan=2)	

		
    def createManageButton(self):
		# if (loggedIn):	
		butManageQs = Button(self, text='Manage Questions',font=('MS', 15,'bold'), background='green', padx=10, pady=10, highlightthickness=0)
		butManageQs['command']=self.manageQuestionnaire      #Note: no () after the method
		butManageQs.grid(row=1, column=5, columnspan=3)


    def displayCourseInfo(self, courses):
        print courses.values()
        self.master.destroy()
        for directory, subdirectories, files in os.walk("./students"):
            ID = len(files)
            name ="./students/" + "c" + str(ID) + ".csv"
            with open(name, 'a+') as csvfile:
                        writer = csv.writer(csvfile,delimiter='|')
                        writer.writerow([str(courses.values())])



    def createCourseLink(self, courses):
		for key in courses:
			butCourse = Button(self, text=courses[key],font=('MS', 44,'bold'), background='blue', padx=80, pady=40)
			butCourse['command']=lambda :self.displayCourseInfo(courses)     #Note: no () after the method
			butCourse.grid(row=5, column=4, columnspan=5, rowspan=4)


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

    def manageQuestionnaire(self):
			editGuide = Text(self, height=10, font=('MS', 14, "bold"), background='#CF4858', padx=20, pady=20)
			editGuide.grid(row=1, column=1, columnspan=10, rowspan=2, padx=100, pady=(10,0))
			editGuide.insert("1.0", "Edit the Questionnaire below. 	All but the last Question should contain the following 5 sections seperated by '|'. The final question should only include text introducing the selected course.\n1: The Question text \n2&3: A single digit for the next question (starting at 0) on answering Yes/No respectively.\n4&5: Digit(s) (seperated by commas) relating to which course(s) can be eliminated from the list below on ansering Yes/No respectively.\n\n")
			editGuide.insert("7.0", courses)
			editGuide.config(state=DISABLED)
			editScreen = Text(self, height=16, font=('MS', 14), fg='white', background='#CF4858', padx=20, pady=20)
			editScreen.grid(row=3, column=1, columnspan=8, rowspan=10, padx=100)
			x = 1
			for i in range(len(whole_csv)):
					editScreen.insert((str(x)+".0"), whole_csv[i])
					global x
					x+=1	
			butSaveQs = Button(self, text='Save',font=('MS', 15,'bold'), highlightthickness=0, padx=10, pady=5, command=lambda: self.saveQuestionnaire(editScreen.get("1.0",'end-1c')))     
	 		butSaveQs.grid(row=12, column=8, columnspan=2)	
			
    def saveQuestionnaire(self, input):
			verifying = input.splitlines()
			okSave = True
			for i in range(len(verifying)-1):
				sections = verifying[i].split('|')
				# code below verifies requirements outlined in editGuide Textbox are met
				if len(sections) == 5 and len(sections[1]) == 1 and sections[1].isdigit() and len(sections[2]) == 1 and sections[2].isdigit() and (y.isdigit() for y in range(len(sections[3].split(',')))) and (z.isdigit() for z in range(len(sections[4].split(',')))):	
					continue				
				else:
					tkMessageBox.showerror("Update Error", "Your changes don't comply with the format required.\n\nPlease check your updates and try again.")	
					okSave = False
			if (okSave):		
				new_file = open("questionnaire.csv", "w+")
				new_file.write(input)
				new_file.close()	
				tkMessageBox.showerror("Saved Successfully", "Your changes have successfully been recorded")	
				self.manageQuestionnaire	
			i = 1
			while i < 40:
				print("{}/40".format(i))
				self.simulateQuestionnaire(input, 0)
				i += 1

    def simulateQuestionnaire(self, input, number):
		verifying = input.splitlines()
		i=1
		print("RUNNING METHOD FOR Q NO: {}".format(number))
		print("INPUT Split Length = {}".format(len(verifying)))
		if number == (len(verifying)-1):
			print("GOT TO FINAL QUESTION")
		elif number > (len(verifying)-1):				
			print("One of the questions ({}) is pointing to a question that doesn't exist. SEE Qno v Length".format(number))
		else:	
			while i < 10:
				if number < (len(verifying)-1):
					print("{}/10".format(i))
					nextQ = verifying[number].split('|')
					self.simulateQuestionnaire(input, nextQ[(random.randint(1,2))])
				else:
					print("Stuck getting to Question number: {}".format(number))
					break	
				i+=1				
# Main
#root = Tk()
#root.resizable(width=FALSE, height=FALSE)
#root.configure(background='#4D505B')
#root.geometry('{}x{}'.format(1200, 600))
#root.title("Questionnaire")
#app = Questionnaire(root)
#app.configure(background='#4D505B')
#root.mainloop()



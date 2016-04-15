from  cmtOptions import *
import string
from Tkinter import *
import random


class cmtQuestions:
    def __init__(self,id,question = ""):
        self.question = question
        self.options = []
        self.id = id

    def addOptions(self,option):
        self.options.append(option)

    def deleteOptions(self,position):
        self.options.pop(position)

    def __str__(self):
        Qstring = str(self.question) + "\n"
        for i in range(len(self.options)):
            Qstring = Qstring + "{}: {} \n".format(chr(65 + i),self.options[i])
        return Qstring

    def length(self):
        count = 0
        for i in range(len(self.options)):
            if self.options[i].correctness == True:
                count += 1
        return "{} options with {} are true".format(len(self.options),count)

    def wrapper(self):
        temp = []
        temp = self.options
        text = self.question
        options = []
        for i in range(len(temp)-1,-1,-1):
            tmp = random.randint(0,i)
            options.append(temp[tmp])
            del temp[tmp]
        return text,options

if __name__ == "__main__":
    Q1 = cmtQuestions("Q1")
    o1 = cmtOptions("a1",True)
    Q1.addOptions(o1)
    o2 = cmtOptions("b1",False)
    o3 = cmtOptions("c1",False)

    Q1.addOptions(o2)
    Q1.addOptions(o3)
    a,b = Q1.wrapper()
    print(a,b)
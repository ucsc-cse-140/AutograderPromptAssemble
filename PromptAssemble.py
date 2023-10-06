import os, sys

def PromptAssemble(assignmentNum, questionNum, answerFuncName):
    
    prompt = "Students are tasked with answering the following question: \n"
    
    #Load assignment sheet
    if assignmentNum >= 0 & assignmentNum <= 4:
        assignment = open("instructions/p" + str(assignmentNum) + ".md")
    else:
        print("No assignment #" + assignmentNum)
        return "Say the word 'Error'"
        
    #Add question to prompt    
    splitText = assignment.read().split("####")
    selectQ=0
    #Question is 1-3, Problem is 0, doesn't work for 4
    while not (splitText[selectQ].startswith("Question " + questionNum) | splitText[selectQ].startswith("Problem " + questionNum)):
        selectQ++
        if selectQ > len(splitText):
        print ("Question " + questionNum + " does not exist")
        return "Say the word 'Error'"
    prompt = prompt + splitText[selectQ] + "\n"
    
    
    
    
PromptAssemble(1, 1, "irrelevant")
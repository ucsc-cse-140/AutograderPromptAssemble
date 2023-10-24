import os, sys

def switch_assignment_function(assignment, question):
    switch = {
        # Assignment 0
        (0, 1): ("buyLotsOfFruit.py", "buyLotsOfFruit"),
        (0, 2): ("shopSmart.py", "shopSmart"),
        # Assignment 1
        (1, 1): ("search.py", "depthFirstSearch"),
        (1, 2): ("search.py", "breadthFirstSearch"),
        (1, 3): ("search.py", "uniformCostSearch"),
        (1, 4): ("search.py", "aStarSearch"),
        (1, 5): ("search.py", "breadthFirstSearch"),
        (1, 6): ("searchAgent.py", "cornersHeuristic"),
        (1, 7): ("searchAgent.py", "foodHeuristic"),
        (1, 8): ("searchAgent.py", "ClosestDotSearchAgent"),
        (1, 9): ("searchAgent.py", "ApproximateSearchAgent"),
        # Assignment 2
        (2, 1): ("multiAgents.py", "ReflexAgent"),
        (2, 2): ("multiAgents.py", "MinimaxAgent"),
        (2, 3): ("multiAgents.py", "AlphaBetaAgent"),
        (2, 4): ("multiAgents.py", "ExpectimaxAgent"),
        (2, 5): ("multiAgents.py", "betterEvaluationFunction"),
        (2, 6): ("multiAgents.py", "ContestAgent"),
        # Assignment 3
        (3, 1): ("valueIterationAgent.py", "ValueIterationAgent"),
        (3, 2): ("analysis.py", "question2"),
        (3, 3): ("analysis.py", "question3"), #divided into 3a through 3e
        (3, 4): ("qLearningAgents.py", "QLearningAgent"),
        (3, 5): ("qLearningAgents.py", "getAction"), #the one in QLearningAgent
        (3, 6): ("analysis.py", "ContestAgent"),
        (3, 7): ("", ""),
        (3, 8): ("", ""),
        (3, 9): ("qLearningAgents.py", "ApproximateQAgent"),
    }
    
    return switch.get((assignment, question), ("", ""))


def PromptAssemble(assignmentNum, questionNum, score, scoreMax):
    
    prompt = "Students are tasked with answering the following question: \n\n"
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
    while not (splitText[selectQ].strip().startswith("Question " + str(questionNum)) | splitText[selectQ].strip().startswith("Problem " + str(questionNum))):
        selectQ = selectQ+1
        if selectQ > len(splitText):
            print ("Question " + questionNum + " does not exist")
            return "Say the word 'Error'"
    prompt = prompt + splitText[selectQ] + "\n\n"
    
    print(prompt)
    
    prompt = prompt + "The student's answer is as follows:\n\n"
    
    print(prompt)
    
    #Get to start of question
    answerLocation=switch_assignment_function(assignmentNum, questionNum);
    print(answerLocation[0])
    with open(answerLocation[0]) as f:
        reachedStart = False
        blockComment = False
        for line in f:
            if "\"\"\"" in line:
                blockComment = not blockComment
            if not blockComment:
                if answerLocation[1] in line:
                    reachedStart=True
                if reachedStart: #no else, so it starts on function declaration
                    if not "\"\"\"" in line:
                        prompt = prompt + line + "\n"
                    if 'return' in line:
                        break
                    
    prompt = prompt + "The student scored " + str(score) + " points out of a maximum " + str(scoreMax) + ". Explain what they might have gotten wrong."
    
    print(prompt)
                
        
    
    
    
PromptAssemble(1, 1, 3, 3)
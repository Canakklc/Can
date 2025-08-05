subjectUserData ={
    "FirstUser":[]
}
QuestionsAndResults ={
    "firstQuestion":[],
    "secondQuestion":[],
    "thirtQuestion":[],
    "fourthQuestion":[],
    "fifthQuestion":[]
}


def Questioning():
    global subjectUserData
    userData = str(input("User name,age and gender"))
    subjectUserData["FirstUser"].append(userData)
    newUserData=f"**{userData}"
    print(subjectUserData)
    

def Testing():
    global QuestionsAndResults
    print("Please answer the questions only with yes/no")
    #first question
    firstQuestion=str(input("Do you have fewer?"))
    if firstQuestion == "yes":
        fewer=int(input("Please enter your fewer"))
        QuestionsAndResults["firstQuestion"].append(f"Has fewer{fewer}")
        
        
    elif firstQuestion =="no":
        QuestionsAndResults["firstQuestion"].append("Has no fewer")
    #Second Question
    SecondQuestion =str(input("Do you have coughing?"))
    if SecondQuestion == "yes":
        QuestionsAndResults["secondQuestion"].append("has coughing")
    else:
        QuestionsAndResults["secondQuestion"].append("has no coughing") 
    #Thirt Question
    ThirtQuestion = str(input("Do you have aches on any place of your body?"))
    if ThirtQuestion == "yes":
        QuestionsAndResults["thirtQuestion"].append("has aches")
    else:
        QuestionsAndResults["thirtQuestion"].append("has no aches")
    #Fourth Question
    
    forthQuestion=int(input("For how long you have been feeling discomfort?"))
    
    QuestionsAndResults["fourthQuestion"].append(f"Pacient has been feeling discomfor for {forthQuestion} days")
    #Fifth Question
    FifthQuestion =str(input("Have you had a contact with a covid pacient within one week or less?"))
    if FifthQuestion == "yes":
        QuestionsAndResults["fifthQuestion"].append("Pacient has contact")
    else:
        QuestionsAndResults["fifthQuestion"].append("Patient has no contact")

    for questions,answers in QuestionsAndResults.items():
        print(f"----{questions}")
        for answers in answers:
            print(f"*{answers}")    

        
                   

Questioning()
Testing()    







    

quiz =int(input("quiz note"))
midtern = int(input("midterm note"))
final =int(input("final note"))


def calculateAverage(quiz,midtern,final):
    quizVal =quiz * 0.2
    if quiz<59:
        print(f"be more carefull next time{quiz}")
    midternVal =midtern * 0.3  
    finalVal =final *0.5 
    Average=quizVal+midternVal+finalVal
    
    return Average

    
        
   

Marks =calculateAverage(quiz,midtern,final)

def canPassOrNot(Marks):
    if Marks <59:
        print(f"Student has failed with{Marks}")
        return
    else:
        print(f"Student has passed with {Marks}")


canPassOrNot(Marks)      


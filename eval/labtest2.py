# Evaluation
# Harsh Kashyap         
# CSE4(2COPC4)    
# 101917088   
# hkashyap_be19@thapar.edu    
# 8051625669
# Thapar Institute Of Engineering And Technology

#Consider the following 2-SAT problem with 4 Boolean variables a, b, c, d:
#The MOVEGEN function to generate new solution be arbitrary changing value of any one
#variable
#Let the candidate solution be of the order (abcd) and the initial candidate solution be (1111).
#Let heuristic to evaluate each solution be number of clauses satisfied in the formula.
#Apply Simulated Annealing (Consider T= 500 and cooling function = T-50)
#Accept every good move and accept a bad move if probability is greater than 50%.

#F=(¬a\/d)/\(c\/b)/\(¬c\/¬d)/\(¬d\/¬b)/\(¬a\/¬d)

import copy
import math
import random                                                           #importing random funcction
def evaluatingF(element):
    Enext=0                                                             # to store the next E or heuristic value
    clause1=not(element[0])or element[3]                                # the first clause in question  ¬a\/d
    clause2=element[2] or element[1]                                    # the second clause in question  c\/b
    clause3=not(element[2]) or not (element[3])                         # the third clause in question  ¬c\/¬d
    clause4=not(element[3]) or not(element[1])                          # the fourth clause in question  ¬d\/¬b
    clause5=not(element[0]) or not(element[3])                          # the fifth clause in question  ¬a\/¬d
    x=(clause1) and (clause2) and (clause3) and (clause4) and (clause5) # anding all the clause
    #checking no. of clauses which turn to be true, This will add up to the heuristic value
    if clause1:
        Enext=Enext+1
    if clause2:
        Enext=Enext+1
    if clause3:
        Enext=Enext+1
    if clause4:
        Enext=Enext+1
    if clause5:
        Enext=Enext+1
    #return this state
    return x,Enext
    
    
#fn that takes in the variables and a randomly chose variable whose value is to be swapped. 
#only two values possible 0 or 1 . So, we will do a not
def moveGen(element,index):
    newstate=copy.deepcopy(element)                                 #deepcopy to copy the matrix
    newstate[index]=not(newstate[index])                            #not to change value of 0 to1 and vice versa
    return newstate 
    
#fn to print value of matrix in 0 or 1 format
def printM(matrix):
    print('a:',int(matrix[0]),', b:',int(matrix[1]),', c:',int(matrix[2]),', d:',int(matrix[3]),)

#fn to print value of matrix in true or false format
def printMB(matrix):
    print('a:',bool(matrix[0]),', b:',bool(matrix[1]),', c:',bool(matrix[2]),', d:',bool(matrix[3]),'\n')
    
#Simulated Annealing
def SimulatedAnnealing(element, Ecurrent,T,res):
    bestCase=element                            #taking initial cse as best case
    check=False                                 #flag to see if we reach goal state or not
    while T>0:
        better=False                            #flag for intermediate states
        print('\n--------------------------------------------------------------------')
        print('\nTemperature T : ',T)           #temperature
        #res,Ecurrent=evaluatingF(bestCase)
        if res :                                #if the resultant boolean expression is true then goal state found
            print("\n\tYayyy!!!")
            print("\nReached End state\t Optimal state")
            print("And values are : ")
            printM(bestCase)
            print('\tOr')
            printMB(bestCase)
            check=True
            break
        var = random.randint(0, 3)              #randomly choose a bit to manipulate
        nextstate=moveGen(bestCase, var)        #generate a random state by changing one bit
        resNext,Enext=evaluatingF(nextstate)    #getting E and resultant boolean expression of new state
        exponent= (Enext- Ecurrent)/T           #evaluating fn
        Probab=(1/(1+math.exp(-exponent)))      #finding the probability of the fn using sigmoidal fn
        if (Enext-Ecurrent)>0 or Probab>0.5:    #checks if it is good move or if not a good move then probability better than 0.5
            better=True                         #if a better state is found
            bestCase=nextstate                  #make the best state to next state    
            print('The next Base State is : ')
            printM(bestCase)
            print('\nAnd its value of E is : ',Enext)
            res=resNext
            Ecurrent=Enext                      #update value of current and next res and E(Heuristic) for next iteration
        print('Probability : ',Probab)  
        T=T-50                                  #keep updating value of T
        if not better :
            print('No better state in this particular iteration as the found E was',Enext)
    if not check:
        print('\nReached end of this iteration.Sorry')
        print('Please redo RUN to find a value')
        
        
if __name__== "__main__":
    print("\n\t2 SAT Problem\n")
    print('--------------------------------------------------------------------')                                
    Ecurrent=0              #stores the current heuristuic value
    T=500                   #stores the current time
    #element=[False,False,True,False]
    #element=[True,True,True,True]               
    #[a,b,c,d]
    element=[bool(1),bool(1),bool(1),bool(1)]           # or element =[1,1,1,1] both will work
    print('Initial base state')
    printM(element)
    print('And its value of E is : ',Ecurrent)
    res,Ecurrent = evaluatingF(element)
    SimulatedAnnealing(element,Ecurrent,T,res)
    print('--------------------------------------------------------------------')

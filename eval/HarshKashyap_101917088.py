# Harsh Kashyap         
# CSE4(2COPC4)    
# 101917088   
# hkashyap_be19@thapar.edu    
# 8051625669


# MORE EFFCIENT METHOD without using queue 
# NOTE : We can have even a more efficient approach, by not printing intermediate states. 
# Priniting intermediate states takes time. Please comment out print lines for even faster result 
################################################################################
import copy
import queue
from numpy import random                                        #importing random funcction
import time

#fn to generate a 3X3 matrix which is unique  MORE EFFICIENT APPROACH
def genState():
    puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]                          #generate an array of size 9    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(puzzle)                                      #shuffle the elements of array
    state=[]                                                    #appending list
    for i in range(3):                                          #run the loop for 3 times
        ind=3*i
        temp=[]                                                 #create a temporary array that will store 3 values at a time
        temp.append(puzzle[ind+0])                              #keep on inserting in values 0,3,6
        temp.append(puzzle[ind+1])                              #keep on inserting in values 1,4,7
        temp.append(puzzle[ind+2])                              #keep on inserting in values 2,5,8
        state.append(temp)                                      #will store a list in list of list
    return state                                                #return the newly generated random 8 puzzle problem


#LESS EFFICIENT APPROACH
'''
#fn to generate a new 3X3 matrix
#took help of W3schools for random array regeration
def genState():
                                                                #loop will run until a unique 3X3 matrix is generated
    while (True):
        x = random.randint(9, size=(3, 3))                      #generation of 3X3 matrix
        res = list(set(i for j in x for i in j))                #will find all the unique value in the matrix x
        if (len(res)==9):   #(len(res)==len(x)*len(x[1])):      #if the number of unique element is 9, the no element is repeated hence break, if not repeat the procedure
            return x.tolist()                                   ##convert the array generated to a list
'''

#fn to print the heuristic of the newstate with the goal state
def heuristic(state, newstate): 
    diff=0                                                      #count the no. of tiles that do not match
    for i in range(3):                                          #3=len(state) is row of state
        for j in range(3):                                      #3=len(state[1]) is column of state
            if(state[i][j]!=newstate[i][j]):                    #check if the two tiles do not match
                diff=diff+1                                     #increase the count for the tiles that do not match
    return diff


#fn to find the position of zero or empty tile
def findzero(list,zero):
    for i in range(3):                                          #3=len(state) is row of state
        for j in range(3):                                      #3=len(state[1]) is column of state
            if(list[i][j]==zero):                               #check if the given tile is zero or not
                return (i,j)                                    #if found return the row and col

#fn to move the zero right
def right(i,j,list):
    newstate=copy.deepcopy(list)                                #deepcopy to copy the matrix
    if(j<2):                                                    #q=len(state[1])-1 condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
                                                                #if condition is satisfied, then swap it
        swap=newstate[i][j+1]
        newstate[i][j+1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate                                             #return the updated position matrix as the new state

#fn to move the zero left
def left(i,j,list):
    newstate=copy.deepcopy(list)                                #deepcopy to copy the matrix
    if(j>0):                                                    #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
                                                                #if condition is satisfied, then swap it
        swap=newstate[i][j-1]
        newstate[i][j-1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate                                             #return the updated position matrix as the new state

#fn to move the zero up
def up(i,j,list):
    newstate=copy.deepcopy(list)                                #deepcopy to copy the matrix
    if(i>0):                                                    #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
                                                                #if condition is satisfied, then swap it
        swap=newstate[i-1][j]
        newstate[i-1][j]=newstate[i][j]
        newstate[i][j]=swap
    return newstate                                             #return the updated position matrix as the new state

#fn to move the zero down
def down(i,j,list):
    newstate=copy.deepcopy(list)                                #deepcopy to copy the matrix
    if(i<2):                                                    # 2=len(state[1])-1    condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
                                                                #if condition is satisfied, then swap it
        swap=newstate[i+1][j]
        newstate[i+1][j]=newstate[i][j]
        newstate[i][j]=swap
    return newstate                                             #return the updated position matrix as the new state


#fn to perform HillClimb
def HillClimb(state, goal):
    first=True                                                  #a flag for initial state so that state doe not generate
    countState=0                                                #count the no. of state
    count=0                                                     # count total iterations
    while(True):                                                #keep running the loop
        print("\n--------------------------------------------------------------")
        if(first):                                              #if it is first then make the condition false
            first=False                                         #this works onky once during the iteration of first condition where matrix random generation is not required
        else:                       
            print("\nWorking for a random Initial state")
            state=genState()                                    #generate a new state
            if(state==goal):                                    #if the randomly generated state is same as the goal state then no step further.
                print("Oops!! generated a state same as goal state")
                continue                                        #will ignore such case and make sure random state is not same as base state
        countState=countState+1                                 #increment the counter
        visited = []                                            #queue to keep the visited state. so that a state is not repeated
        oHV = heuristic(state, goal)                            #heuristuc value of the state
        path=[]                                                 #to print the path or the intermediate states
        found=False                                             #found to check if state==goal
        print("Initial State Matrix generated :\n", state)
        counter=0                                               #count each iterations
        while(True):
            counter =counter+ 1                                 #increment counter by 1
            visited=visited+[state]                             #add the given state into visited
            path=path+[state]                                   #add the state in path
            row,col=findzero(state,0)                           #find the index of (0)
            print("Initially zero is present at ",row," ",col)
            heuristicFound=False                                #to check if value of heuristic and the next 4 child states. If the value of any next 4 state is less than parent state from which they are generated, then heuristicFound=true else it will remain to true
            print("\n\nLoop ", counter)     
            print("STATE---",state)
            #up
            updatedState = up(row,col,state)    
            if(updatedState==goal):                             #if updatedState is goal state, then break
                found=True                  
                break
            else:
                if(not(updatedState in visited)):       
                    HV=heuristic(updatedState,goal)             #find the heuristic value of updatedState
                    if(HV<oHV):                                 #if the next state which has lesser heuristic value will be the next state
                        freshState= updatedState                #updated the fresh state to the updatedState  #fresh state the state with least heuristic value
                        oHV=HV                                  #make this new heuristic value the old heuristic value, next states heuristic value will be compared from this val
                        heuristicFound=True                     #if found then this state will proceed and further depth will be serached.

            #down
            updatedState = down(row,col,state)
            if(updatedState==goal):
                found=True
                break
            else:
                if(not(updatedState in visited)):
                    HV=heuristic(updatedState,goal)             #find the heuristic value of updatedState
                    if(HV<oHV):                                 #the next state which has lesser heuristic value will be the next state
                        freshState= updatedState                #updated the fresh state to the updatedState
                        oHV=HV                                  #make this new heuristic value the old heuristic value, next states heuristic value will be compared from this val
                        heuristicFound=True                     #if found then this state will proceed and further depth will be serached.
            
            #left
            updatedState = left(row,col,state)
            if(updatedState==goal):
                found=True
                break
            else:
                if(not(updatedState in visited)):
                    HV=heuristic(updatedState,goal)             #find the heuristic value of updatedState
                    if(HV<oHV):                                 #the next state which has lesser heuristic value will be the next state
                        freshState= updatedState                #updated the fresh state to the updatedState
                        oHV=HV                                  #make this new heuristic value the old heuristic value, next states heuristic value will be compared from this val
                        heuristicFound=True                     #if found then this state will proceed and further depth will be serached.

            #right
            updatedState = right(row,col,state)
            if(updatedState==goal):
                found=True
                break
            else:
                if(not(updatedState in visited)):
                    HV=heuristic(updatedState,goal)             #find the heuristic value of updatedState
                    if(HV<oHV):                                 #the next state which has lesser heuristic value will be the next state
                        freshState= updatedState                #updated the fresh state to the updatedState
                        oHV=HV                                  #make this new heuristic value the old heuristic value, next states heuristic value will be compared from this val
                        heuristicFound=True                     #if found then this state will proceed and further depth will be serached.
            
            if(not(heuristicFound)):                            #no state has lesser value than the initial state then break it. Hill Climbing won't work. Will search for a new array 
                break
            else:
                state=freshState                                #will go deeper into the state with least heuristic value
        print("\nTotal time for this particular initial state = ",counter)
        count=counter+count                                     #count- counts grand total no. of iteration. counter-counts iteration for each array
        if(found):                                              #if goal state is same as the intermediate state -> found is true
            print("Found.\tYayyyy!!! Works")
            path=path+[goal]                                    #add the goal state to the path as well
            print("--------------------Conclusion--------------------")
            print("Goal state can be achieved from initial state matrix -> ",path[0])
            print ("\nPATH \n")
            for i in path:                                      #for proper display of path
                print(i)
                print("                 |   ")
                print("                 |   ")
                print("                 \/")
            print("No. of random states generated is ",countState)
            print("Total iterations is  ",count)
            break                                               #end loop. No more iterations required
        else:
            print("Not Found. This initial state does not work. ")



if (__name__== "__main__"):
    start=time.time()                                           # a stopwatch
    print("\nHILL Climbing Search Algo")
    state=[[1,2,3],[8,0,4],[7,6,5]]                             #initial state
    goal=[[2,8,1],[0,4,3],[7,6,5]]                              #goal state
    print("Initial State \n",state)
    print("Goal state to be achieved, \n",goal)
    HillClimb(state,goal)                        
    print("Total time = ",round((time.time()-start),1))         #keeps time instance

# LESS EFFICIENT METHOD
########################################################################
#Evaluation
"""
import copy
import sys
import queue
from numpy import random            #importing random funcction
import time

#fn to check if the state achieved is equal to the goal state
def equalitycheck(state, newstate):
    for i in range(len(state[1])):          #len(state[1]) is row of state
        for j in range(len(state[1][i])):   #len(state[1]) is column of state
            if(state[1][i][j]!=newstate[1][i][j]):      #if even one single position fails to match, return false
                return False
    return True                     #otherwise return true


#fn to print the heuristic of the newstate with the goal state
def heuristic(state, newstate): 
    diff=0          #count the no. of tiles that do not match
    for i in range(len(state[1])):      #len(state[1]) is row of state
        for j in range(len(state[1][i])):   #len(state[1]) is column of state
            if(state[1][i][j]!=newstate[1][i][j]):      #increase the count for the tiles that do not match
                diff=diff+1
    return diff


#fn to find the position of zero or empty tile
def findzero(list,zero):
    for i in range(len(list[1])):
        for j in range(len(list[1][i])):
            if(list[1][i][j]==zero):        #check if the given tile is zero or not
                return (i,j)

#fn to move the zero right
def right(i,j,list):
    newstate=copy.deepcopy(list)
    if(j<(len(list[1][i])-1)):      #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[1][i][j+1]
        newstate[1][i][j+1]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

#fn to move the zero left
def left(i,j,list):
    newstate=copy.deepcopy(list)
    if(j>0):                    #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[1][i][j-1]
        newstate[1][i][j-1]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

#fn to move the zero up
def up(i,j,list):
    newstate=copy.deepcopy(list)
    if(i>0):            #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[1][i-1][j]
        newstate[1][i-1][j]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

#fn to move the zero down
def down(i,j,list):
    newstate=copy.deepcopy(list)
    if(i<(len(list[1])-1)):         #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[1][i+1][j]
        newstate[1][i+1][j]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate
    
def genState():
    arr=[i for i in range(0,9)]
    random.shuffle(arr)
    li=[]
    for i in range(3):
        p=[]
        p.append(arr[(3*i)+0])
        p.append(arr[(3*i)+1])
        p.append(arr[(3*i)+2])
        li.append(p)
    return li
    
#fn to generate a new 3X3 matrix
def genState():
    #loop will run until a unique 3X3 matrix is generated
    while (True):
        x = random.randint(9, size=(3, 3))      #generation of 3X3 matrix
        res = list(set(i for j in x for i in j))            #will find all the unique value in the matrix x
        if (len(res)==9):   #(len(res)==len(x)*len(x[1])):          #if the number of unique element is 9, the no element is repeated hence break, if not repeat the procedure
            return x.tolist()   ##convert the array generated to a list

  
#fn to generate a new 3X3 matrix Efficient APProach
def genState():   
    while True:             #loop will run until a small heuristic value is found
        while (True):       #loop will run until a unique 3X3 matrix is generated
            x = random.randint(9, size=(3, 3))      #generation of 3X3 matrix
            res = list(set(i for j in x for i in j))            #will find all the unique value in the matrix x
            if (len(res)==9):   #(len(res)==len(x)*len(x[1])):          #if the number of unique element is 9, the no element is repeated hence break, if not repeat the procedure
                break
        x.tolist()          ##convert the array generated to a list
        s=[10,x]
        s[0]=heuristic(goal,s)
         #print(x)
        if(s[0]<=3):         #to prevent large iterations will make sure only those matrices are done Hill climbing where utmost misplaced tile is 3
            return x.tolist()    #return the unqiue 3X3 matrix as base condition

#fn to perform HillClimb
def HillClimb1(state,goal):
    countState=0            #will count toal no. of initial state taken before we got an initial state that helps us achieve the goal state
    totalCount=0            #will count toal no. of times the inner loop runs or basically total time or iteration the Hill Climb algo runs in this case
    given =True             #if the given base condition in question works, a flag for base condition only so that random array is not generated during firsy iteration
    path=[]                 #will store the right path from initial state to goal state
    #loop that keeps on running until we get a bse state that can make us reach the goal state
    while(True):
        print("\n--------------------------------------------------------------")
        print("\nWorking for a random Initial state")
        path=[]             #path will be set to fresh every time the initial state fails to reach a goal state 
        countState=countState+1         #increment the count of states generated by 1
        state[0]=10                    #give the initial heuristic vales as 10 , since max posssible heuristic value can be 9
        if(not(given)):                 #if its not the first iteration then generate a random bas state
            state[1]= genState()        #receive the state
        state[0]=heuristic(state,goal)
        print("Initial State Matrix generated :\n", state[1])
        queue=[] +[state]               #append initial state in the queue
        k,l=findzero(state,0)           #find the index of zero in bas state
        print("Initially zero is present at ",k," ",l)
        visited =[]+[state]             #append the state in visited so that it is not visited once again
        check=False                     #checking if state can be goaled successfully or not
        counter=0                       #count no. of iterations of each particular base state
        #loop that runs for each particular state 
        while(True):
            if(len(queue)==0):          #if there are no elements to be gone by in queue,break
                break
            #totalCount=totalCount+1           #increment counter by 1
            counter=counter+1
            state=queue.pop(0)           #pop a new state
            path=path+[state[1]]        #add it to the path
            queue.clear()               #clear the queue
            k,l=findzero(state,0)        #finding the position of zero every time for the next state to swap
            print("\n\nLoop ", counter)
            print("STATE---",state)
            #UP
            ns=up(k,l,state)
            #if the new state after moving up and goal is same , we got it 
            if(equalitycheck(goal,ns)):
                check=True
                print("\nFound ")
                print(ns)
                break
            #else we will add the state in queue if it not already visited and we  will calculate its heuristic value
            else:
                if (not(ns in visited)):
                    ns[0]=heuristic(goal,ns)
                    queue= queue+[ns]


            #DOWN
            ns=down(k,l,state)
            #if the new state after moving down and goal is same , we got it 
            if(equalitycheck(goal,ns)):
                check=True
                print("\nFound ")
                print(ns)
                break
            #else we will add the state in queue if it not already visited and we  will calculate its heuristic value
            else:
                if (not(ns in visited)):
                    ns[0]=heuristic(goal,ns)
                    queue= queue+[ns]



            #LEFT
            ns=left(k,l,state)
            #if the new state after moving left and goal is same , we got it 
            if(equalitycheck(goal,ns)):
                check=True
                print("\nFound ")
                print(ns)
                break
            #else we will add the state in queue if it not already visited and we  will calculate its heuristic value
            else:
                if (not(ns in visited)):
                    ns[0]=heuristic(goal,ns)
                    queue= queue+[ns]

            #RIGHT
            ns=right(k,l,state)
            #if the new state after moving right and goal is same , we got it 
            if(equalitycheck(goal,ns)):
                check=True
                print("\nFound ")
                print(ns)
                break
            #else we will add the state in queue if it not already visited and we  will calculate its heuristic value
            else:
                if (not(ns in visited)):
                    ns[0]=heuristic(goal,ns)
                    queue= queue+[ns]
            
            queue.sort()            #sort the queue in min order of its heuristic value
            fresh=queue[0]          #fresh has the least heuristic value element
            print("QUEUE  --- ",queue)
            print("Visited" ,visited)
            if(fresh[0]>=state[0]):         #if the heuristic value of the newly achieved element is greater than the original state, this path is wrong, and we will come out of loop
                break
            else:
                visited=visited+[fresh]     #else continue the approach and add the new state to visited 
        print("\nTotal time for this particular initial state = ",counter)
        totalCount=totalCount+counter       #add the time of this particular state to the total time
        if(not(check)):                     #if this state does not achieve goal state
            print("Not Found. This initial state does not work. ")
            if(given):                      #if its first iteration make it false, signifying first iteration is over
                given=False
        else:                               #if we achieved the goal state
            print("Yayyyy!!! Works")
            path=path+[goal[1]]               #add the goal state to the path as well
            print("--------------------Conclusion--------------------")
            print("Goal state can be achieved from initial state matrix -> ",path[0])
            print ("\nPATH \n")
            for i in path:
                print(i)
                print("                 |   ")
                print("                 |   ")
                print("                 \/")
            print("No. of random states generated is ",countState)
            print("Total iteration is ",totalCount)

            break   




if (__name__== "__main__"):
    start=time.time()
    print("\nHILL Climbing Search Algo")
    state=[[1,2,3],[8,0,4],[7,6,5]]          #initial state
    goal=[[2,8,1],[0,4,3],[7,6,5]]]              #goal state
    print("Goal state to be achieved, \n",goal[1])
    res=heuristic(state,goal)
    goal[0]=res

    HillClimb1(state,goal)
    print("Total time = ",time.time()-start)
"""
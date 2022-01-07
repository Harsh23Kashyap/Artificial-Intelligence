#Given two jugs- a 4 liter and 3 liter capacity. 
# Neither has any measurable markers on it. There
#is a pump which can be used to fill the jugs with water. 
# Simulate the procedure in Python to get
#exactly 2 liter of water into 4-liter jug
import copy
import sys
import queue

capacity=[4,3]  #initial (can be same or changed)
goal = 2    #goal state in JUG1
def equalitycheck(state):
    if(state[0]==goal ):
                return True
    return False

def transfer(list,i, j):
    newstate=copy.deepcopy(list)
    extra=newstate[i]
    newstate[j]=newstate[j]+newstate[i]
    if(j==0 and newstate[j]>capacity[0]):
        extra=newstate[j]-capacity[0]
        newstate[j]=4
    elif(j==1 and newstate[j]>capacity[1]):
        extra=newstate[j]-capacity[1]
        newstate[j]=capacity[1]
    newstate[i]=extra
    return newstate

def full(list,i):
    newstate=copy.deepcopy(list)
    if(i==0):
        newstate[i]=capacity[0]
    if(i==1):
        newstate[i]=capacity[1]
    return newstate

def empty(list,i):
    newstate=copy.deepcopy(list)
    newstate[i]=0
    return newstate


def BFS(state):
    queue=[] +[state]  #append initial state
    visited =[]+[state]
    check=False  #checking if state can be goaled successfully or not
    counter=0   #count no. of iterations
    ns=state
    while(len(queue)>0 and counter<10000):
        counter=counter+1
        state=queue.pop(0)
        #TRANSFER Case1
        ns=transfer(state,0,1)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                visited=visited+[ns]
                print(ns)
                queue= queue+[ns]


        #TRANSFER CASE 2
        ns=transfer(state,1,0)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                print(ns)
                visited=visited+[ns]
                queue= queue+[ns]
        
        #FULL CASE1
        ns=full(state,0)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                print(ns)
                visited=visited+[ns]
                queue= queue+[ns]

        #FULL CASE2
        ns=full(state,1)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                print(ns)
                visited=visited+[ns]
                queue= queue+[ns]

        #EMPTY CASE1
        ns=empty(state,0)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                print(ns)
                visited=visited+[ns]
                queue= queue+[ns]

        #EMPTY CASE2
        ns=empty(state,1)
        if(equalitycheck(ns)):
            check=True
            print("\nCongrats")
            print("Previous state = ")
            print(state)
            print("Intermediate state = ")
            print(ns)
            print("Reached the goal state ")
            break
        else:
            if (not((ns in visited) or ns in queue)):
                print(ns)
                visited=visited+[ns]
                queue= queue+[ns]

    if (check):
        ns=empty(ns,1)
        print(ns)
    if(not(check)):
        print("OOPS!!! Cannot Reach goal state ")   




if (__name__== "__main__"):
    state=[0,0]  #first is 4 litre and second is 3 litre
    capacity[0]=int(input("Enter size of jug1  : "))
    capacity[1]=int(input("Enter size of jug2  : "))
    goal=int(input("Enter the goal state : "))

    BFS(state)


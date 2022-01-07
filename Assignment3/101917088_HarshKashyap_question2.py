#If the initial and final states have been changed as below and approach you need to use is Hill
#Climbing searching algorithm. H(n): number of misplaced tiles in the current state n as
#compared to the goal node as the heuristic function for the following states

#NOT COMPLETE
import copy
import sys
import queue
# where 0 is blank space
#
#   1   2   3
#   8   x   4   
#   7   6   5

#   2   8   1
#   x   4   3   
#   7   6   5
def equalitycheck(state, newstate):
    for i in range(len(state[1])):
        for j in range(len(state[1][i])):
            if(state[1][i][j]!=newstate[1][i][j]):
                return False
    return True

def heuristic(state, newstate):
    diff=0
    for i in range(len(state[1])):
        for j in range(len(state[1][i])):
            if(state[1][i][j]!=newstate[1][i][j]):
                diff=diff+1
    return diff

def findzero(list,zero):
    for i in range(len(list[1])):
        for j in range(len(list[1][i])):
            if(list[1][i][j]==zero):
                return (i,j)

def right(i,j,list):
    newstate=copy.deepcopy(list)
    if(j<(len(list[1][i])-1)):
        swap=newstate[1][i][j+1]
        newstate[1][i][j+1]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

def left(i,j,list):
    newstate=copy.deepcopy(list)
    if(j>0):
        swap=newstate[1][i][j-1]
        newstate[1][i][j-1]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

def up(i,j,list):
    newstate=copy.deepcopy(list)
    if(i>0):
        swap=newstate[1][i-1][j]
        newstate[1][i-1][j]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate

def down(i,j,list):
    newstate=copy.deepcopy(list)
    if(i<(len(list[1])-1)):
        swap=newstate[1][i+1][j]
        newstate[1][i+1][j]=newstate[1][i][j]
        newstate[1][i][j]=swap
    return newstate


def BFS(state,goal):
    queue=[] +[state]  #append initial state
    k,l=findzero(state,0)
    print("Initially zero is present at ",k," ",l)
    visited =[]+[state]
    check=False  #checking if state can be goaled successfully or not
    counter=0   #count no. of iterations
    while(len(queue)>0 and counter<10000):
        counter=counter+1
        k,l=findzero(state,0)
        #if(len(queue)==0):
        #    break
        state=queue.pop(0)
        queue.clear()
        k,l=findzero(state,0)
        print("\n\nLoop ", counter)
        print("STATE---",state)
        #UP
        ns=up(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("\nFound ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                ns[0]=heuristic(goal,ns)
                queue= queue+[ns]


        #DOWN
        ns=down(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("\nFound ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                ns[0]=heuristic(goal,ns)
                queue= queue+[ns]



        #LEFT
        ns=left(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("\nFound ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                ns[0]=heuristic(goal,ns)
                queue= queue+[ns]

        #RIGHT
        ns=right(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("\nFound ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                ns[0]=heuristic(goal,ns)
                queue= queue+[ns]
        
        queue.sort()
        fresh=queue[0]
        print("QUEUE  --- ",queue)
        print("Visited" ,visited)
        if(fresh[0]>=state[0]):
            break
        else:
            visited=visited+[fresh]
    print("\nTotal time = ",counter)
    if(not(check)):
        print("\nNot Found ")   




if (__name__== "__main__"):
    print("\nHILL Climbing Search Algo\n")
    #state=[0,[[1,2,3],[8,0,4],[7,6,5]]]
    #state=[0,[[1,2,3],[4,0,5],[6,7,8]]]
    #state=[10,[[2,0,3],[1,8,4],[7,6,5]]]
    #state=[10,[[2,8,3],[1,5,4],[7,6,0]]]
    state=[10,[[1,2,3],[0,8,4],[7,6,5]]]
    goal=[0,[[2,8,1],[4,0,3],[7,6,5]]]
    #goal=[0,[[1,2,3],[8,0,4],[7,6,5]]]
    #goal=[[1,3,0],[8,2,4],[7,6,5]]
    #goal=[[2,8,1],[7,6,5],[0,4,3]]
    #goal=[4,[[2,1,3],[4,0,5],[6,7,8]]]
    res=heuristic(state,goal)
    goal[0]=res

    BFS(state,goal)


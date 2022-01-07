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
    for i in range(len(state)):
        for j in range(len(state[i])):
            if(state[i][j]!=newstate[i][j]):
                return False
    return True

def findzero(list,zero):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(list[i][j]==zero):
                return (i,j)

def right(i,j,list):
    newstate=copy.deepcopy(list)
    if(j<(len(list[i])-1)):
        swap=newstate[i][j+1]
        newstate[i][j+1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

def left(i,j,list):
    newstate=copy.deepcopy(list)
    if(j>0):
        swap=newstate[i][j-1]
        newstate[i][j-1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

def up(i,j,list):
    newstate=copy.deepcopy(list)
    if(i>0):
        swap=newstate[i-1][j]
        newstate[i-1][j]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

def down(i,j,list):
    newstate=copy.deepcopy(list)
    if(i<(len(list)-1)):
        swap=newstate[i+1][j]
        newstate[i+1][j]=newstate[i][j]
        newstate[i][j]=swap
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
        k,l=findzero(state,0)

        #UP
        ns=up(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("Found ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                visited=visited+[ns]
                queue= queue+[ns]


        #DOWN
        ns=down(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("Found ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                visited=visited+[ns]
                queue= queue+[ns]



        #LEFT
        ns=left(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("Found ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                visited=visited+[ns]
                queue= queue+[ns]

        #RIGHT
        ns=right(k,l,state)
        if(equalitycheck(goal,ns)):
            check=True
            print("Found ")
            print(ns)
            break
        else:
            if (not(ns in visited)):
                visited=visited+[ns]
                queue= queue+[ns]

    if(not(check)):
        print("Not Found ")   




if (__name__== "__main__"):
    #state=[[1,2,3],[8,0,4],[7,6,5]]
    state=[[1,2,3],[4,0,5],[6,7,8]]

    #goal=[[2,8,1],[0,4,3],[7,6,5]]
    #goal=[[1,3,0],[8,2,4],[7,6,5]]
    #goal=[[2,8,1],[7,6,5],[0,4,3]]
    goal=[[2,1,3],[4,0,5],[6,7,8]]

    BFS(state,goal)


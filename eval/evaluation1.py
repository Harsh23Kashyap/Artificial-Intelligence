import copy 
from numpy import random
import time
#fn to find the position of zero or empty tile
def findzero(list,zero):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(list[i][j]==zero):        #check if the given tile is zero or not
                return (i,j)


#fn to move the zero right
def right(i,j,list):
    newstate=copy.deepcopy(list)
    if(j<2):      #len(list[i])-1)#condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[i][j+1]
        newstate[i][j+1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

#fn to move the zero left
def left(i,j,list):
    newstate=copy.deepcopy(list)
    if(j>0):                    #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[i][j-1]
        newstate[i][j-1]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

#fn to move the zero up
def up(i,j,list):
    newstate=copy.deepcopy(list)
    if(i>0):            #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[i-1][j]
        newstate[i-1][j]=newstate[i][j]
        newstate[i][j]=swap
    return newstate

#fn to move the zero down
def down(i,j,list):
    newstate=copy.deepcopy(list)
    if(i<2):         #len(list)-1   #condition that checks whether the swapping is even possible or not(the index is not a boundary position where swapping isn't possible)
        #if condition is satisfied, then swap it
        swap=newstate[i+1][j]
        newstate[i+1][j]=newstate[i][j]
        newstate[i][j]=swap
    return newstate
  
#fn to print the heuristic of the newstate with the goal state
def heuristic(state, newstate): 
    diff=0          #count the no. of tiles that do not match
    for i in range(3):      #len(state)   #len(state[1]) is row of state    which is 3
        for j in range(3):   #len(state[i] #len(state[1]) is column of state    which is 3
            if(state[i][j]!=newstate[i][j]):      #increase the count for the tiles that do not match
                diff=diff+1
    return diff


#fn to generate a new 3X3 matrix
def genState():
    #loop will run until a unique 3X3 matrix is generated
    while (True):
        x = random.randint(9, size=(3, 3))      #generation of 3X3 matrix
        res = list(set(i for j in x for i in j))            #will find all the unique value in the matrix x
        if (len(res)==9):   #(len(res)==len(x)*len(x[1])):          #if the number of unique element is 9, the no element is repeated hence break, if not repeat the procedure
            return x.tolist()   ##convert the array generated to a list

def HillClimbing(start, final,count):
    visited = []
    parent_value = heuristic(start, final)
    distance=[]
    new = start
    while(True):
        count =count+ 1
        temp = new
        visited.append(temp)
        distance.append(new)
        row,col = findzero(temp,0) 
        for state in range(1,5):
            if(state == 1): 
                next = up(row,col,temp)
            if(state == 2): 
                next = down(row,col,temp)
            if(state == 3): 
                next = left(row,col,temp)
            if(state == 4):
                next = right(row,col,temp)
            if(next == final): 
                distance.append(final)
                print("Total Iteration: ", count)
                return True,count,distance
            if(next != temp and next not in visited): 
                hvalue = heuristic(next, final) 
                if(parent_value >= hvalue):
                    parent_value = hvalue
                    new = next
        if(new != temp):
                temp = new
        else:
            break

                
    return False,-1,-1
starttime = time.time()
start = [
        [2, 8, 3], 
        [1, 0, 4], 
        [7, 6, 9]
      ]
final =[
        [1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]
      ]
count=0
flag,k,distance = HillClimbing(start, final,count)
if(flag==True):
    print("Initial Stage :  ",start)
else:
    while flag==False:
        t=ran()
        if(t!=final):
            flag,k,distance=HillClimbing(t,final,count)
    print("Initial Stage : ",t)
print('Total No. of Iterations : ',k)
print("Distance : ")
print(distance)
end = time.time()
print("Time Taken : ",end - starttime)
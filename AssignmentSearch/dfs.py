import copy



def up(row,col,s):
    arrcopy=copy.deepcopy(s)
    if(row-1>=0):
        arrcopy[row][col]=arrcopy[row-1][col]
        arrcopy[row-1][col]=0
    return arrcopy

def down(row,col,s):
    arrcopy=copy.deepcopy(s)
    if(row+1<len(s)):
        arrcopy[row][col]=arrcopy[row+1][col]
        arrcopy[row+1][col]=0
    return arrcopy

def left(row,col,s):
    arrcopy=copy.deepcopy(s)
    if(col-1>=0):
        arrcopy[row][col]=arrcopy[row][col-1]
        arrcopy[row][col-1]=0
    return arrcopy

def right(row,col,s):
    arrcopy=copy.deepcopy(s)
    if(col+1<len(s[0])):
        arrcopy[row][col]=arrcopy[row][col+1]
        arrcopy[row][col+1]=0
    return arrcopy

def findIndex(x,s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]== x):
                return (i,j)

def check(s,newState):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]!=newState[i][j]):
                return False
    return True
            
def main():
#     s=[[1,2,3],[8,0,4],[7,6,5]]
#     g=[[2,8,1],[0,4,3],[7,6,5]]
    s=[[2,0,3],[1,8,4],[7,6,5]]
    g=[[1,2,3],[8,0,4],[7,6,5]]
    row,col=findIndex(0,s)
    print(row,col)
    
    print(k)
    stack = []
    visited = []
    stack.append(s)
#     print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    print(stack[0])
    count=0
    
    while(1):
#         print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        cur=stack[len(stack)-1]
        print(cur)
        stack.pop(len(stack)-1)
        
        if cur in visited:
            continue
        else:
            visited.append(cur)
        
        if cur==s and count!=0:
            continue
        count+=1
        
        row,col=findIndex(0,cur)
        
        #up
        newState=up(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print('Goal state is : ')
            print(newState)
            break
        if (newState not in visited):
            stack.append(newState)
            
        #down
        newState=down(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print('Goal state is : ')
            print(newState)
            break
        if (newState not in visited):
            stack.append(newState)
        
        
        
        #left
        newState=left(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print('Goal state is : ')
            print(newState)
            break
        if (newState not in visited):
            stack.append(newState)
            
        
        #right
        newState=right(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print('Goal state is : ')
            print(newState)
            break
        if (newState not in visited):
            stack.append(newState)
#     print(s)
#     print(g)
    print('Number of times code ran:')
    print(count)


if __name__=="__main__":
    main()

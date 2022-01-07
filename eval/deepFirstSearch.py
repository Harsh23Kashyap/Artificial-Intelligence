''' depth = 1'''
import copy

visit=[] 
lifo=[]

i=0
def child(curr,visit,sum_level,level):
    val1=[]
    if(sum_level<level):
        for j in range(len(curr)):
            if(len(curr[j])>0):
                p=copy.deepcopy(curr)
                val=curr[j][-1]
                p[j].pop(-1)
                k=0
                while(k<len(curr)):
                    p1=copy.deepcopy(curr)
                    p1[j].pop(-1)
                    if(k!=j):
                        p1[k].append(val)
                        if(p1 not in visit):
                            visit.append(p1)
                            val1.append(p1)
                    k+=1
    return val1

def solve(initial,goal,level):
    global lifo
    sum_level=0

    if(goal in  initial):
        visit.append(goal)
        return(visit)
    else:
        while(goal not in visit): 
            a=lifo.pop()
            x=child(a,visit,sum_level,level)
            if(goal in x):
                print("Found")
                break
            elif (len(x)==0):
                if(len(lifo)==0):
                    print("Not Found")
                    break
                sum_level-=1
            else:
                for i in x:
                    lifo.append(i)
                sum_level+=1

    
if __name__=="main":
    initial=[['B'],['A','C'],[]]
    goal1=[['A','B','C'],[],[]] 
    visit.append(initial)
    lifo.append(initial)      
    solve(initial,goal1,1)
    m=1
    for i in visit:
        print(m ,end='  ')    
        print(i)
        m=m+1
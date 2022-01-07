Solve the given 0/1  knapsack problem by considering the following points:NameWeightValue A453B405C508D9010Chromosome is a 4-bit string.–{xA xB xC xD}Population size = 4, Maximum Capacity of the bag(W)= 100.First two fittest chromosomes selected as it is.3rd and 4th fittest use for one-point crossover in the middle followed by single bit mutation of first offspring. Bits chosen 
#for mutation follows this cyclic order (xD, xC, xB, xA).Initial population: {1 1 1 1, 1 0 0 0, 1 0 1 0, 1 0 0 1}.Output the result after 10iterations.#
import numpy as np
def findWeight(cweight):
    cw=0
    for i in range (len(cweight)):
        if(cweight[i]==1):
            cw=cw+ weight[i]
    return cw

def findValue(cval):
    cv=0
    for i in range (len(cval)):
        if(cval[i]==1):
            cv=cv+ value[i]
    return cv

def leastFit(cycleVal):
    less= secondless= 100000000000
    for i in range(len(cycleVal)):
        if(cycleVal[i]<less):
            secondless=less
            less=cycleVal[i]
        elif (cycleVal[i]>less and cycleVal[i]<secondless):
            secondless=cycleVal[i]
    return less,secondless

def crossover(first,second):
    swap= [first[2], first[3]]
    first=[first[0], first[1], second[2],second[3]]
    second=[second[0],second[1],swap[0],swap[1]]
    return first,second

def passCycle(cycle):
    cycleweight=[0,0,0,0]
    cyclevalue=[0,0,0,0]
    mutation=3
    #check and assign weight
    for i in range (len(cycle)):
        cycleweight[i]=findWeight(cycle[i])
        if(cycleweight[i]>maxweight):
            cycle[i]=(np.random.randint(2, size=popsize)).tolist()
            i=i-1
        else:
            cyclevalue[i]=findValue(cycle[i])
    for i in range (10):
        r,c=leastFit(cyclevalue)
        cycle[r],cycle[c]=crossover(cycle[r],cycle[c])
        if(cycle[r][mutation]==1):
            cycle[r][mutation]=0
        else:
            cycle[r][mutation]=1
        mutation=mutation-1
        if(mutation==-1):
            mutation=3
        
        print("After "+str(i+1)+"th mutation : ")
        print(cycle)
    print("FINALLY")



if (__name__== "__main__"):
    weight=[45, 40, 50, 90]
    value=[3, 5 ,8, 10]
    maxweight=100
    popsize=4
    cycle=[[1 ,1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0 ,0, 1]]
    passCycle(cycle)
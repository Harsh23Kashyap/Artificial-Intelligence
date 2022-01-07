#Evaluation
import copy
import sys
import queue
from numpy import random            #importing random funcction
import time

if (__name__== "__main__"):
    start=time.time()
    print("\n2 SAT Problem")
    element=[1,1,1,1]   #[a,b,c,d]
    F = (not(element[0])or element[3])
    print(F)
    #SA(element)

    end=time.time()
    print("Total time = ",end-start)

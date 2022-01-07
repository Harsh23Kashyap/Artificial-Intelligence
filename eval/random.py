# Python3 code to demonstrate
# checking unique values in matrix
# set() + list comprehension

# initializing matrix
path=[[[2, 8, 1], [4, 6, 3], [7, 0, 5]], [[2, 8, 1], [4, 0, 3], [7, 6, 5]], [2, 8, 1], [0, 4, 3], [7, 6, 5]]                               [[2, 8, 1], [4, 6, 3], [7, 0, 5]]
for i in path:
                print(i)
                print("                 |   ")
                print("                 |   ")
                print("                \_/")

#fn to generate a new 3X3 matrix
def genState():
    #loop will run until a unique 3X3 matrix is generated
    while (True):
        x = random.randint(9, size=(3, 3))      #generation of 3X3 matrix
        res = list(set(i for j in x for i in j))            #will find all the unique value in the matrix x
        if (len(res)==9):   #(len(res)==len(x)*len(x[1])):          #if the number of unique element is 9, the no element is repeated hence break, if not repeat the procedure
            return x.toList()   ##convert the array generated to a list

  
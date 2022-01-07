
def moveup(i,j,list):
    num=list[i-1][j]
    list[i-1][j]=list[i][j]
    list[i][j]=num

def moveleft(i,j,list):
    num=list[i][j-1]
    list[i][j-1]=list[i][j]
    list[i][j]=num

def index(r,c,indexlist, index):
    for i in range(r):
        for j in range(c):
            if list[i][j]==index:
                return (i,j)

list=[[1,2,3],[4,1,6],[5,0,9]]
fi,fj=index(3,3,list,0)
print(list)

while (fi>0 or fj>0):
    if(fi>0):
        moveup(fi,fj,list)
        fi=fi-1
    if(fj>0):
        moveleft(fi,fj,list)
        fj=fj-1
    print(list)

print(list)

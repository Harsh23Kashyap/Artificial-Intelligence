
queue=[]
def enqueue(i):
    queue.append(i)

def dequeue():
    if (len(queue)>0):
        return queue.pop(0)


for i in range (5):
    enqueue(i)

print(queue)

while (len(queue)!=0):
    print(dequeue())
    print(queue)

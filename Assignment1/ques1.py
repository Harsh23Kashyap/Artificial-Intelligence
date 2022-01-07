#10 students
import array as arr
math=arr.array('i',[])
for i in range (10):
    num=int(input("Enter maths value : "))
    math.append(num)
print("Highest = ",max(math))
print("Lowest = ",min(math))
print("Average = ",sum(math)/len(math))




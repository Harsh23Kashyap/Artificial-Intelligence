#10 students
import array as arr
sal=int(input("Enter salary : "))
if (sal<=10000):
    print("HRA = ",0.2*sal)
    print("DA = ",0.8*sal)
elif (sal<=20000):
    print("HRA = ",0.25*sal)
    print("DA = ",0.9*sal)
else:
    print("HRA = ",0.3*sal)
    print("DA = ",0.95*sal)





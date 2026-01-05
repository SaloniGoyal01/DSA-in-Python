from array import *
arr = array('i', [])
x = int(input("Enter a number: "))
for i in range(0, x):
    y = arr.append(int(input("Enter next number: ")))
for j in arr:
    print(j, end=" ")
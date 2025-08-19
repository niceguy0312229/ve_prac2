# Clear the screen
import subprocess
import os
subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)



a = [ 1, 2, 3 ]
b = a
b[1] = 0 
print("For b = a command, it assign the same memory ID")
print(a, b) 
#print(f"ID_a =  {str(id(a))},id(b))
print(f"ID_a =  {id(a)}, ID_b = {id(b)}")
print("\n")

b = a.copy()                         # shallow copy
b[1] = 10 
print("Below is shallow copy example-----  ")
print(f"ID_a =  {id(a)}, ID_b = {id(b)}")
print(a, b)                           

a = [[1, 2], [3, 4], [5, 6]]
b = a.copy()                       


print(f"ID_a =  {id(a)}, ID_b = {id(b)}")
b[1][1] = 0
print(a)
print(b)
print("You need to do deep copy for sub  ==>  a and b id is different, but sub method is not applicable")
print("\n")

import copy
b = copy.deepcopy(a)
b[1][1] = 10 
print("below is the deep copy example")
print(f"ID_a =  {id(a)}, ID_b = {id(b)}")
print(a)
print(b)
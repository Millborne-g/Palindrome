#Millborne A. Galamiton BS CPE 2B
from math import *
def palindrome(value):
    size = len(value)
    res = size/2#divide it to 2 to get the values from the left side not including the middle value
    s = []#initialize a stack
    for i in range(len(value)):
        if i <floor(res):#if i is still below the middle value then the stack will continuously append the user input 
            s.append(value[i])            
        elif i > floor(res):#the i will skip the middle value to check the right side if it is equal to the left side
            temp =  s.pop()      
            if temp != value[i]:
                return False
                break            
    return True #return True if the both side left and right is equal                
 
          
stri = input("Enter a palindrome: ")#ask the user input
size = len(stri)#identify the size
if size % 2 != 0:#check the size if it is odd or not even number. if its odd then this will be executed
    if palindrome(stri) == True:#pass the value above then check if it is true
        print("Yes (a palindrome string) ",stri)
    else:
        print("No (not a palindrome string)")
else:print("Not qualified")#if it is an even number

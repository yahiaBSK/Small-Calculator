
#____________Progma:___________

def P(x,y):
    return x+y
    
def M(x,y):
    return y-x
    
def F(x,y):
    return y*x

def O(x,y):
    return x/y

def O2(x,y):
    return y/x
      



print ("THIS IS SMALL & SIMPLE CALCULATOR , WELCOM  :) ")
print ("")
print ("")
p = input ("click  OK  to continue .....")
if p == p:
    print ("")
    print ("")
import os
os.system('cls' if os.name == 'nt' else 'clear')
    
print ("1 - ADD (+) ")
print ("2 – MOIN (-) ")
print ("3 - FOIX (×) ")
print ("4 – ON (÷) ")
print ("")
print ("")
print ("(enter sujt the num (1 / 2 / 3 / 4)")
print ("")
print ("")
c = input ("CHOOSE YOUR CLCULATION TYPE : ")
print ("")
num1 = int (input("ENTER YOUR FIRST NUM [X] : "))
num2 = int (input("ENTER YOUR SECOND NUM [Y] : "))
if c == "1":
    print (num1, "+", num2, "=", P(num1,num2))
elif c == "2":
    print (num1, "-", num2, "=", M(num1,num2))
elif c == "3":
    print (num1, "×", num2, "=", F(num1,num2))
elif c == "4":
    if num1 > num2:
        print (num1, "÷", num2, "=", O(num1,num2))
    elif num1 < num2:
        print("")
        print ("You Can't Solve :", num1,"÷", num2, "So Your Solve Is : ")
        print("")
        print (num2, "÷", num1, "=", O2(num1,num2))
    
else :
    print("")
    print ("ERROR IN STYLE NUM !!")
    
OO=input("DO YOU WANT TO RESTART THE PGM ? .... ()")
if OO==OO:
    import os
    os.system('')
    
    
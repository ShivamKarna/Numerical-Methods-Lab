# 28 Jestha, Thursday
import numpy as np


try:
    num = float(input("Enter a number : "))
except ValueError:
    print("Enter Float Number Please! ")
    exit(0)

choice  = input("Enter your choice between -> (ln,sin,cos,tan) : ")
choiceDict = ('ln','sin','cos','tan')

if choice not in choiceDict:
    print("Please choose between -> (ln, sin, cos, tan)")

try:
    if (choice == "ln"):
        if(num <=0):
            raise RuntimeError("Invalid Input, Can't Calculate Log 0 or negative values in Log.")
        ln = np.log(num)
        print(ln)
    elif( choice == "sin"):
        sin = np.sin(num)
        print(sin)
    elif(choice == "cos"):
        cos = np.cos(num)
        print(cos)
    elif(choice == "tan"):
        tan = np.tan(num)
        print(tan)
except ValueError:
    print("Enter float only")
except RuntimeError as e:
    print(f"Error : {e}")
except Exception:
    print("Please enter valid choice")

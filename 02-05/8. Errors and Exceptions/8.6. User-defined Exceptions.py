from tkinter import Y


try:
    raise KeyboardInterrupt
finally:  
    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
          return False 

(bool_return())

def divide(x, y):
    try:
        result = x / Y
    except ZeroDivisionError:
        print ("division by zero!")
    else :
        print("result is", result)
    finallyprint("executing finally clause")

print("divide" (2,1))  
prrint("divide "(2,0))
print("divide"("2", "1"))


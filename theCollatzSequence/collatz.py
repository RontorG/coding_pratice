""" 
Exercise from "automate the boring stuff with python"
https://automatetheboringstuff.com/2e/chapter3/
"""
def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
    elif number % 2 == 1:
        value = 3 * number + 1
        print(value) 
    return value
    

def valid(intNum, txt=""):
    print(txt)
    while True: 
        try:
            n = int(input(intNum))
            break
        except ValueError:
            print("Only integer values allowed")
    return n


print("The simplest impossible problem")
num = valid("enter a integer") 
v = num

while True:
    v = collatz(v)
    if v == 1:
        break
    


"""
Exercise from "automate the boring stuff with python"
https://automatetheboringstuff.com/2e/chapter4/
"""

def pretty(data):
    if len(data) == 0:
        print("nothing to do here")
    elif len(data) == 1:
        print(data[0])
    else:
        for item in data:
            print(item, end="")
            if item == data[-2]:
                print(end=" and ")
            elif item == data[-1]:
                print("")
            else:
                print(end=", ")


span = ['apples', 'bananas', 'tofu', 'cats']
#span = ['trigo']

pretty(span)

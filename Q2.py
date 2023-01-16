# Create a function to division by provided argos: [[1, 0], [1, 2], [6, 3], [1, “a”] handle with specific errors

def checkifdivides(a,b):
    try:
        res= a/b
        print(f"Division successful between {a} and {b} = {res}\n")
    except ZeroDivisionError as e1:
        print(f"Please do not try to divide {a} by zero!\n")
    except TypeError as e2:
        print(f"Please ensure that the data types of inputs '{a}' and '{b}' are same\n")        
        
        
testList = [[1, 0], [1, 2], [6, 3], [1, "a"]]

for row in testList:
    checkifdivides(row[0],row[1])
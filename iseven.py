"""
Function that returns whether the no is even or not.
"""
def iseven(no:int) -> bool:
    return no %2 == 0

print(iseven(123))
 
def isodd(no:int) -> bool:
    return not iseven(no)

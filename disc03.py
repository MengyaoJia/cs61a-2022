def merge(n1,n2):
""" Merges two numbers by digit in decreasing order
>>> merge(31, 42)
4321
>>> merge(21, 0)
21
>>> merge (21, 31)
3211
"""
#noticable point: each argument is in a decreasing order as well
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    elif n1 % 10 > n2 %10:
        #*10 is fabulouss
        return merge(n1,n2//10)*10 + n2%10
    else:
        return merge(n1//10,n2)*10 + n1%10

print(merge(31,42))

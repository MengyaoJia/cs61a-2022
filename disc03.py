def hailstone(n):
"""Print out the hailstone sequence starting at n, and return
the number of elements in the sequence.
>>> a = hailstone(10)
10
5
16
8
4
2
1
>>> a
7
>>> b = hailstone(1)
1
>>> b
1
"""
    count = 1
    if n == 0:
        return count
    else:
        if n%2 == 0:
            #int can only be used at str
            print(int(n))
            #steps counting
            count += hailstone(n/2)
        else:
            print(int(n))
            count += hailstong(n*3+1)
    return count



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

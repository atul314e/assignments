import time
import math

def printFirstHalf(num, zero_to_append):
    '''
        row is \n
        4 2 | 3 3 3 3 3 3 | 2 4\n
        pre = [4, 2]\n
        lst = [3, 3, 3, 3, 3]\n
        post = reverse of pre\n
    '''
    matrix=[] # it will contain list of all rows of pattern
    # prints the first half of pattern
    for turn in range(num):
        pre=[]
        lst=[]
        n=num
        val=num-turn

        while n>val:
            if math.floor(math.log10(n))<zero_to_append:
                pre.append('0'*zero_to_append+str(n))
            else:
                pre.append(str(n))
            n-=1
        
        VAL=math.floor(math.log10(val)) # no of digits in val

        # filling the list lst
        for N in range(val+(val-1)):
            if VAL<zero_to_append:
                lst.append('0'*zero_to_append+str(val))
            else:
                lst.append(str(val))
        
        if len(pre)!=0:
            post=pre.copy()
            post.reverse()
            pre.extend(lst)
            pre.extend(post)
            matrix.append(pre)
            string=" ".join(pre)
            print(string)
        else:
            matrix.append(lst)
            string=" ".join(lst)
            print(string)
    return matrix


def printSecondHalf(matrix):
    size=len(matrix)
    index=size-12
    # prints the second half of pattern
    while index>=0:
        string=" ".join(matrix[index])
        print(string)
        index-=1

def printPrettyMatrix():
    '''
    pretty matrix print pattern given a number n as-\n
    n  n   n   n  ...   n    n   n\n
    n n-1 n-1 n-1 ...   n-1 n-1  n\n
    n n-1 n-2 n-2 ...   n-2 n-1  n\n
    ..............................\n
    ..............................\n
    n n-1 n-2 ... 1 ... n-1 n-2  n\n
    ..............................\n
    ..............................\n
    n n-1 n-2 n-2 ...   n-2 n-1  n\n
    n n-1 n-1 n-1 ...   n-1 n-1  n\n
    n  n   n   n  ...    n   n   n\n
    \n
    ----------------- first this half generated\n
    ###########\n
    4444444\n
    4333334\n
    4322234\n
    ###########\n
    4321234\n
    ---------------- second half generated using part inside #####\n
    4322234\n
    4333334\n
    4444444\n
    '''
    num=int(input("Enter number >> "))

    zero_to_append=math.log10(num) 
    zero_to_append=math.floor(zero_to_append) 
    matrix=printFirstHalf(num, zero_to_append)
    printSecondHalf(matrix)

start=time.time()
printPrettyMatrix()
end=time.time()

print("time of printing pattern in ms-- ", (end-start)*10**3)
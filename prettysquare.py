import time
import math

def printFirstHalf(num):
    '''
        row is \n
        4 3 | 2 2 2  | 3 4\n
        pre = [4, 3]\n
        lst = [2,2,2]\n
        post = reverse of pre\n
    '''
    total_digits=math.floor(math.log10(num))+1 # total digits
    matrix=[] # it will contain list of all rows of pattern
    # prints the first half of pattern
    for turn in range(num):
        pre=[]
        lst=[]
        n=num
        val=num-turn

        while n>val:
            num_of_digits=math.floor(math.log10(n))+1 # number of digits of current number
            zeroes_to_append=total_digits-num_of_digits
            pre.append('0'*zeroes_to_append+str(n))
            n-=1
        
        VAL=math.floor(math.log10(val))+1 # no of digits in val
        zeroes_to_append=total_digits-VAL
        # filling the list lst
        for N in range(val+(val-1)):
            lst.append('0'*zeroes_to_append+str(val))
        
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
    index=size-2
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

    matrix=printFirstHalf(num)
    printSecondHalf(matrix)

start=time.time()
printPrettyMatrix()
end=time.time()

print("time of printing pattern in ms-- ", (end-start)*10**3)
import random

def sublistsum(numlist=[]):    
    if len(numlist)==0:
        numlist=[random.randint(1, 10) for iter in range(10)]
    S=int(input("Enter the number >> "))    
    left=0
    right=0
    sum=0
    sum+=numlist[left]

    while(1):
        if right>len(numlist)-1:
            break
        elif sum>S:
            #print(sum)
            sum-=numlist[left]
            left+=1
        elif sum==S:
            break
        elif sum<S:
            right+=1
            if right<=len(numlist)-1:
                sum+=numlist[right]   

    #print(sum, left, right)
    if right>len(numlist)-1:
        print("[]")
    else:
        print(numlist)
        print("------------- ")
        sublist=[]
        while left<=right:
            sublist.append(numlist[left])
            left+=1
        print(sublist)

sublistsum()
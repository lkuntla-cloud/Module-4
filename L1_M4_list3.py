L=[1,4,3,2,5,9,6,7,8]
count=0
for i in L:
    count+=i
print("the sum is: ",count)
avg=count/len(L)
print("The average is: ",avg)
L.sort()
print(L)
print("The smallest number in the list is: ",L[0])
print("The greatest number in the list is: ",L[-1])



numbers1=[1,2,3]
numbers2=[2,4,5]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("The result is: ",list(result))

numbers=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,numbers))
print("The square value if the numbers is: ",square)
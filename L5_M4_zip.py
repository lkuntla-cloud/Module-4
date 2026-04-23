s1={2,3,1}
s2={"b","a","c"}
s3=list(zip(s1,s2))
print(s3)

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
    
stocks={"reliance","infosys","tcs"}
prices={1275,1345,1453}
new_dict={x: y for x,y in zip (stocks,prices)}
print(new_dict)
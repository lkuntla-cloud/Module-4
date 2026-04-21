def multiply_tuples(numbers):
    ans=1
    for num in numbers:
        ans*=num
    return ans
tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
result1=multiply_tuples(tup1)
result2=multiply_tuples(tup2)
print("The result of tuple 1 was: ",result1)
print("The result of tuple 2 was: ",result2)
print("odd numbers in list")
input1=int(input("Enter a number: "))
odd_numbers=[x for x in range(input1) if x%2!=0]
print("The odd numbers in",input1," are: ",odd_numbers)
for i in range(50):
    print("_",end="")
print()
print("capitalize fruits")
fruits=["banana","apple","mango","grapefruit","kiwi"]
capitalized_fruits=[fruit.capitalize() for fruit in fruits]
print("The original fruits are: ",fruits)
print("The capitalized fruits are: ",capitalized_fruits)
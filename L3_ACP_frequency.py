test_dict={"Codingal":3,"is":2,"best":2,"for":2,"coding":1}
print("The test dictionary is: ",test_dict)
check=int(input("Enter the value you want to check the frequency of: "))
fre=0
for value in test_dict.values():
    if value==check:
     fre+=1
print("The frequency is: ",fre)
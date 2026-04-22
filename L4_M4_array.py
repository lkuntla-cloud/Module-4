import array as arr
array_num=arr.array("i",[1,2,3,4,5,3,3])
print("original array: "+str(array_num))
print("number of occurences of number 3 in array: "+str(array_num.count(3)))
array_num.reverse()
print("The reversed array is: "+str(array_num))
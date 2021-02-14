#Write a Python program to get the smallest number from a list.


list1 = [10, 20, 4, 45, 99]
 

list1.sort()
 
print("Smallest element is:", *list1[:1])
print("The Count of even and odd in the given list is : ")
print()

lst = [1,2,3,4,5,6,7,8,9]
 
even_count = 0
odd_count = 0
 
for num in lst:
     
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
         
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)






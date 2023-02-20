#Write a Python program to count the number of even and odd numbers from a series of numbers.



#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

#$Expected Output :

#Number of even numbers : 4

#Number of odd numbers : 5
number_list = (1,2,3,4,5,6,7,8,9)
even_count , odd_count = 0 , 0
for a in number_list :
    if a % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1
print("even_count in number_list :", even_count)
print("odd_count in number_list :" , odd_count)
    
    

#1."Write a function named multiplication that accepts a list of integers and prints
#  the result of multiplying all of them.
#  Eg given [1,2,3,4] it returns 24 

#To create a function in python you use def 
def multiplication (numbers):
    # multiplication starts with 1 as the number as the number is going to multiply by itself
    result = 1 
    # for loop
    for number in numbers:
        # multiply the number in numbers with the result
        result *= number
        print(result)

# You have to call the function
multiplication([1,2,3,4,5])


#2. Write a function named addition that accepts a list of integers and returns the 
# result of adding all of them. Eg given [1,2,3,4] it returns 10

def addition (numbers):
    result = 1
    for num in numbers:
        result += num
        return(result)

addition([1,2,3,4])


#3 You are given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, what is the result of their 
#union 
#set1.union(set2) results in {1, 2, 3, 4, 5, 6}
#intersection
#set1.intersection(set2) results in {3, 4}
#difference
#set1.difference(set2) results in {1, 2}

set1={1,2,3,4}
set2= {3,4,5,6}

#union

print(set1.union(set2))

#intersection

print(set1.intersection(set2))

#Difference

print(set1.difference(set2))

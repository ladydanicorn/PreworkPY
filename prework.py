#Question 1
#Write a function to print "hello_USERNAME!"

def hello_name(user_name):
    print("hello_"+user_name)
user_name = input("Enter username: ")
hello_name(user_name)

#Question 2
#Write a python function, first_odds that prints 
#the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
first_odds()

#Question 3
#Please write a Python function, max_num_in_list 
#to return the max number of a given list. 

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
#print(max_num_in_list([4, 2, 7, 0]))

#Question 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
a_year = int(input("What year is it: "))
print(is_leap_year(a_year))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.
    
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1,3,4]
print(is_consecutive(a_list))

from math import floor
import math
from math import factorial
from persiantools.jdatetime import JalaliDateTime
import datetime, pytz
from datetime import datetime 
import pprint
from typing import List,Dict , Union
import time



# students = []
# first_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# first_student["name"] = fname
# first_student["Last name"] = lname
# first_student["Birth_year"]= birth_year
# first_student["average"]= average

# students.append(first_student)



# second_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# second_student["name"] = fname
# second_student["Last name"] = lname
# second_student["Birth_year"]= birth_year
# second_student["average"]= average

# students.append(second_student)
# print(second_student["name"] + second_student ["Last name"])

# third_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# third_student["name"] = fname
# third_student["Last name"] = lname
# third_student["Birth_year"]= birth_year
# third_student["average"]= average

# students.append(third_student)
# print(third_student["name"] + third_student ["Last name"])


# pprint.pprint(students)

# # upper() and  " "
# uperName = students[0]
# first_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(first_upeper_name.upper())

# uperName = students[1]
# second_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(second_upeper_name.upper())

# uperName = students[2]
# third_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(third_upeper_name.upper())


# # average 
# mark = students[0]
# first_mark = mark["average"]

# mark = students[1]
# second_mark = mark["average"]

# mark = students[2]
# third_mark = mark["average"]


# average_of_three = (first_mark + second_mark + third_mark)/3 
# print(floor(average_of_three))



# with while and for :
# students = []
# index = 0
# average = 0
# for i in range(3):

#     first_name = input("what's your name?")
#     last_name = input("what's your last name?")
#     birth_year = int(input("tell me about your birth yaer"))
#     gpa = float(input("what is your GPA" ))

#     student= {
#         "name" : first_name ,
#         "family" : last_name , 
#         "birth_year" : birth_year ,
#         "gpa" : gpa
#     }

#     students.append(student)

# while index < 3 :
#         id = students[index]["name"] + " " + students[index]["family"]
#         gpa_of_three = students[index]["gpa"]
#         average = average + gpa_of_three
#         index += 1
#         pprint.pprint(id.upper())
#         print(average)

# pprint.pprint(students)
# print(average / len(students))


# Binary search 
start_time = time.time()
numbers = [1 , 3 ,5 , 7 , 9]
num = int(input("say a odd nubmber between 0 to 9  "))

def binary_search(x) :
    left = 0
    right = len(numbers)-1
    while left <= right :
        mid = (left + right)//2
        if numbers[mid] == num :
            print("eyval ine")
            return
        elif numbers[mid] < num:
            left = mid +1
        else: 
            right = mid -1

    return "not found"
result = binary_search(num)
print(result)


# # سوال:
# فرض کن یک لیست مرتب شده به نام numbers دارید:

# python
# Copy code
# numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# یک عدد target می‌دهیم که در این لیست جستجو شود. کد باینری سرچ را بنویسید که بگوید آیا عدد target در لیست وجود دارد یا خیر و اگر موجود بود، اندیس آن را چاپ کند.

# ورودی: عدد target (مثلاً 12)

# خروجی:

# اگر عدد موجود بود: "Found at index X"
# # اگر عدد موجود نبود: "Not found" 


numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

num = int(input("Enter an even number between 0 to 20 ? "+"\n"))

def search(num):
    left = 0
    right =len(numbers)-1
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == num:
            print(num , " is here")
            return
        elif numbers[mid] < num :
            left = mid + 1
        else:
            right = mid - 1
    
    print("peyda nashod")
    return

javab = search(num)
end_time = time.time()
ex_time = start_time - end_time
print(javab)
print(f"the time is {ex_time} seconds")


# یک تابع بنویس که nامین عدد فیبوناچی را محاسبه کند. دنباله فیبوناچی به این صورت است:

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) برای n > 1
# تابع شما باید برای هر عدد n که وارد می‌شود، nامین عدد فیبوناچی را محاسبه کند.
fibonacci = [ ]


def fibonacci(n):
    if n < 1 :
        print("stop")
    while n > 1:
       f = (n-1) + (n -2 )
       if fibonacci[-1] < 100 :
         n = int(input("a number"))





from math import floor
import math
from persiantools.jdatetime import JalaliDateTime
import datetime, pytz
from datetime import datetime 
import pprint
from typing import List,Dict , Union



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



students : List[Dict[str , Union[str , int , float]]] = []

i: int = int(input("how many students there are?"))




for n in range(i)  :

    first_name: str = input("First name : " ).capitalize()
    last_name: str = input("Last name : " ).capitalize()
    birth_year: int = int(input("birth year : " ) )
    grade: float = float(input("Average : " ) )
    students.append({

        "first name" : first_name ,
        "last name" : last_name ,
        "birth year" : birth_year ,
        "grade" : grade
    })
    i += 1

def upper_name(x:Dict[str , Union[str , int , float]]):
    """
    take first name and last name and 
    convert it to uppercase 
    """
    
    for student in students:
       full_name = f"{student['first name']} {student['last name']}"
       print(full_name.upper())

def age(age:Dict[str , Union[str , int , float]])->Dict[str , Union[str , int , float]]:
    """
    calculate the ages
    """
    birthdate = JalaliDateTime.now().year
    
    for student in students:
        age = birthdate - student["birth year"]
        print( age)
        
def average(gpa:Dict[str , Union[str , int , float]]):
    """
    calculate GPA
    """
    grade = 0
    for student in students:
        grade = grade + student["grade"]

    print(grade/len(students))

upper_name(students)
age(students)
average(students)

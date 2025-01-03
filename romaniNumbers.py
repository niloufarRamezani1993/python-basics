roman_nums = ["C" , "XC","LXXX", "LXX" , "LX" , "L", "XL" , "X" , "IX" , "V" , "IV" , "I" ]
norm_num =[100 , 90 , 80 , 70 , 60 , 50 , 40 , 10 , 9 , 5 , 4 , 1 ]

num = int(input("Enter a number to convert" + "\n"))


def romani_number(n):
    romans= ""
    index = 0
    while 0 < n :
        for _ in range(n // norm_num[index]):
           romans = romans + roman_nums[index]
           n = n - norm_num[index]
        index += 1
    return romans
    

print(romani_number(num))
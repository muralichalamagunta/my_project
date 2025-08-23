# import copy

# old_list = [[1,2,3], [4,5,6]]
# new_list = copy.copy(old_list)

# new_list[0][2] = 99

# print("Old_list:", old_list)
# print("New_list:", new_list)


# old_list = [[1,2,3], [4,5,6]]
# news_list = copy.deepcopy(old_list)

# news_list[0][2] = 99

# print("Old_list:", old_list)
# print("News_list:", news_list)

# print("If Else")


# n = int(input("Enter n"))
# if n > 0:
#     print("Zero")
# else:  
#     print("Not a zero")    

# nums = -1

# if nums >= 5:
#     print("T")
# else:
#     print("F")

# num = 6

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# list = [1,2,3,4,5,6,7,8,9,10]  

# for num in list:
#     if num % 2 == 0:
#         print(num, end= " ")


# a = int(input("Enter a value"))
# b = int(input("Enter b value"))  

# if a > b :
#     print(" A is greater")
# else:
#     print("B is greater") 

# num = 78

# if num >=0 and num <=50:
#     print("T")
# else:
#     print("F")

# a = int(input("Enter value"))

# if a % 2 == 0:
#     print("T") 
# else:
#     print("F")

# a = 17

# if a >= 18:
#     print("T")
# else:
#     print("F") 

# num = int(input("Enter a number:"))
# if num % 5 ==0:
#     print("T")
# else:
#     print("F")

# print("If elif else")

# num = 5

# if num > 10:
#     print("Y")
# elif num == 10:
#     print("N")
# else :
#     print("K")  

# marks = 49

# if marks >= 90:
#     print("Pass")
# elif marks >=70:
#     print("Just pass")
# elif marks >=50:
#     print("Pass")
# else:
#     print("D")

# user = int(input("Enter marks"))

# if user >= 90:
#     print("Grade A")
# elif user >= 70:
#     print("Grade B")
# elif user >= 50:
#     print("Grade C")
# else:
#     print('fail')

# user = int(input("Enter marks"))

# if user > 0:
#     print("Positive")
# elif user == 0:
#     print("Zero")
# else: 
#     print("Negative")

# a = int(input("Enter a value"))
# b = int(input("Enter b value"))

# operater = "-"

# if operater == "+":
#     print("Adding", a+b)
# elif operater == "-":
#     print("sub", a-b)
# elif operater == "%":
#     print("div", a%b)
# else:
#     print("Multi", a*b)


# age = 13

# if age < 13:
#     print("Child")
# elif age >=13 and  age <=19:
#     print("Teenager")
# elif age >=20 and age <=59:
#     print("Adult")
# else:
#     print("Senior")

# for i in range(1,21):
#     print(i, end = ",")

# fruits = ["Apple", "Banana", "cherry"]

# for fruit in fruits:
#     print("I like", fruit)

# for char in "hello":
#     print(char, end = " ")

# total = 0
# for i in range(3,11):
#     total += i
# print(total)

# count = 0
# for i in range(1,10): 
#     count += i
# print(count)

# for i in range(1,11):
#     print(i)

# for i in range(1,11):
#     print(i)

# word = "python"
# for char in word:
#     print(char)

# for i in range(1,20):
#     if i % 2 == 0:
#         print(i)
count = 0
for i in range(1,50):
    count += i
print(count)

string = "hello"
print(string[::-1])
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)



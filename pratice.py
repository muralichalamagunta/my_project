print("Start")

# num = int(input("Enter value : "))

# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# text = "murali krishna"   
# vowels = "aeiou"

# count = 0
# for char in text:
#     if char in vowels:
#         count = count + 1
# print(count)  

# list = [1, 2, 3, 4]
# total = 0
# for num in list:
#     total = total + num
# print(total)

# num = int(input("Enter valua : "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num *i)


# list = [11, 24 ,86, 99]
# largest = list[0]

# for num in list:
#     if num > largest:
#         largest = num
# print(largest)

# string = "murali"
# reversed_string = ""

# for char in string:
#     reversed_string = char + reversed_string
# print(reversed_string)

# num = int(input("Enter valua : "))
# factorial = 1

# for i in range(1, num + 1):
#     factorial = factorial * i
# print(factorial)

# list = [1, 1, 2, 3, 3, 4, 5]
# empty_list = []
# for item in list:
#     if item not in empty_list:
#         empty_list.append(item)
# print(empty_list)

# string = "mmuurrali"
# empty_string = ""

# for char in string:
#     if char not in empty_string:
#         empty_string = empty_string + char
# print(empty_string)

text = "murali puspha miukitfd"
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
# print(count)
# for char in count:
#     if count[char] > 2:
#         print(char, "=", count[char])

# for char in count:
#     if count[char] < 2:
#         print(char, "=", count[char])

for char in count:
    if char == "u" :
        print(char, "=", count[char]) 
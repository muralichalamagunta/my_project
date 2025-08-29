# class person:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello, I am {self.name}")   
# p = person("John")   
# p.greet() 

# class person:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello, I am {self.name}")
# p = person("John")
# p.greet()

# class animal():
#     def sound(self):
#         print("Same sound")
# class dog(animal):
#     def sound(self):
#         print("Dog barking")

# a = animal()
# a.sound()        
# d = dog()        
# d.sound() 

# class animal():
#     def sound(self):
#         print("Same sound") 
# class dog(animal):
#     def sound(self):
#         print('Dog barking')        
# # a = animal()
# # a.sound()
# b = dog()
# b.sound()

# import psycopg2

# try:
#     conn = psycopg2.connect(
#         host="",
#         database="",
#         username="",
#         password="",
#         port=""
#     )
#     cursor = conn.cursor()
#     print("Connection succesfull")

# except Exception as e:
#     print("Error:", e)  
# finally:
#     if cursor in locals:
#         cursor.close()
#     if conn in locals:
#         conn.close() 

# import psycopg2

# try:
#     conn = psycopg2.connect(
#         host="",
#         username="",
#         password="",
#         database="",
#         port=""
#     )

#     cursor = conn.cursor()
#     print("Connection successfull")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if cursor:
#         cursor.close()

#     if conn:
#         conn.close()



# my_list = [10,20,30,40]
# print(my_list)
# print(len(my_list))
# print(my_list[::-1])
# for item in my_list:
#     print(*my_list)
# my_list1 = [1, 5, 6, 3, 8, 9]
# for num in my_list1:
#     if num % 2 == 0:
#         print(num)

# my_list = [10,20,30,40]
# print(my_list)
# print(*my_list)
# for item in my_list:
#     print(item)


# my_list1 = [1, 5, 6, 3, 8, 9]
# for num in my_list1:
#     if num % 2 == 0:
#         print(num, end=" ")
# for num in my_list1:
#     if num % 2 != 0:
#         print(num, end = " ")

# my_list2 = [1, 3, 2, 4, 6, 8, 9]     
# evens = [x for x in my_list2 if x % 2 == 0] 
# odds = [num for num in my_list2 if num % 2 != 0]  

# print("Even numbers:", evens)
# print("Odd numbers:", odds) 

# mylist = [1, -2, 8, -9, 5, 5, -7, 7, 2]
# print(list(set(mylist)))
# print(sorted(set(mylist)))
# print(sorted(set(mylist), reverse=True))

# mylist1 = [1, -3, 4, 2, 5, -7, 3, -4, 2]
# final_list = []
# for item in mylist1:
#     if item not in final_list:
#         final_list.append(item)
# print(final_list)
# print(set(final_list))
# print(sorted(set(final_list)))
# print(sorted(set(final_list), reverse=True))
 
# mylist1 = [1, 3, 4, 2, 5, 7, 3, 4, 2]
# mylist2 = [1, 3, 5, 2, 5, 6, 7, 8, 8]
# final_list = []
# for item in mylist1:
#     if item in mylist2 and item not in final_list:
#         final_list.append(item)
# print(final_list)


# def count_up_to(n):
#     count = 1
#     while count <=n:
#         yield count
#         count += 1
# for num in count_up_to(5):
#     print(num)        

# string = "hello123"
# letters = ""
# numbers = ""
# for char in string:
#     if char.isdigit():
#         numbers += char
#     else:
#         letters += char
# reversed_letters = ""
# for char in letters:
#     reversed_letters = char + reversed_letters
# result =  reversed_letters + numbers
# print(result)
# reversed_numbers = ""
# for char in numbers:
#     reversed_numbers = char + reversed_numbers
# result = letters +  reversed_numbers
# print(result)           

# string = "hello123"
# letters = ""
# numbers = ""
# for char in string:
#     if char.isdigit():
#         numbers += char
#     else:
#         letters += char 
# reversed_letters = ""
# for char in letters:
#     reversed_letters = char + reversed_letters
# result = reversed_letters + numbers
# print(result)     

# reversed_numbers = ""
# for char in numbers:
#     reversed_numbers = char + reversed_numbers
# result = letters + reversed_numbers
# print(result)

str = "mississippi"
letter_count = {}
for letter in str:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
max_count = max(letter_count.values())
for letter, count in letter_count.items():
    if count == 1:
        print(f"{letter} : {count}")

      

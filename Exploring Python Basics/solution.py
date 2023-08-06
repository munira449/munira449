#Task 1: variable manipulation
def task1():
 
 name = "Munira Huda"
 age = 27
 print("My name is " + name + " and i am " + str(age) + " years old")

task1()


#Task 2: Data Types and Type Conversion
def task2():
 
 num1 = 10
 num2 = 11.0
 num1_float = float(num1)
 num2_int = int(num2)
 print("num1:" + str(num1))
 print("num1_float:" + str(num1_float))
 print("num2:" + str(num2)) 
 print("num2_int" + str(num2_int))

task2()

#Task 3: String Manipulation
def task3():

 sentence = "Python programming is fun!"
 print("Length of the string:", len(sentence))
 print("8th character:", sentence[7])
 substring = sentence[0:6]
 result = substring + " I enjoy it!"
 print(result)

task3()

#Task 4: Lists and List Manipulation
def task4():

 list = ["apple" , "banana", "cherry", "date"]
 print(list)
 list.append("grape")
 print(" Add grape " + str(list))
 list.remove("banana")
 print(" after removing banana list is: " + str(list))
 print("the length of the list: " + str (len(list)))
 sliced_fruits = (list[1:3])
 print("sliced_fruits: " + str(sliced_fruits))
 extra_fruits = ["kiwi" , "lemon"]
 combined_fruits = str(sliced_fruits) + str(extra_fruits)
 print("combinrd list: " + str(combined_fruits))

task4()

#Task 5: Conditional Statements
def task5():

  num = 42
  if num % 2 == 0:
     print(f"{num} is even.")
  else:
     print(f"{num} is odd.")

task5()

#Task 6: Loops
def task6():

 for num in range(1,11):
     print(num)
     sum = 0
 for num in range(1,101):
     sum = sum + num
     print(num)

task6()

#Task 7: Functions

def calculate_square(num):
    return num ** 2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = 7
square_of_number = calculate_square(number)
print("Square of", number, "is:", square_of_number)
number2 = 29
if is_prime(number2):
    print(number2, "is a prime number.")
else:
    print(number2, "is not a prime number.")

   


#Task 8: Dictionaries
def task8():

 student = {"name": "Munira Huda","age": 27,"grade": "A"}
 student["course"] = "Computer Science"
 print("Keys in the dictionary:")
 for key in student.keys():
     print(key)
 print("\nKey-Value pairs:")
 for key, value in student.items():
     print(f"{key}: {value}")

task8()





    


import random
# Part A Conditions

 
# A.1 
number = float(input("Enter a number:"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

    
# A.2
age = int(input("Enter your age:"))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")
 
    
# A.3
stored_username = "admin"
stored_password = "1234"
 
entered_username = input("Enter username:")
entered_password = input("Enter password:")
 
if entered_username == stored_username and entered_password == stored_password:
    print("Match")
else:
    print("Aww..too bad")

    
# A.4
score = float(input("Enter your score from 0-100:"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

    
# A.5
order_total = float(input("Enter order total: "))
is_member = input("Are you a member? (yes/no): ") == "yes"
 
if order_total >= 500 or is_member:
    print("\nFree shipping")
else:
    print("\nShipping cost: 50")
 
    
# A.6
print(5 == 5)   # True
print(5 != 3)   # True
print(7 > 10)   # False
print(2 < 9)    # True
print(6 >= 6)   # True

 
# Part B - Truthy, falsy and membership


# B.1
empty_string = ""
non_empty_string = "hello"
zero = 0
non_zero = 42
empty_list = []
non_empty_list = [1, 2, 3]

if empty_string:
    print("empty string is truthy")
else:
    print("empty string is falsy")
 
if non_empty_string:
    print("non-empty string is truthy")
else:
    print("non-empty string is falsy")
 
if zero:
    print("zero is truthy")
else:
    print("zero is falsy")
 
if non_zero:
    print("non-zero is truthy")
else:
    print("non-zero is falsy")
 
if empty_list:
    print("empty list is truthy")
else:
    print("empty list is falsy")
 
if non_empty_list:
    print("non-empty list is truthy")
else:
    print("non-empty list is falsy")

    
# B.2 
supported_languages = ["Python", "Java", "C++", "JavaScript"]
language = input("Enter a programming language:")
 
if language in supported_languages:
    print("\n",language,"is supported")
else:
    print("\n",language, "is not supported")

    
# B.3 


blocked_usernames = ["max", "root", "test", "guest"]
username = input("Choose a username:")

if username in blocked_usernames:
    print("\nAww..too bad, not today.")
else:
    print("\nUsername accepted")
 
    
# B.4 


logged_in = False
has_permission = False
 
if not logged_in:
    print("You must log in first")
 
if not has_permission:
    print("You do not have permission to access this page")

 
# Part C - For loops


# C.1


names = ["Alice", "Bob", "Emma", "Bobby"]
for i in range(len(names)):
    print("\nHej", names[i])
    i +=1
 
    
# C.2
for number in range(1, 51):
    if number % 2 == 0:
        print(number)

        
# C.3
numbers_list = [10, 20, 30, 40, 50]
total = 0
for n in numbers_list:
    total += n
print("Sum:", total)


# C.4 
values = [23, 67, 12, 89, 45, 3]
largest = values[0]
for v in values:
    if v > largest:
        largest = v
print("Largest:", largest)


# C.5 
words = ["cat", "elephant", "dog", "bidy", "ox", "butterfly"]
count = 0
for word in words:
    if len(word) > 5:
        count += 1
print("Words longer than 5 characters:", count)


# C.6 


scores = [55, 82, 70, 45, 91, 68, 77]
passes = 0
failures = 0
for s in scores:
    if s >= 70:
        passes += 1
    else:
        failures += 1
print("\nPasses:", passes,"Failures:", failures)
 

# C.7
student_grades = {"Max": 85, "Sam": 92, "Venus": 78}
 
for key in student_grades:
    print(key)
 
for value in student_grades.values():
    print(value)
 
for key, value in student_grades.items():
    print("\nShow",key, "-", value)

# Part D Ranger


# D.1
for i in range(1,10):
    print(10-i)

    
# D.2
number = int(input("Enter a number to get a multiplication table:"))
for i in range (1, number+1):
    print(number, "x", i, "=", number*i)

    
# D.3
songs = ["Barfly","Barista Breaks","Glamourgirl","Smooth"]
for i, x in enumerate(songs):
    print(i,x)

    
# D.4
for x in range(1,3):
    for y in range(1,4):
	    print(y,x)

        
# D.5
num_list = []
for x in range (1,6):
	row = []
	for y in range(1,6):
		row.append((x,y))
	num_list.append(row)
print("\nShow me:",num_list)


# Part E While Loops


# E.1 


x = 10
while x > 0:
    print(x)
    x -=1

    
# E.2
password = "password"
while (password != input("Enter correct password ")):
    continue


# E.3

seed = 0
food = {1:"banana", 2:"apple", 3:"kiwi", 4:"icecream", 5:"fudge", 6: "orange"}
while (input("Type quit or see the food:") != "quit"):
    seed = random.randint(1,5)
    print(food[seed]) 


# E.4


total = 0
user_input = 0
print("Continue to provide numbers and I will count them for you, until you hit 0")

while (True):
    user_input = int(input())
    total += user_input
    if(user_input == 0):
        break
    # Apaprently there is a new thing clled walrus; (user_input := int(input())) != 0:...
print("\nThe total is: ",total) 


# E.5


secret_numba = 9
print("Guess the magic number between 1 and 10")
while (True):
    user_input = int(input())
    if (user_input == secret_numba):
        print("Congrats")
        break
    elif (user_input > secret_numba):
        print("Your guess is too high")
    else:
        print("Your guess is too low") 


# Part F break & continue

# F.1

for x in range(1,100):
    if (x % 7 == 0 and x % 9 == 0):
        print("\nNumber divisble by both 7 and 9 is:",x)
        break 


# F.2


list_of_strings = ["banana", "apple", "", "kiwi", "", "icecream", "fudge", "orange"]
for x in list_of_strings:
    if (x != ""):
        print("\nYou can eat",x)
    else:
        continue 


# F.3


find = "banana"
def findData(item_to_be_found):
    list_of_strings = ["banana", "apple", "", "kiwi", "", "icecream", "fudge", "orange"]
    for x in list_of_strings:
        if (x == item_to_be_found):
            print("\nYou found me!")
            break
    else:
        print("Requested data not found.")

findData(find)
findData("TOMATO") 

# simple call to a funciton that check if the supplied data is found. If not found, when the whole loop went through,
# it prints corresponding information.


# F.4

print("\nEnter values for processing please. Program stops on 999 input.")
processed_values = []
while(True):
    user_input = int(input())
    if (user_input == 999):
        break
    elif (user_input > 0 and user_input < 999 ):
        processed_values.append(user_input)
    else:
        continue

print("The values entered were: ", processed_values)
# Part G Applied Challenge

#G.1-2
study_sessions = [
    {"Subject":"Sports", "Duration":"25"},
    {"Subject":"Warm Up", "Duration":"35"},
    {"Subject":"Walking", "Duration":"45"},
    {"Subject":"Yoga", "Duration":"55"},
    {"Subject":"Heavy Coding", "Duration":"25"},
    {"Subject":"Coding", "Duration":"35"},
    {"Subject":"Enlgish", "Duration":"45"},
    {"Subject":"Gym", "Duration":"55"},
    {"Subject":"History", "Duration":"96"},
    {"Subject":"Politics", "Duration":"35"}]


total_minutes = 0
for x in study_sessions:
    total_minutes += int(x["Duration"])
    
print("\nGrand Total", total_minutes)


# G.3
empty_dictionary = {"Total Minutes" : 0}
for x in study_sessions:
    empty_dictionary["Total Minutes"] += int(x["Duration"])
print("\nGrand Total Dictionary Style:", empty_dictionary)


# G.4
current_max = int(study_sessions[0]["Duration"])
for x in study_sessions:
    if current_max < int(x["Duration"]):
        current_max = int(x["Duration"])

print("\nMax value via loop is:",current_max)


# G.5
for x in study_sessions:
    if int(x["Duration"]) > 45:
        print("The session for ", x["Subject"],"is longer than 45 minutes.")


total_minutes = 0
for x in study_sessions:
    total_minutes += int(x["Duration"])

print("\nWhat would you like to see? All Sessions? Total time of sessions (type total)? Filter sessions by subject or quit?")
sorted_sessions = []
while(True):
    user_input = input()
    if (user_input == "quit"):
        break
    elif (user_input == "All Sessions"):
        print(study_sessions)
        continue
    elif (user_input == "total"):
        print("\nTotal session time is:",total_minutes)
    elif (user_input == "filter"):
        print("\nFiltered session list:\n",sorted(study_sessions, key=lambda k : k["Subject"]))
        continue
    else:
        print("Unidentified input provided, better luck next time.")
        break


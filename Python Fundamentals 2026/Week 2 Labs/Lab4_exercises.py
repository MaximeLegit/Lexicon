################################################## LECTURE ##################################################

def add (a: int, b: int) -> int:
    return a + b
#print(add("Yo","Dane"))

# Docstrings

def calculate_area(width, height):
    """ Return are of rectangle """
    return width * height

#print(calculate_area(9,9))
#print(calculate_area.__doc__)

################################################## LECTURE ##################################################

# Part A


def greet():
    print("Howdy")

def show_course_name():
    print("Python 2026 course")

def print_separator():
    print(" ")

for x in range(1,3):
    greet()
    show_course_name()

def greet_person(name):
    print("Hi",name)
greet_person("Lola")

def introduce(name,city="Alaska"):
    print("Your name is", name, "and you live in", city)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Show me add", add(5,6), "subtract", subtract(5,6), "multiply", multiply(9,9), "divide", divide(32,8))


introduce("Max")  # Default argument is used.
introduce("Max","London") # Both parameters are supplied and default one is overwritten.

print("Random calculation", 5 * calculate_area(4,5))


# Part B Return values

def is_even(number):
    return number % 2 == 0
print("Is numba 4 even?",is_even(4))


def get_larger(a,b):
    if a > b:
        return a
    else:
        return b
print("Which is bigger?",get_larger(5,6))


def classify_score(score):
    if score > 40:
        return "PASS"
    else:
        return "FAIL"

def full_name(first_name, last_name):
    print(f"First name:",first_name,"Last name:",last_name)
full_name("Lola", "Go")



def calculate_discount(price, percent):
    return price - (price * (percent / 100))
#print(int(calculate_discount(100, 25)))


def show_example():
    t = calculate_discount(100, 50)
    print("show_example method print:", int(t))

print("\nPrint form a function", show_example(), "vs. returning a value", int(calculate_discount(100, 25)))
print("Since the func returns a value and we do nothing with it, hence the none. Proper way is to either bind the result" \
    "to a variable, or call directly like I do and print its return")


# Part C Defaults and keywords

def greet(name, greeting="Hello"):
    print(greeting,name)
#greet("Max")
#greet("Max","Hi")

def calculate_price(price, quantity=1, discount=0):
    if discount > 0:
        return quantity * (price - (price * (discount / 100)) )
    else:
        return quantity * price 
#print("Discount 50%:", calculate_price(1000, discount=50), "Discount? None for you:", calculate_price(1000))


def create_profile(name, city="Unknown", active=True):
    return {"Name":name, "City":city, "Active":active}
#print(create_profile("Lola"))
#print("\nCalling func with different keyword order",create_profile(active=False, name="Ninja"))

#def problem(test_1 ="test_1", test_2):
#    print(test_1, test_2)
# As you mentioned in the lecture, and this I do not recall or did not know, undefined parameters cannot follow a defined ones.
# if we want an unassigned parameter, it has to go first. Otherwise compiler with not compile.

# Part D Functions and collections


def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
#print("Total:", calculate_total([1,2,3,3,4]))


def count_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
#print("Even total:",count_even([2,4,6,8,9,11]))


def get_long_words(words, minimum_length):
    return [words,minimum_length]


def find_student(students, name):
    for student in students:
        if student["Name"] == name:
            return student["Name"]
        else:
            return None

def detective_mode():
    search = find_student([{"Name":"Oskar", "City":"Lund"}, {"Name":"Bobby", "City":"Luleå"}], "Max")
    #search_2 = find_student([{"Name":"Oskar", "City":"Lund"}, {"Name":"Bobby", "City":"Luleå"}], "Oskar")
    if search != None:
        print("\nThe student", search, "was found.")
    else:
        print("\nThe student was absent.")

#detective_mode()


def average_score(students):
    """ Count the average score """
    total_score = 0
    for student in students:
        total_score += student["Score"]
    print("\n\nAverage score: ", (total_score / len(students)))


def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"] == True:
            active_users.append(user)
    return active_users

result = get_active_users([{"Name":"Oskar", "active":True}, {"Name":"Bobby", "active":False},{"Name":"Max", "active":True},{"Name":"Max", "active":False}])
print("\n\nActive users: ", result, "Active users type: ", type(result))


# Part E Decomposition

def celsius_to_farenheit(celsius):
    """ Convert celsius to farenheit """
    fahrenheit = round(((celsius * (9/5)) + 32),2)
    if fahrenheit > 80:
        print(f"{celsius}C is equal to {fahrenheit}F and it is HOT")
    elif fahrenheit > 50:
        print(f"{celsius}C is equal to {fahrenheit}F and it is WARM")
    else:
        print(f"{celsius}C is equal to {fahrenheit}F and it is COLD")
    print("\nType of variables for celsicus and farenheit respectively are:", type(celsius),"and",type(fahrenheit))

def subtotal(current_sum):
    return current_sum

def discount(amount, percentage):
    return amount * (percentage / 100)

def final_total(current_amount, price_reduction):
    temp_sum = subtotal(current_amount)
    rabatt = discount(temp_sum, price_reduction)
    final_sum = temp_sum - rabatt
    print("Your total is:_", final_sum, "kronors. The type of variable final_sum is: ", type(final_sum))


# Part F - Applied challenge: Event registration processor 

def validate_participant(participants):
    validated_data = []
    age_range = False
    for participant in participants:
        registration_fee = 1000
        name = participant["Name"].strip().title()
        if (participant["Age"]) > 18 :
            age_range = True
        if age_range:
            registration_fee += 25
        validated_data.append({"Name":name, "Age": participant["Age"], "Registration Fee": registration_fee})
    return validated_data

def revenue(data):
    total_revenue = 0
    for x in data:
        total_revenue += x["Registration Fee"]
    return total_revenue

def get_students(participants):
    student_participants = []
    for participant in participants:
        student_participants.append(participant["Name"])
    return student_participants

def get_oldest_participant(participants):
    current_oldest_participant = participants[0]["Age"]
    oldest_participant = None
    for i, participant in enumerate(participants,1):
        if participant["Age"] > current_oldest_participant:
            current_oldest_participant = participant["Age"]
            oldest_participant = participant["Name"]
    return oldest_participant

def readable_summary(participant):
    """ Print readable summary of participants, as its type """
    print(f"{participant["Name"]} is {participant["Age"]} years old.")


# Part G

def get_min_max(data):
    data.sort()
    min = data[0]
    max = data[len(data)-1]
    return min, max

def is_palindrome(word):
    return True if word == word[::-1] else False

def count_character_frequencies(word):
    """ Return count frequencies of a character """
    frequencies = {}
    for character in word:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
    return frequencies

def get_keys(data):
    """ Return positive, negative, zero keys for the given list """
    positive_keys = []
    negative_keys = []
    zero_keys = []
    for value in data:
        if value < 0:
            negative_keys.append(value)
        elif value > 0:
            positive_keys.append(value)
        else:
            zero_keys.append(value)
        
    return {"Positive Keys:" : positive_keys, "Positive Key count:" : len(positive_keys),
            "Negative Keys:" : negative_keys,  "Negative Key count:" : len(negative_keys),
            "Zero Keys: " : zero_keys, "Zero Key count: " : len(zero_keys)}
    

if __name__ == '__main__':
    #average_score([{"Name":"Oskar", "Score":25}, {"Name":"Bobby", "Score":35},{"Name":"Max", "Score":45},{"Name":"Max", "Score":65}])
    #print("\n\n")
    #celsius_to_farenheit(35)
    #celsius_to_farenheit(15)
    #celsius_to_farenheit(2)
    print("\n\n")
    #final_total(100,10)
    validated_data = validate_participant([{"Name":"Oskar Awesome", "Age":18}, 
                         {"Name":"Bobby Blue", "Age":69},
                         {"Name":"Max Burger", "Age":45},
                         {"Name":"Al Capone", "Age":35},
                         {"Name":"Ryn Gosling", "Age":55},
                         {"Name":"Annie Blue", "Age":15},
                         {"Name":"Scarlet Johansson", "Age":43},
                         {"Name":"Bradd Pitt", "Age":65}])
    #print(validated_data)
    #print("Total revenue:", revenue(validated_data))
    #print("get_students:", get_students(validated_data))
    #print("Oldest: ", get_oldest_participant(validated_data))
    #readable_summary(validated_data[0])
    #min, max = get_min_max([1,2,3,40,5,6,70,8,9,11,22,33])
    #print("\n", min, ", ", max)

    #print(is_palindrome("Lola"))
    #print(is_palindrome("ALA"))

    char_freq_otp = count_character_frequencies("Abracadabra")
    #print(char_freq_otp)

    output = get_keys([1, -3, 5, 0, 0, 2, 4, -6])
    print(output)
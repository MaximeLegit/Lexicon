
# Part A


# A.1
print ("\nMaksims\nPyhton course 202\nGoing through the basics")

# A.2
name="Maksims"
age=35
height=1.87

print ("\n\nThis is", name, ",type", type(name), ", he is", age, "years old, type", type(age), "and ", height, "meters high, type", type(height))

# A.3
# This changes int to a float, a different data type.
age= 35.10
print("\nAge now is", age, "type", type(age))

# A.4
temp_1 = 1
temp_2 = 2
print("\nMathematical operations: Addition: ",(temp_1+temp_2),"Subtrraction:", (temp_1-temp_2), "Multiplication:",(temp_1*temp_2),
    "Normal division:",(temp_2+temp_1)," Floor: ", (temp_1//temp_2), "Remainder:",(temp_1%temp_2), "Exponent:", (temp_1**temp_2))

# A.5. Overwriting original age as input
age = input("Enter age:")
print ("\nAge is: ", type(age), "however, we need:", type(int(age))) 

#actual_price = 30/7
#print("\nactual_price=", actual_price, " which gives us that the price is ", str(actual_price))


#Part B


# B.1
def getData():
    name, yob = input("Enter age and year of birth").split()
    current_year = 2026
    print("\nYour age is", str(current_year-int(yob)))
getData()

# B2..
def displayPrice():
    price, discount = input("Please give us price and a discount").split()
    sum=float(price)-(float(price)*(float(discount)/100))
    print("\nFinal price is", str(round(sum,2)))
displayPrice()

# B.3 - 5.
def playingWithNumbas():
    temp_c = float(input("Enter celsius value:"))
    print ("\nValue in farenheit is" , str(round(((temp_c * (9/5)) + 32),2)))
    
    length, width = input("Enter length and width of a room:").split()
    area = float(length) * float(width)
    perimeter = 2 * float(length) + float(width)
    print("\nArea: ",area," Perimeter:",perimeter)
playingWithNumbas()

## if styring is entered, or non digit, due to that there is no try catch yet, an exception would be caught so program would crash


# Part C


# B.1 - 6
def strings():
    sentence = "Amaze amaze amaze"
    print("Length:", len(sentence), "\nUpper case:", sentence.upper(), "\nLower case", sentence.lower(), "\nWhite spaces purged:", sentence.replace(" ", ""))
    name, surname = input("Enter your name and surname").split()
    print(f"\nYour name is {name} and your surname is {surname}")
    str = "python programming"
    print("\n 1st char", str[0]," Last character:", str[-1], " First six:", str[0:5], "Last eleven:", str[-11:],"Reverse:", str[::-1])
    name, surname = input("Enter your name and surname ").split()
    username = (name[0:3] + surname[0:5]).lower()
    print(username)
    email= "maxim@awesome.com"
    extract_data = email.split("@")
    first, second = email.split("@")
    print("\nList version:",extract_data,"String version:",(first+second))
    java = "Java"
    print("Original:", java, "New:", java.replace("Java","Python"))
strings()


# Part D


# 1 - 4
def investigation():
    new_str = "ThermoNuclearAstroPhysics"
    print("Positive index: ", new_str[1], "Negative index:", new_str[-2], "Omitting:", new_str[1:len(new_str)-1], "Stepping",new_str[::2])
    ai = "Artifical Intelligence" #Same as above, just difference indexes.
    print("\nSplit using whitespace: ", ai.split(), "Strip 'a & e'", ai.strip("Ae"),"Replacing Intelligence with ..", ai.replace("Intelligence", "Food") )
    immutability ="I am a string"
    immutability[0] = "U"
    print("\n",immutability," which gives us a created string object, and one cannot randomly set a new value this way, however..")
    immutability = "U" + immutability[1:]
    print("this is the workaround", immutability)

investigation() 

# Part E


# 1 - 5
def data_collector():
    name, surname, city, yob, fav_programming_language = input("Please enter your name, surname, year of birth and favourite programming language: ").split()
    print(name, surname)
    # Since i perform split on input, no need to perform part 2.

    generated_id = (name[0:3] + yob[0:3])
    print(generated_id)
    print(f"\nYour name is {name}, surname is {surname}, you were born in {city}, your year of birth is {yob} and your favourite programming language is {fav_programming_language}")
    print("Initials: ", name[0], surname[0], "name length:", len(name), "fav lang: ", fav_programming_language[::-1])
data_collector()

# Part F


def converter():
    seconds = int(input("Please input seconds and see the magic: "))
    hours = seconds / 3600
    minutes = (seconds - 3600) / 60
    remaining_seconds = (seconds - 3600) % 60
    print("\nHours:", round(hours,1), "Minutes:", round(minutes,2), "Seconds: ", remaining_seconds)

    digits = list(input("Please input 4 digits: "))
    print("Digits are as follows:")
    for i in range(len(digits)):
        print("",digits[i])
    
    new_string = input("Please enter random text: ")
    mask_me = new_string[:2] # extract first two syllables
    for i in range(2,len(new_string)-2):
            mask_me += "*" # append the starts for the duration from 2nd to two digits from the end
    mask_me += new_string[-2:] 
    print("Now then: ", mask_me )


converter()
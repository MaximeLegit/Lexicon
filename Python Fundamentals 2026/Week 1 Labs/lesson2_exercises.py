# Part A - Lists, Slicing n Dicing

# A.1 -5

languages = ["Python", "Java", "C++", "JavaScript", "Go", "Rust", "Ruby", "Swift"]
print("\nFirst:",languages[0],"Last:",languages[-1],"Third:",languages[2],"Second to Last:",languages[-2])
print("\nSlices:",languages[0:3],"Next:",languages[2:5],"Soem More:",languages[-3:],"Reverse:",languages[::-1])

languages.append("Kotlin")
print("\nAppended list:",languages)

languages.insert(2, "PHP")
print("\nInserted into the list:",languages)

languages.remove("PHP")
print("\nRemoved recent addition",languages)

languages.pop()
print("Popped Kotlin:",languages)

numbers = [12, 45, 3, 67, 22, 89, 5]
print("\nLength:", len(numbers), "Min:", min(numbers), "Max:",max(numbers), "Sum:",sum(numbers))

numbers.sort()
print("\nSorted a list in ascending order", numbers)

numbers.reverse()
print("\nNow in descending:", numbers)

list_a = [1,2,3,4]
list_b = list_a
list_b.append(5)
print(list_a) 

list_c = list_a.copy()
list_c.append(67)
print("\nThe proper way, list_a:",list_a, "and list_c",list_c)


# Part B Tuppples

# B.1 - 4

rgb = {255, 0, 128}
r,g,b = rgb
print("\nThe values are:", r, g, b)

person = {"Frank", 29, "NY"}
name, age, city = person
print(f"Given name: {name} Age: {age} Lives in: {city}")

random_data = {25, 52} #The idea with tuples is that values should be fixed and not changed, when you want to set value permanently; Need modifications? Lists or sets

list_of_tuples =[(10, 20),(30, 40),(50, 60),(70, 80)]
print("Accesing 2nd tuple, 2nd element:", list_of_tuples[2][1])

# Part C Sets

courses = ["Math", "Math", "Sports", "English"]
unique_courses = set(courses)
print("\nLength before:", len(courses),"length after:",len(unique_courses))

dev_skills_1 = {"sql", "elrang", "java", "c++"}
dev_skills_2 = {"sql", "cherry", "chocolate", "c++"}
shared_skills = dev_skills_1 & dev_skills_2 # mental note, &, intersection
dev_1_only = dev_skills_1 - dev_skills_2 # # mental note, - , basic subtraction
both_devs = dev_skills_1 | dev_skills_2 # # mental note, | , basic union
print("\nShared skills:",shared_skills,"Developer one: ", dev_1_only, "Both developers:", both_devs)

numbers ={1, 2, 3, 4}
numbers.add(5)
numbers.discard(2)
print("\nNumber set:", numbers)

# I think set can be used slightly faster but they cannot be referenced with values, like set[1]


# Part D Dictionaries


laptop = {"Brand:" : "Asus", "Model" : "Vivobook", "RAM" : 32, "Price" : "20000"}
print("Value for key Brand is:", laptop["Brand:"])
print("Values for each key are:")
for v in laptop.values(): #values + items
    print(v)

laptop["Price"] = 10000

laptop.pop("RAM")
print(laptop)

print("\nThis is",laptop.get("Brand"))
print("\nThis should not exist: ",laptop.get("Donald"))

print("\nAll the keys are:")
for k in laptop.keys():
    print(k)

print("\nAll the values are:")
for v in laptop.values():
    print(v)

print("\nAll the pair combinations are:")
for i in laptop.items():
    print(i)

study_data= {"Math":"8", "English":"9", "Swedish":"12", "Sports":"7", "History":"30"}
total_hours = 0
for x in study_data.values():
    total_hours += int(x)
print("\nTotal hours:", total_hours)



# Part E Nested collections


list_of_dicts = [{"Title": "Omega", "Author": "C. Clark", "Pages:": "89", "Availability": "Booked", "Year":"1968"},
                 {"Title": "Dawn", "Author": "C. Clark", "Pages:": "98", "Availability": "Available", "Year":"1969"},
                 {"Title": "I, Robot", "Author": "Isaac Asimov", "Pages:": "234", "Availability": "Booked", "Year":"1952"},
                 {"Title": "The Robots of Dawn", "Author": "Isaac Asimov", "Pages:": "234", "Availability": "Booked", "Year":"1955"},
                 {"Title": "The Naked Sun", "Author": "Isaac Asimov", "Pages:": "234", "Availability": "Available", "Year":"1962"}]
print("\nTitle of the 3rd book is:", list_of_dicts[2]["Title"], " and is the book availabe?",list_of_dicts[4]["Availability"] )

list_of_dicts[0]["Title"] = "Zero"
list_of_dicts[0]["genre"] = "Sci-FI"
print("\n",list_of_dicts[0])

company_data = [{"IT":"Max"}, {"Reception":"Donald"}, {"Security":"Mikael"}]

course = [{"Name":"Networking", "Teacher":"Anton", "Topic": ["Routing", "Switching"]}, 
          {"Name":"Java", "Teacher":"Annie", "Topic": ["Coding","Debugging"]}, 
          {"Name":"Python", "Teacher":"Aladdin", "Topic": ["Lists","Tuples"]}]
x=0
while x < len(course):
    print("\nChained Indexing topic:",course[x]["Topic"][1])
    x+=1



# Part F Personal Media Catalogue


game_catalogue = [{"Game":"DarkSouls", "Genre":"Soulslike", "Level":"Expert", "Difficulty":"Normal","Year":2005},
                  {"Game":"DarkSouls2", "Genre":"Pleb", "Level":"Expert", "Difficulty":"N/A","Year":2009},
                  {"Game":"DarkSouls3", "Genre":"Soulslike", "Level":"Good", "Difficulty":"Insanity","Year":2012},
                  {"Game":"Lies of P", "Genre":"Soulslike", "Level":"Decent", "Difficulty":"Insanity","Year":2020},
                  {"Game":"Nioh 2", "Genre":"Soulslike", "Level":"Decent", "Difficulty":"Dream of the Demon","Year":2018},
                  {"Game":"Nioh 3", "Genre":"Soulslike", "Level":"Decent", "Difficulty":"Dream of the Demon","Year":2026},
                  {"Game":"God of War", "Genre":"Soulslike", "Level":"Decent", "Difficulty":"N/A","Year":2018},
                  {"Game":"Assassins Creed", "Genre":"Adventure", "Level":"Expert", "Difficulty":"Insanity","Year":2000}]

unique_catalogue = set()

for p in game_catalogue:
    unique_catalogue.add(tuple(p.items()))

print("\n",game_catalogue[0]["Game"])
print("\n",game_catalogue[-1]["Game"])
print("\n","Difficulty" in game_catalogue[3])
print("\n","Challenge" in game_catalogue[3])

game_catalogue[2]["Year"] = 2011
print("\n",game_catalogue[2])

game_catalogue[2]["Boba"] = 2025
print("\n",game_catalogue[2])

game_catalogue.pop()
print("\nFull Set should be missing Lies of P now..\n",game_catalogue)


# Part G Stretch

usernames_1 = ["lola", "daffy", "crypto"]
usernames_2 = ["floyd", "link", "daffy"]

set_1 = set(usernames_1)
set_2 = set(usernames_2)

print("\nDuplicates in the sets: ", (set_1 & set_2), "Unique: ", (set_1 ^ set_2))

course_platform = [
    {"Course name": "Math", "Teachers":["Sven","Olaf"], "Students": ["Me","Myself","&I"], "Topics": ["Algebra","Geometry"]},
    {"Course name": "NeuroScience", "Teachers":["Adam","Bobby"], "Students": ["Andrew","Gabby"], "Topics": ["Grey Matter","Neuro Path Ways"]},
    {"Course name": "Philosofy", "Teachers":["Patrik","Emma"], "Students": ["Venus","Lena","Sam"], "Topics": ["Manners","Behavior"]}
]

products = {"Mouse":22, "keyboard":44, "Camera":2000, "Speakers":4000, "OLED Screen":9999}
products["Mouse"] = 19
print("\nShow: ",products["Mouse"])

total_units = 0
for x in products.values():
    total_units += x
print("\nTotal Units: ", total_units)

# I see lists as a list of items, usually of one and the same type, and they cna be modified.
# Tuples, primarily, cannot be modified. They are ordered and usually have pairs of different elements in them.
# I see sets as when you want something, unique, or check fi there are duplicates, but you can also modify it, like add or remove.
# Dictionaires are good to make key value pairs, like different types and then access them. Python has made cool built in functions for that.
# One can also access them by indexes.
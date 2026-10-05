################################################## LECTURE ##################################################

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
student_1 = Student("Lola", 99)
#print(student_1.name)



################################################## LECTURE ##################################################

# Part A Classes and objects

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_long(self):
        return True if self.pages > 300 else False

first_book = Book("Stranger in a strange land", "Robert A. Heinlein", 486)
second_book = Book("The caves of Steel", "Isaac Asimov", 244)
third_book = Book("Gateway", "Fredrik Pohl", 386)
fourth_book = Book("Red Rising", "Pierce Brown", 444)
fifth_book = Book("Golden Son", "Pierce Brown", 386)

#print("Sample print of first book, the title:",first_book.title, "Author:", first_book.author, "Total pages:", first_book.pages)
#print("Sample print of first book, the title:",fifth_book.title, "Author:", fifth_book.author, "Total pages:", fifth_book.pages)


class Laptop:
    def __init__(self, brand, model, ram_gb = 64, price = 30000):
            self.brand = brand
            self.model = model
            self.ram_gb = ram_gb
            self.price = price

asus = Laptop("Asus", "Vivobook", 32, 10000)
asus_2 = Laptop("Asus", "Zenbook", 32, 12000)
msi = Laptop("MSI", "Stealth", 32, 15000)
#print("Current asus price=",asus.price)

asus.price = 20000
#print("Now it is",asus.price)


msi_2 = Laptop("MSI", "Stealth", 32, 15000) # same as msi
#print("Are they the same object?", msi is msi_2)


lenovo = Laptop("Lenovo", "Ideapad")
#print("Values for lenovo with default parameters: ", lenovo.brand, lenovo.model, lenovo.ram_gb, lenovo.price)

acer = Laptop(brand="acer", model="predator", ram_gb=24, price=17999)
#print("Acer values:", acer.brand, acer.model, acer.ram_gb, acer.price)


# Part B Methods and state

#print("Is the first book long?", first_book.is_long(), "Correct, since it's page count is", first_book.pages)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, sum_to_remove):
        if self.balance >= sum_to_remove:
            self.balance -= sum_to_remove
            print(f"{self.balance} if left on your bank account")
        else:
            raise ValueError(f"Not enough money in the account to withdraw {sum_to_remove}")

my_bank_account = BankAccount("Max", 100)
my_bank_account.deposit(100)
#print("Current sum:", my_bank_account.balance)

my_bank_account.withdraw(150)
#print("Updated sum:", my_bank_account.balance)

#my_bank_account.withdraw(150)
#print("Should be value error if I were to remove comment on line above..")


class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed  

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

first_task = Task("Push Ups")
#print("State of the object first task is: ", first_task.title, first_task.completed)


second_task = Task("Pull Ups")
second_task.complete()
#print("Push Ups should not be false? ", first_task.completed, "Whilst pull ups are complete, right?", second_task.completed)

second_task.reopen()
#print("On second thought, let me double check something..and, are pull ups actually done?", second_task.completed, 
#      "Thereby demonstrating that changing state of the second task has absolutely no effect on the first_task")


# Part C Instances and class attributes

class Product:

    tax_rate = 0.33
    def __init__(self, name, price):
        self.name = name
        self.price = price  
    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)
    def __repr__(self):
        return f"Product name: {self.name} price: {self.price}"

paint = Product("paint", 300)
bike = Product("bike", 5000)
car = Product("car", 25000)
updated_paint_price = paint.price_with_tax()
updated_bike_price = bike.price_with_tax()
updated_car_price = car.price_with_tax()

#print(f"Price of paint is {updated_paint_price}, price of the bike is {updated_bike_price}, car's price is {updated_car_price}")

Product.tax_rate = 0.15
updated_paint_price = paint.price_with_tax()
updated_bike_price = bike.price_with_tax()
updated_car_price = car.price_with_tax()

#print(f"NEW price of paint is {updated_paint_price}, price of the bike is {updated_bike_price}, car's price is {updated_car_price}")

paint.tax_rate = 0.1
extra_cheap_paint = paint.price_with_tax()
#print("Paint's object price with the new super, duper, mega, I-wish-I-Had-Such-Taxes is:", extra_cheap_paint)


#print("Bike object is: ", repr(bike))
#print("Product class is:", Product)  


# Part D Collections of objects

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= 70 else "FAIL"

    def __repr__(self):
        return f"Student: {self.name}, score: {self.score}"

students = [
    Student("Lola", 85),
    Student("Max", 999),
    Student("Bonny", 91),
    Student("Fanny", 45),
    Student("Eren", 70),
    Student("Jimmy", 58),
]

for student in students:
    #print(f"Student: {student.name}, score: {student.score}")
    print(f"Student: {student.name}, status: {student.get_status()}")

greatest_students = [student for student in students if student.score >= 70]
print("Greatest students:", greatest_students)


# Part E Objects inside objects


class Teacher:
    def __init__(self, name):
        self.name = name

class Course:

    school = "Lexicon"
    # In this case, after teacher's feedback, it is a good example that whilst having information about students, the curse, the teacher,
    # there can be multiple schools. It is so simple yet brilliant. This was, if we have this as a class attribute, we can easily define
    # it to someone else, whilst currently it is hardcoded to "Lexicon", but it can be other things too of course.

    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student, score):
        self.students.append(Student(student, score))

    # I did this separate method to cover the case that if I want to add more than one student, and the above method is for one respecively.
    def add_students(self, list_of_students):
        self.students.extend(list_of_students)

    def get_students(self):
        return self.students
    
    def get_passing_students(self):
        if len(self.students) == 0:
            raise ValueError(f"None of the students have passed")
        return [student for student in self.students if student.score >= 70]

    def update_score(self, student, score):
        for st in self.students:
            if student == st.name:
                st.score = score
                print("Students:", st.name, "new score is", st.score)
                break
        else:
            print("Requested student not found.")

    def above_threshold(self, threshold):
        return [student for student in self.students if student.score >= threshold]

#teacher_obj = Teacher("Aladdin")
course = Course("Coding", "Aladdin")
print("Displaying course name:", course.course_name, "and subsequently the teacher:", course.teacher)

course.add_student("Max", 55)
course.add_student("Gloria", 66)
course.add_student("Janne", 77)

for student in course.students:
    print(student)

# Part F Applied Challenge

# Explanation: Student and Teacher class have everyting required. I have modified Course class to perform the missing functionalities.
# Hence, the only part missing was the 2 students, where we had to create 5 in total, and tests + the course summary which is:

print("Adding previously defined students to the course.")
course.add_students(students) # line 166
for student in course.students:
    print(student)

print("Now adding Bobby on top.")
course.add_student("Bobby", 5)
for student in course.students:
    print(student)

print("Show me passing students:")
passing_studs = course.get_passing_students()
print(passing_studs)

print("Now show me all students:")
all_students = course.get_students()
print(all_students)

print(f"Course summary: Course name: {course.course_name}, teacher name: {course.teacher}, number of students: {len(all_students)}, Passing students: ")
for student in passing_studs:
    print(student.name)


# Part G Stretch


course.update_score("Max", 99)
course.update_score("Aladdin", 99)


print("Students who scored above 30 are:", course.above_threshold(30))


extra_course = Course("Chilling", "Max")
print("Displaying course name:", extra_course.course_name, "and subsequently the teacher:", extra_course.teacher, "and are there any students?" \
,extra_course.students, "No! The list is empty since I added none.")

# Last part was added on line 192 along with the explanation.
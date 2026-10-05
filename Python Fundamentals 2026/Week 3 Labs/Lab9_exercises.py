################################################## LECTURE ##################################################
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "unknown"

class Dog(Animal):
    def make_sound(self):
        #return super().make_sound()
        return "Woof Woof"

class Cat(Animal):
    def make_sound(self):
        #return super().make_sound()
        return "Meow Meow"

animals = [Dog("Rex"), Cat("Shaula")]


for animal in animals:
    print(animal.name, animal.make_sound())

# work if class is empty, not with an init.
#dog = Dog("Buba")
#print(isinstance(dog, Dog("GG")))


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name} - Score: {self.score}"

student = Student("Lola", 99)


# has-a composition

class Engine:
    def __init__(self, hp):
        self.hp = hp
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine(200)
car = Car("Audi", engine)
print(car.brand, car.engine.hp)
################################################## LECTURE ##################################################


################################################ Assignment ##################################################

# Part A. Polymorphism

class Notification:
    def send(self):
        return "General Message"

class EmailNotification(Notification):
    def send(self):
            return "Email Notification"

class SMSNotification(Notification):
    def send(self):
        return "SMS Notification"

notifications = [Notification(), EmailNotification(), SMSNotification()]

for notification in notifications:
    print(notification.send())
# Why this works. This works because notification is using whatever element, be that class object, and integer or a string to do what I say it to do, in this case,
# send the message. 


# Part B. Polymorphism with inheritance


class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "The document is " + self.title

class PDFDocument(Document):
    def describe(self):
        return "The PDF document is " + self.title

class TextDocument(Document):
    def describe(self):
        return "The Text document is " + self.title


documents = [PDFDocument("Aurora"), PDFDocument("Borealis"), TextDocument("Notepad"), TextDocument("++")]

for document in documents:
    print(document.describe())


# Part C. Duck typing


class Printer():
    def display_status(self):
        return "Printy Print"

class Screen():
    def display_status(self):
        return "Screeny Screen"

display_statuses = [Printer(), Printer(), Screen(), Screen()] # This is a bit odd, but it works. Would not get a +1 on a code review here though.

for ds in display_statuses:
    print(ds.display_status())
# This works simple since each class is its own entity with a function called display_status(). I simply create an object and then call that function
# that happens to have the same name, nothing more. Henec you see the printy print and screeny screen.


# Part D. isinstance()


class User:
    def who_am_i(self):
        return "User"

class AdminUser(User):
    def who_am_i(self):
        return "AdminUser"

auo = AdminUser()
print(f"Is auo an object is an AdminUser object? {isinstance(auo, AdminUser)}, a user object? {isinstance(auo, User)} and is it a string? {isinstance(auo, str)}")

# Admin user is considered an instance of user because of the IS-A relationship here, since AdminUser class inherits the User class, line 131.


# Part F. __str__ with inheritance


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"{self.owner} - Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def __str__(self):
        return super().__str__() + f" Interest rate: {self.interest_rate}"

account = Account("Lola", 9999)
savings_account = SavingsAccount("Max", 8888, 0.02)

print(savings_account)


# Part G. Inheritance or composition


class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, cpu, brand):
        self.cpu = cpu
        self.brand = brand

cpu = CPU("7950x3D")
computer = Computer(cpu, "Ryzen")

print("Model:", computer.cpu.model, "Brand:", computer.brand)

# so by using composition, we do not inheriten the cpu class directly, but we rather reference it in the constructor so that when the
# computer is created, we may insert the cpu object. 
# Car / Engine       - composition HAS - A
# Manager / Employee - composition HAS - A
# Course / Teacher   - composition HAS - A
# Phone / Device     - inheritance IS - A


# Part H. Applied Challenge

class Exporter:
    def export(self, data):
        print("Exporter data:", data)
 
    def __str__(self):
        return "Generic Exporter"

class ConsoleExporter(Exporter):
    def export(self, data):
        print(f"Console Exporter: {data}")
 
    def __str__(self):
        return "Console Exporter"

class TextExporter(Exporter):
    def export(self, data):
        print(f"Text exporter: {data}")
 
    def __str__(self):
        return "Text Exporter"
 
class SummaryExporter(Exporter):
    def export(self, data):
        print(f"Summary Exporter: {data}")
 
    def __str__(self):
        return "Summary Exporter"


print("###############################\n\n")
data = "Data to be printed by EACH exporter"
exporters = [Exporter(), ConsoleExporter(), TextExporter(), SummaryExporter()]
for exporter in exporters:
    print("\nUsing", exporter)
    exporter.export(data)

class OutsideExporter:
    def export(self, data):
        print(f"OutsideExporter: {data}")
 
    def __str__(self):
        return "OutsideExporter, with same calling code"
oe = OutsideExporter()
print("\nShow it can be used by the same calling code: ", oe)

print("\n###############################\n")
final_exporters = [ConsoleExporter(), OutsideExporter()]
for fe in final_exporters:
    print(f"Is {fe} an instance of Exporter? {isinstance(fe, Exporter)}")
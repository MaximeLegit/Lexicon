from datetime import datetime
from pymongo import MongoClient

class Library():
    
    def generate_library_data(self, db):
        books = [
            {"_id" : 1, "title" : "Gateway", "nr_of_copies" : 1, "author" : "Frederik Pohl", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 2, "title" : "Beyond the Blue Event", "nr_of_copies" : 2, "author" : "Frederik Pohl", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 3, "title" : "Heechee Rendezvous", "nr_of_copies" : 3, "author" : "Frederik Pohl", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 4, "title" : "The Annals of the Heechee", "nr_of_copies" : 1, "author" : "Frederik Pohl", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 5, "title" : "The Boy who would live forever", "nr_of_copies" : 2, "author" : "Frederik Pohl", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 6, "title" : "Golden Son", "nr_of_copies": 3, "author" : "Pierce Brown", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 7, "title" : "Morning Star", "nr_of_copies": 3, "author" : "Pierce Brown", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}},
            {"_id" : 8, "title" : "Dark Age", "nr_of_copies": 2, "author" : "Pierce Brown", "genre" : "Sci-Fi", "status" : {"borrowed" : False, "borrowed_date" : None}}
        ]

        members = [
            {"_id": 1, "first_name": "Lola", "last_name": "Sven", "email": "lola.sven@example.com", "books_borrowed" : []},
            {"_id": 2, "first_name": "Maxime", "last_name": "The Great", "email": "maxime@example.com", "books_borrowed" : []},
            {"_id": 3, "first_name": "jwow", "last_name": "shy", "email": "jwow.shy@example.com", "books_borrowed" : []},
            {"_id": 4, "first_name": "Onion", "last_name": "Knight", "email": "onion.knight@example.com", "books_borrowed" : []}
        ]
        for name in ["members", "books"]:
            db[name].drop()

        db.members.insert_many(members)
        db.books.insert_many(books)

    def display_book_data(self, db):
        for book_data in db.books.find():
            print(book_data)

    def display_members_data(self, db):
        for member_data in db.members.find():
            print(member_data)

    def clean_library(self, db):
        for row in ["members", "books"]:
            db[row].drop()

    def select_member(self, db, id):
        result = db.members.find_one({"_id": id})
        print("\nGreat! You have selected ", result["first_name"])

    def display_book_data(self, db):
        for book_data in db.books.find():
            print(book_data)
    
    def borrow_a_book(self, db, member_id):
        time_limit = 14

        print("\nPlease type the desired book ID to be borrowed")
        while True:
            try:
                choice = input()
                if int(choice) in range (1,9):

                    borrowed_book = db.books.find_one({"_id": int(choice)})
                    db.books.update_one(borrowed_book, {"$inc" : {"nr_of_copies" : -1} }, {"$set" : {"status" : True, "borrowed_date" : datetime.now()}})

                    #member = 

                    print("verify Update")
                    break
                else:
                    print("\nInvalid number. Please try again.")
            except ValueError:
                print("\nYou must enter a a digit between 1-8 to borrow a book.\n")

#################### class end ################\n" \

def main_loop_print():
    print("\n1. Show available books" \
        "\n2. Show all members" \
        "\n3. Borrow a Book." \
        "\nX. Exit"
        )


def member_selection(db):
    print("\nWelcome to my Digital Library. We have a small collection of books that you can borrow and a small community who can borrow them." \
        "\nPlease select a member first by typing their ID number. Available members:\n")
    library_object = Library()
    library_object.display_members_data(db)
    member_id = None
    while True:
        try:
            member_id = input()
            if int(member_id) in range (1,5):
                library_object.select_member(db, int(member_id))
                break
            else:
                print("\nInvalid number. Please try again.")
        except ValueError:
            print("\nYou must enter a a digit between 1-4, not random hilly billy.\n")
    return int(member_id)

def run():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["webshop"]

    library_object = Library()
    library_object.generate_library_data(db)

    member_id = member_selection(db)
    print("\nNow you may proceed to browse the digital library and take books, a maximum of 3, to read." \
    "\nIf you wish to select another character at any time, please type the word <change>, without the specail symbols.")

    while True:
        main_loop_print()
        choice = input("\nPlease select the desired option:\n").strip()

        if choice == "1":
            library_object.display_book_data(db)
        elif choice == "2":
            library_object.display_members_data(db)
        elif choice == "3":
            library_object.borrow_a_book(db, member_id)
        elif choice == "X":
            print("Thank you for browsing my digital library. Adjo.")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == '__main__':
    run()

    # DB Design
    # The way I see this task is as follows. I make a database, populate it with books and members ( I have them predefined ), the I shall attempt to perform operations such as
    # borrow books, update the db correspondingly, select members, change members, cater for negative values and attempt to add, at a later stage, ranking system that keeps
    # track of the most popular books. So far, this skeleton is not designed for that. I plan to add book titles to member db and denote a book as borrowed via bo
    #

'''

Build a Python program called libary.py that manages a book club’s library using MongoDB and pymongo through a text-based menu.
 
Members should have a name and a unique email address. Books should have a title, author, genres, and number of copies. Members should be able to borrow books for 14 days and review books they have previously borrowed and returned.
 
Start by describing your database design in a comment, explaining and justifying which data you choose to embed and which data you choose to reference.
 
Add schema validation, indexes, and a menu option for generating test data.
 
The program should allow users to search for books, borrow and return books, view member profiles, and display overdue loans.
 
A member may borrow a maximum of 3 books at a time and must not be allowed to borrow any additional books if they have an overdue loan. The number of available copies must never become negative, and you must ensure this using a single database update operation.
 
Use MongoDB aggregation pipelines to generate reports, such as the most frequently borrowed books and the average rating for each book.
 
The program must handle invalid user input without crashing, and user input must never be inserted directly into a database query filter.
'''
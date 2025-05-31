import datetime
import csv
import os

Books = {
    "Python Crash Course": {"Author": "Eric Matthes", "Copies": 4},
    "Clean Code": {"Author": "Robert C. Martin", "Copies": 3},
    "Code Complete": {"Author": "Steve McConnell", "Copies": 2},
    "Automate the Boring Stuff": {"Author": "Al Sweigart", "Copies": 5},
    "The Pragmatic Programmer": {"Author": "Andy Hunt", "Copies": 2}
}

Members = {"Ruba", "Moh", "Nour", "Salma", "Omar"}

Borrow_member = [
    ["Ruba", 1, "Clean Code", datetime.date.today()],
    ["Moh", 2, "Python Crash Course", datetime.date.today()],
    ["Salma", 1, "Automate the Boring Stuff", datetime.date.today()]
]

def add_books():
    name = input("Book name: ")
    author = input("Author name: ")
    copies = int(input("Copies: "))
    if name in Books:
        Books[name]["Copies"] += copies
        print("Book updated.")
    else:
        Books[name] = {"Author": author, "Copies": copies}
        print("Book added.")

def display_books():
    for name, info in Books.items():
        print(f"{name} - {info['Author']} - {info['Copies']} copies")

def add_member():
    name = input("Username: ")
    Members.add(name)
    print("Member added.")

def display_members():
    for i, m in enumerate(Members, 1):
        print(f"{i}. {m}")

def borrow_book():
    display_books()
    user = input("Username: ")
    if user in Members:
        book = input("Book to borrow: ")
        if book in Books:
            num = int(input("Copies: "))
            if num <= Books[book]["Copies"]:
                Books[book]["Copies"] -= num
                Borrow_member.append([user, num, book, datetime.date.today()])
                print("Borrowed.")
            else:
                print("Not enough copies.")
        else:
            print("Book not found.")
    else:
        print("Not a member.")

def show_borrowed():
    for r in Borrow_member:
        print(f"{r[0]} borrowed {r[1]} of {r[2]} on {r[3]}")

def search_book():
    name = input("Search book: ")
    if name in Books:
        print(f"{name} - {Books[name]['Author']} - {Books[name]['Copies']} copies")
    else:
        print("Not found.")

def return_book():
    user = input("Username: ")
    book = input("Book to return: ")
    for r in Borrow_member:
        if r[0] == user and r[2] == book:
            Books[book]['Copies'] += r[1]
            Borrow_member.remove(r)
            print("Returned.")
            return
    print("No record found.")

def delete_book():
    name = input("Book to delete: ")
    if name in Books:
        del Books[name]
        print("Deleted.")
    else:
        print("Book not found.")

def update_book():
    name = input("Book to update: ")
    if name in Books:
        author = input("New author: ")
        copies = int(input("New copies: "))
        Books[name] = {"Author": author, "Copies": copies}
        print("Updated.")
    else:
        print("Book not found.")

def export_books():
    with open("books.txt", "w") as f:
        for name, info in Books.items():
            f.write(f"{name},{info['Author']},{info['Copies']}\n")
    print("Books exported.")

# عرض كامل محتوى Users.csv

def show_users_file():
    file_path = os.path.dirname(__file__)+"\\"+"Users.csv"
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read()
            print("\n--- Users.csv Content ---")
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# عرض كامل محتوى Ratings.csv
def show_ratings_file():
    file_path = os.path.dirname(__file__)+"\\"+"Ratings.csv"
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read()
            print("\n--- Ratings.csv Content ---")
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

while True:
    print("\n1. Add book\n2. Show books\n3. Add member\n4. Show members\n5. Borrow\n6. Borrowed\n7. Search\n8. Return\n9. Exit\n10. Delete book\n11. Update book\n12. Export books")
    print("13. Show Ratings\n14. Show Full Users File\n15. Show Full Ratings File")
    try:
        ch = int(input("Choice: "))
        if ch == 1: add_books()
        elif ch == 2: display_books()
        elif ch == 3: add_member()
        elif ch == 4: display_members()
        elif ch == 5: borrow_book()
        elif ch == 6: show_borrowed()
        elif ch == 7: search_book()
        elif ch == 8: return_book()
        elif ch == 9:
            print("Exit.")
            breakش
        elif ch == 10: delete_book()
        elif ch == 11: update_book()
        elif ch == 12: export_books()
        elif ch == 13: show_ratings_file()
        elif ch == 14: show_users_file()
        elif ch == 15: show_ratings_file()
        else: print("Invalid.")
    except:
        print("Enter a number.")

import datetime
import sqlite3
from sqlite3 import IntegrityError

connection = sqlite3.connect("todo.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS entries(
                    id INTEGER PRIMARY KEY,
                    todo STRING NOT NULL,
                    deadline STRING NOT NULL)""")


class Database:

    @staticmethod
    def add_db(todo, deadline, todo_index):
        try:
            cursor.execute("""INSERT INTO entries(id, todo, deadline)
                              VALUES
                              (?,?,?)""", (int(todo_index), str(todo), str(deadline)))
        except IntegrityError:
            print("Id is not unique")
        else:
            connection.commit()
            print("\nTodo successfully added!")

    @staticmethod
    def edit_db(index, newTodo, deadline):
        cursor.execute("""UPDATE entries SET todo = ?, deadline = ? WHERE id = ?""",
                       (str(newTodo), str(deadline), index))
        connection.commit()
        print("\nTodo successfully edited!")

    @staticmethod
    def delete_db(index):
        cursor.execute("""DELETE FROM entries WHERE id = ?""", (index,))
        connection.commit()
        print("\nTodo successfully deleted!")

    @staticmethod
    def get_data():
        cursor.execute("SELECT * FROM entries")
        data = cursor.fetchall()
        return data


class Todo:

    def __init__(self, text):
        self.text = text
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Date: {self.date.strftime('%d/%m/%Y %H:%M')} Text: {self.text}"


class Manager:
    @staticmethod
    def exit_program():
        e = input("Enter 'exit' to quit the program, click Enter to continue ")
        if e == "exit":
            quit()

    @staticmethod
    def set_deadline():
        deadline = input("Enter deadline in correct format (e.g. 20.04.2022): ")
        date = deadline.split(".")
        return f"Deadline: {date[0]}/{date[1]}/{date[2]}"

    def __init__(self, database):
        self.database = database

    def add(self, todo, todo_index):
        self.exit_program()
        deadline = self.set_deadline()
        self.database.add_db(todo, deadline, todo_index)

    def edit(self, index, newTodo):
        self.exit_program()
        deadline = self.set_deadline()
        self.database.edit_db(index, newTodo, deadline)

    def delete(self, index):
        self.exit_program()
        self.database.delete_db(index)

    def show_all(self):
        self.exit_program()
        data = self.database.get_data()

        if not data:
            print("There are no records in database!")

        else:
            for item in data:
                print(item)


def menu():
    choice = None
    db = Database()
    manager = Manager(db)

    while choice != "exit":

        print("\nMenu:")
        print("a) Add")
        print("e) Edit")
        print("d) Delete")
        print("s) Show")
        print("Enter 'exit' to  quit program\n")

        choice = input("Your choice: ")

        if choice.lower() == "a":

            text = input("ToDo text: ")
            todo_index = int(input("Enter id: "))
            todo = Todo(text)

            manager.add(todo, todo_index)

        elif choice.lower() == "e":

            manager.show_all()
            edit_index = int(input("Enter index: "))

            newText = input("Enter ToDo text: ")
            newTodo = Todo(newText)

            manager.edit(edit_index, newTodo)

        elif choice.lower() == "d":

            delete_index = int(input("Enter index: "))
            manager.delete(delete_index)

        elif choice.lower() == "s":
            manager.show_all()

        else:
            print("\nPlease choose correct option!")


menu()

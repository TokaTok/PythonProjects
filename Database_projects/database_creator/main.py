import sqlite3


class CreateDataBase:

    def __init__(self):
        self.data_base = input("What do you want to name the database?: ")
        self.table = input("What do you want to name the table?: ")
        self.columns = int(input("How many columns do you want in the table?: "))
        self.column_name = []
        self.column_type = []
        self.table_initialization()
        self.create_database()

    def table_initialization(self):
        for _ in range(self.columns):
            self.column_name.append(input("Column name: "))
            self.column_type.append(input("Column type: "))

    def create_database(self):
        connection = sqlite3.connect(f"{self.data_base}.db")
        cursor = connection.cursor()
        cursor.execute("")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table}("
                       f"id INTEGER PRIMARY KEY AUTOINCREMENT)")

        for i in range(self.columns):
            cursor.execute(f"ALTER TABLE {self.table} ADD COLUMN {self.column_name[i]} TYPE {self.column_type[i]}")
            connection.commit()


CreateDataBase()

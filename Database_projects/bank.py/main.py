from datetime import datetime
import sqlite3
import pytz

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR NOT NULL,
                    balance REAL NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS history(
                    id INTEGER,
                    date VARCHAR NOT NULL,
                    amount REAL NOT NULL,
                    status VARCHAR)""")


class Account:

    @staticmethod
    def _get_local_time():
        return pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()

    def __init__(self, name, balance=0):
        self.name = name

        try:
            self.balance = int(balance)

        except:
            self.balance = 0

        cursor.execute("""INSERT INTO accounts(name, balance)
                            VALUES
                            (?,?)""", (self.name, self.balance))

        connection.commit()

        self.uid = cursor.lastrowid

    def __db_operate(self, balance, amount, status):

        cursor.execute("""INSERT INTO history
                            VALUES
                            (?,?,?,?)""", (self.uid, self._get_local_time(), amount, status))

        cursor.execute("""UPDATE accounts SET balance = ? WHERE id = ?""", (balance, self.uid))

        connection.commit()

    def deposit(self, amount):

        try:
            self.balance += amount
            print(f"Your balance increased by {amount} USD.")
            print(f"Balance: {self.balance} USD")
            self.__db_operate(self.balance, amount, "DEPOSITED")

        except:
            print("Please make sure your input is correct!")

    def withdraw(self, amount):

        try:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Your account decreased by {amount} USD")
                print(f"Balance: {self.balance} USD")
                self.history.append([self._get_local_time(), "-" + str(amount), self.balance])

            else:
                print("Not enough money on the balance!")

        except:
            print("Please make sure your input is correct!")

    def show_balance(self):
        print(f"There is {self.balance} USD on your balance.")

    def show_history(self):

        for date, amount, balance in self.history:
            print(f"{date} >> Amount: {amount} >> Balance: {balance}")


acc = Account("Tornike")

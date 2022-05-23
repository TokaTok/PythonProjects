import requests
from bs4 import BeautifulSoup
import re
from tkinter import *

r = requests.get("https://www.worldometers.info/coronavirus/")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data1 = soup.find("div", {"class": "tab-content", "id": "nav-tabContent"})
data2 = data1.find("div", {"class": "main_table_countries_div"})
data3 = data2.find("tbody")
data4 = data3.find_all("tr")

def find_recovered():
    country = country_entry.get()
    country = country.title()
    if country == "Usa":
        country = "USA"
    elif country == "Uk":
        country = "UK"
    userrows = [t for t in data4 if t.find_all(text=re.compile(f'{country}'))]
    recovered_data = str(userrows[0])
    ans1 = recovered_data.split(">")
    ans1 = ans1[16]
    ans1 = ans1.split("<")
    recovered_number = ans1[0]
    answer_entry.insert(0, recovered_number)


window = Tk()
window.title("Total Recovered By Country")

celsius_label = Label(text="Which country do you want to check?")
celsius_label.grid(row=0, columnspan=2)

country_entry = Entry(width=40)
country_entry.grid(row=1, columnspan=2)

get_button = Button(text="Get Data", width=20, command=find_recovered)
get_button.grid(row=2, column=0)

answer_entry = Entry(width=40)
answer_entry.grid(row=3, columnspan=2)

window.mainloop()


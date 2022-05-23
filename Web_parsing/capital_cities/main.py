import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://geographyfieldwork.com/WorldCapitalCities.htm")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data = soup.find("div", {"id": "mainCont"})
capitals = data.find("div", {"id": "dataG"})
capitals2 = capitals.find("table", {"class": "sortable"})
capitals3 = capitals2.find_all("tr")


def getting_to_answer(dt):
    split_data = dt.split("\n")
    split_data = split_data[2]
    split_data = split_data.split(">")
    split_data = split_data[1]
    split_data = split_data.split("<")

    return split_data[0]


while True:
    country = input("Enter the country you want to know capital of? enter 'Exit' to quit the program: ")
    country = country.capitalize()
    if country == "Exit":
        break
    userrows = [t for t in capitals3 if t.find_all(text=re.compile(f'{country}'))]
    capital_data = str(userrows[0])
    answer = getting_to_answer(capital_data)
    print(f"The capital of {country} is {answer}")

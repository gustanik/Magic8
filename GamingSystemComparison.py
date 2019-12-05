import pandas as pd
import mysql.connector

import matplotlib.pyplot as plt
import csv
from sqlalchemy import create_engine
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='cna330')
cursor = conn.cursor()
cursor.execute("CREATE TABLE gamereviews(id int PRIMARY KEY, score_phrase varchar(50), title varchar(100), url varchar(200), platform varchar(100), score float, genre varchar(50), editors_choice TEXT, release_year int, release_month int, release_day int);")

df = reviews = pd.read_csv("ign.csv") #converts .csv file into Panda dataframe

engine = create_engine('mysql://root:password@localhost/cna330')
with engine.connect() as conn, conn.begin():
    df.to_sql('ign', conn, if_exists='replace')


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#
plt.title("Xbox")
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist") #plots the quantity of games with a specific rating for Xbox
plt.ylabel("Quantity")
plt.xlabel("Score")
plt.show()

plt.title("Playstation4")
reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist") #plots the quantity of games with a specific rating for Playstation4
plt.ylabel("Quantity")
plt.xlabel("Score")
plt.show()






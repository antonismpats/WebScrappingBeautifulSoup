#Scrape Russ stats
from bs4 import BeautifulSoup
import requests

#Make a request to access the basketball-reference site.
url = "https://www.basketball-reference.com/players/w/westbru01.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#Find the table with the Last five games based on the ID
table = soup.find(id='last5')
td = table.find_all('td')
name = soup.find('h1')

#Get the Player's surname and print it
player_name = name.get_text()
player_name = player_name.split(' ')[1]
print(player_name)

i=0
required = ['PTS', 'AST', 'TRB', 'STL', 'BLK']
dic = {'PTS':0, 'TRB':0, 'AST':0, 'STL':0, 'BLK':0}

for tdd in td:
    #Find the name of the stat and it's value
    stat = tdd.get('data-stat').upper()
    prop_stat = tdd.get_text()
    #Assign the new value to each stat
    if  stat in required:       
        dic[stat]=prop_stat
        i+=1
        if i==5:
            i=0
            result = "".join(f"{value}{key} " for key, value in dic.items())
            print(result)
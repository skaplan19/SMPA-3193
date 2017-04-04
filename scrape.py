import csv
import requests
import sys
from BeautifulSoup import BeautifulSoup

url = raw_input("http://m.nationals.mlb.com/player/605452/joe-ross")
r= requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data)


list_of_rows = []

for year in years: 
	print year
	response = requests.get("http://m.nationals.mlb.com/roster/transactions/2017/04")
	html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

for row in table.findAll('tr') [1:]:
    list_of_cells = []
    list_of_cells.append
    for cell in row.findAll('td'):
       list_of_cells.appendcell.text.encode
    list_of_rows.append(list_of_cells)
    

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text",])
writer.writerows(list_of_rows)

# Import libraries
import requests
import urllib.request
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://correlatesofwar.org/data-sets/national-material-capabilities'

# Connect to the URL .
source = requests.get(url)


# Parse HTML

html = urlopen("https://correlatesofwar.org/data-sets/national-material-capabilities").read()
soup = BeautifulSoup(html, 'html.parser')


#Creating and starting with the CSV for the eventual output:

f = csv.writer(open("COW_data_links.csv", "w"))
f.writerow(["Name", "Link"])

# Finding and adding relevant links to the csv

relevant_links = soup.find_all('a', attrs={'class':'summary url'})
for link in relevant_links:
    names = link.contents[0]
    fullLink = link.get('href')
    print(names)
    print(fullLink)
    f.writerow([names, fullLink])

# This creates a file with the relevant URLs and the names
# The next step is to download them automatically








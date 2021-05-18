
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


# Better understanding how to parse HTML and  trying two versions of the parsers

html = urlopen("https://correlatesofwar.org/data-sets/national-material-capabilities").read()
soup = BeautifulSoup(html, 'html.parser')
parsed_html = BeautifulSoup(html, 'lxml')

#Creating and starting with the CSV for the eventual output:

f = csv.writer(open("COW_data_links.csv", "w"))
f.writerow(["Name", "Link"])

# how to use find and find_all and what they produce.
# find_all gives me a list to work with, find just html

first_link_html = parsed_html.body.find('a', attrs={'class':'summary url'})
#print(first_link_html)
print()
all_links_attrs =  parsed_html.body.find_all('a', attrs={'class':'summary url'})
all_links_hrefs = parsed_html.body.find_all('a', href=True)
#print(all_links_hrefs)
#print(len(all_links_hrefs))
print()
#print(all_links_attrs)
#print(len(all_links_attrs))



# How to find the correct link?


# ATTEMPT 1

#this method to get the links I know doesn't work for some reason,
# I suspect because the list item is having so much junk.
# It's also not the best method. Ideally I'd like to download all files.
# But as these are represented as links in HTML I need to get all (relevant) links


for link in all_links_attrs:
    if link == "https://correlatesofwar.org/data-sets/national-material-capabilities/nmc-v4-data":
        relevant_links.append(link)


print()


#ATTEMPT 2 : WORKS partially
# Now I try to extract the links directly from HTML instead of creating a list first.

first_url = parsed_html.body.find('a', attrs={'class':'summary url'}).attrs['href']
print(first_url)

#now finding all links using the same method.. this breaks because of the list issue. Not sure how to fix this:

#for url in parsed_html.body.find_all('a', attrs={'class':'summary url'}).attrs['href']:
    #print(url)

# ATTEMPT 3: works completely
# took this from https://programminghistorian.org/en/lessons/intro-to-beautiful-soup

relevant_links = soup.find_all('a', attrs={'class':'summary url'})
for link in relevant_links:
    names = link.contents[0]
    fullLink = link.get('href')
    print(names)
    print(fullLink)
    f.writerow([names, fullLink])



print()











# Parse HTML and save to BeautifulSoup object¶ Maybe it is necessary to use 'lxml' instead of 'html.parser' depending on the HTML of the website
websitecontent = BeautifulSoup(source.text, "html.parser")



match = websitecontent.title.text
#print(match)

# How to find the files in my case... what type of filter do I need to apply to get a <a href="https://correlatesofwar.org/data-sets/national-material-capabilities/nmc-v5-1/at_download/file">
#
#                <img src="https://correlatesofwar.org/zip.png" alt="Zip archive icon">
#                 NMC_5_0.zip
#               </a>
# possible explanation here: https://www.kite.com/python/examples/4419/beautifulsoup-find-an-element-by-its-id

core_content = websitecontent.find(id='content-core')
#print(core_content.prettify())






#I can use it finding the div with class method too. In this source code the interesting content however is structure differently
headline = websitecontent.find('div', class_='item visualIEFloatFix').h2.a.text
print(headline)

#or use the core_content instead of course
subheading = core_content.div.div.h2.text
#print(subheading)

content = core_content.div.div.h3.text
#print(content)


# I can also use the find_all method, which returns a list instead of the first match that fits.
# This list then allows me to loop over. Here is a problem with locating the object maybe cuz of the find all or the loop???
# See the example at minute 19 here: https://www.youtube.com/watch?v=ng2o98k983k
# or it just repeats the first class_ item that is found and doesn't find all the others.... It runs through the loop 9 times, which is correct as there are 9 items but the result only is the first one.
# the problem seems to be because the first paragraph is structured differently. Need to figure that out

check = websitecontent.find_all('div', class_='item visualIEFloatFix')
#print(check)

all_links = websitecontent.find_all('a')




#for i in websitecontent.find_all('div', class_='item visualIEFloatFix'):
    #headline = check.h2.a.text
    #print(headline)

   # subheading = check.div.div.h2.text
    #print(subheading)

   # content = check.div.div.h3.text
    #print(content)
    #print()




# Import libraries
import requests
import urllib.request
from urllib.request import urlopen
import io
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://correlatesofwar.org/data-sets/national-material-capabilities'

# Connect to the URL
source = requests.get(url)

html = urlopen("https://correlatesofwar.org/data-sets/national-material-capabilities").read()
soup = BeautifulSoup(html, 'html.parser')
parsed_html = BeautifulSoup(html, 'lxml')
first_link_html = parsed_html.body.find('a', attrs={'class':'summary url'})
#print(first_link_html)
print()
all_links_html = parsed_html.body.find_all('a', attrs={'class':'summary url'})
#print(all_links_html)

relevant_links = []
for link in all_links_html:
    if link == "https://correlatesofwar.org/data-sets/national-material-capabilities/nmc-v4-data":
        print(link)

print()

print(len(all_links_html))







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



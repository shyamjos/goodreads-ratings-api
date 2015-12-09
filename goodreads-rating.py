import fnmatch
import os
import xml.etree.ElementTree as ET
import urllib2
import csv

# goodreads_key=
# ebooks_folder=

books = []
for root, dirs, files in os.walk('/home/shyam/Desktop/working-project/books'):
    for filename in files:
        if filename.endswith(('.pdf', '.mobi', '.epub')):
             title=os.path.splitext(filename)[0]
             books.append(( title))

for book in books:
    url="http://www.goodreads.com/book/title.xml?key=&title=" + book
    url = url.replace(' ', '%20')
    print "Fetching details for",book
    try:
        tree = ET.ElementTree(file=urllib2.urlopen(url))
        root = tree.getroot()
        root.tag, root.attrib
        title_books= root[1][1].text
        title_books=title_books[:50]
        # author_book = root[1][23][0][1].text
        year = root[1][7].text
        lang = root[1][11].text
        avg_rt = root[1][15].text
        pages = root[1][16].text
        # total_rt = root[1][14][5].text
        # total_rv = root[1][14][6].text
        with open('books.csv', 'a') as csvfile:
             fieldnames = ['Title', 'Author','Year','Language','Average-Rating','Pages','Total_Ratings','Total_Reviews']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
             # writer.writerow({'Title': title_books, 'Author': author_book, 'Year': year, 'Language': lang, 'Average-Rating':avg_rt, 'Pages':pages, 'Total_Ratings':total_rt, 'Total_Reviews':total_rv })
             writer.writerow({'Title': title_books, 'Year': year, 'Language': lang, 'Average-Rating':avg_rt, 'Pages':pages })
    except urllib2.HTTPError, e:
        print e.getcode()

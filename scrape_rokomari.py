from asyncore import write
import csv
import requests 
from bs4 import BeautifulSoup
from asyncore import write


target_url =["https://www.rokomari.com/book/category/410/science-fiction?ref=h_cl6","https://www.rokomari.com/book/category/410/science-fiction?ref=h_cl6&page=2"]
for page in range(1,2):

    req = requests.get(target_url+list(page)+("&"))

# print(req.status_code)
# print(req.content)

    soup = BeautifulSoup(req.content, "html.parser")
# print(soup)
    books= soup.find_all("div",class_ ="book-list-wrapper")
# print(books)

Book_list = []

for i in books:

    book_title = i.find("p",class_= "book-title").text
    book_author = i.find("p",class_= "book-author").text
    book_price = i.find("p",class_= "book-price").text
    book_dictionary = {
        "Title": book_title.strip(),
        "Author": book_author.strip(),
        "Price": book_price.strip()
    }
    # print(book_dictionary)
    Book_list.append(book_dictionary)

# print(Book_list)

Field_names = ["Title", "Author", "Price"]

with open("rokomari_science_data2.csv", "w") as rokomari_info:
    # writers =write(rokomari_info.handle_error())
    writers = csv.DictWriter(rokomari_info, fieldnames= Field_names)
    writers.writeheader()
    writers.writerows(Book_list)

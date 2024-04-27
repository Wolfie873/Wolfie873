import pymongo
import datetime
import tornado.ioloop
import tornado.web


from pymongo import MongoClient
from pyscript import document

client = MongoClient("mongodb://localhost:27017/")

db = client.bookstore
books_collection = db.books


def search_book(event):
        book_title = document.querySelector("#english")
        output_text = book_title.value
        output_div = document.querySelector("#output")
        output_div.innerText = output_text
        
        
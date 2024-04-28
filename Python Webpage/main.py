import pymongo
import asyncio
import tornado
import tornado.ioloop
import tornado.web
import pprint
import json
import io

from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.bookstore
books_collection = db.books
blue = books_collection.find_one({"title": "Blue"}, {"_id": 0})
books = db.books.find({}, {"_id": 0, "title": 1, "author": 1})

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("database.html", title="Database", books=books, blue=blue)
        
class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1> This is post 1</h1>")
        
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/home", HomeHandler)
        ],
        debug = True,
        autoreload = True)
    
if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listening on port {port}")
    # To start the server on the current thread
    tornado.ioloop.IOLoop.current().start()
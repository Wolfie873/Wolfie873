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

client = MongoClient("mongodb+srv://jortiz:Adm1n%40jl8733@testdb.7gw4rne.mongodb.net/?retryWrites=true&w=majority")
db = client.bookstore


class HelloHandler(tornado.web.RequestHandler):
    async def post(self):
        #Set Cookies
        self.set_cookie("title_name", "", expires_days=0)
        self.set_cookie("author_name", "", expires_days=0)
        self.set_cookie("pages", "", expires_days=0)
        self.set_cookie("rating", "", expires_days=0)
        
        #Initializing data dictionary
        input_data = {
                "title" : "",
                "author" : "",
                "pages" : 0,
                "rating" : 0
                }
        
        #Retrieve input data from POST request
        title_name = self.get_argument("title_name", "")
        author_name = self.get_argument("author_name", "")
        pages = self.get_argument("pages", "")
        rating = self.get_argument("rating", "")
        
        #Validate and process input data
        if title_name and author_name and pages and rating:
            
            #Convert pages and ratings to integers
            try:
                pages = int(pages)
                rating = int(rating)
            except ValueError:
                self.write("<p>Invalid input for pages and rating. Please try again</p>")
                return
            
            #Create input data for library
            input_data = {
                "title" : title_name,
                "author" : author_name,
                "pages" : pages,
                "rating" : rating
                }
            
            #Insert data into MongoDB
            db.books.insert_one(input_data)
        else:
            self.write("<p>Need data, please try again</p>")
            
        #Retreiving additional information for rendering the template
        blue = db.books.find_one({"title": "Blue"}, {"_id": 0})
        books = db.books.find({}, {"_id": 0, "title": 1, "author": 1})
        search = self.get_argument("book_title", "")
        book_search = db.books.find_one({"title": search}, {"_id": 0})
        
        # Render the template with input data and database contents
        self.render("database.html", title="Database", input_data=input_data, books=books, blue=blue, book_search=book_search)
        
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
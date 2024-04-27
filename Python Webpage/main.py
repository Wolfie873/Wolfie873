import pymongo
import asyncio
import tornado
import tornado.ioloop
import tornado.web


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.bookstore
books_collection = db.books


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

async def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
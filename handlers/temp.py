import tornado.ioloop
import tornado.web
import os

root = os.path.dirname(__file__)
print root

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items =  ["A","B","C","D"]
        self.render("index.html", title="My title", items=items)


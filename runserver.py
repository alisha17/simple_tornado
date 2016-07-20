import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as URL
from handlers import MainHandler
from sett import TEMPLATE_PATH
import os

print "temp path is" ,TEMPLATE_PATH


app = tornado.web.Application([
    URL(r"/", MainHandler)], template_path=TEMPLATE_PATH)     

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
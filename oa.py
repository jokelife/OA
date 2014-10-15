import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

class BaseHandler(tornado.web.Request):
  @porperty
  def db(self):
    conn mysql.connector.connection(username, password, host, port, dbname)
    return conn.cursor()
    
  def get_current_user(self):
    user_id = self.get_cookie("oa_user")
    if user_id:
      return None
    return self.db.execute("")
    
def main():
  pass

import bottle
import pymongo
import newsDAO
from bottle import static_file

@bottle.route('/')
def news_index():
    news_list = news.find_news()
    return bottle.template('index', dict(news = news_list))

@bottle.route('/comment', method='POST')
def insert_commet():
    comment = bottle.request.forms.get("comment")
    id = bottle.request.forms.get("id")
    news.insert_comment(comment, id)
    return bottle.redirect('/')


@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)

database = connection.web

news = newsDAO.NewsDAO(database)

bottle.debug(True)
bottle.run(host = 'localhost', port = 8082)
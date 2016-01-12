import string
from bson.objectid import ObjectId

class NewsDAO(object):

    def __init__(self, database):
        self.db = database
        self.news = database.news

    def find_news(self):
        l = []
        for each_news in self.news.find():
            l.append({'id': each_news['_id'], 'title': each_news['title'], 'text': each_news['text'], 'author': each_news['author'], 'image': each_news['image'], 'comments': each_news['comments']})

        return l

    def insert_comment(self, comment, id):
        news = self.news.update_one({"_id": ObjectId(id)}, {"$push": {"comments": comment}})
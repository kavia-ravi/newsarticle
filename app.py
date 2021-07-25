
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask import jsonify

#mongodb_client = MongoClient('mongodb://localhost:27017/theguardian')
#db = mongodb_client.db


app = Flask(__name__)
app.debug = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/theguardian"
mongo=PyMongo(app)

@app.route('/', methods = ['GET'])
def get_all_articles():
    try:
        articles = mongo.db.news_article.find()
        return dumps(articles)

        #return jsonify(temp)
    except Exception, e:
        return dumps({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

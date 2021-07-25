# newsarticle - Scrapy - MongoDB Pipeline
This is an application to crawl an online news website, e.g. www.theguardian.com/au using crawler framework [Scrapy] (http://scrapy.org/)
and build the application in Python to obtain only information relevant to the newsstory, e.g. article text, author, headline, article url, etc.

The data is stored in a hosted mongo database, e.g. compose.io/mongo, for subsequent search
and retrieval. 

Using MongoDB Compass to provides access to the content in the mongo database. 

The data from MongoDB is given access through a flask-Pymongo API
Currently, only a get-all[GET] data method is added.

OUTPUT :
Using postman get request:
![image](https://user-images.githubusercontent.com/28836650/126912024-5aee02fe-edd2-448c-9ca4-55a7a50a92e2.png)


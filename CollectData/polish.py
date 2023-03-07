import json
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

#Store Data in Mongo DB ==> Update Link to your own Database
client = MongoClient("mongodb+srv://DATABASE:Authcode@name.xxxxx.mongodb.net/?retryWrites=true&w=majority")
db = None
try:
    db = client.NewscraperDB
except ConnectionFailure:
   print("Server not available")    
collection = db.Articles

print('Connection to MongoDB Atlas established')


    
def checkForDuplicates (newArticles):
    print("Checking for duplicate Entries")
    articlesDatabase = collection.find()
    for row in articlesDatabase:
        id = row['id']
        for article in newArticles:
            idNewArticle = article ['id']
            if id == idNewArticle:
                newArticles.remove(article)
                print("Message: Article Already Exists")
    return newArticles


def polishAndStore(data):
    
    articles = json.loads(str(data))
    data_newArticles = articles['results']     

    #Check if some Articles from the recent API Call were already collected
    #newDataforDatabase() returns only Articles that havent been collected yet
    newDataforDatabase = checkForDuplicates(data_newArticles)

    counter = 0
    for article in newDataforDatabase:
        #Currencies are a List in the Article Json Format ==> Add them up and convert them into string to store in db
        article.setdefault('currencies')
        currencies = ""
        if article['currencies'] != None:
            for currency in article['currencies']:
                currencies = currencies + str(currency['title']) + " "

        data_dict = {'id': article['id'], 
                    'Domain' : article['domain'], 
                    'Source' : article['source']['title'],
                    'Title' : article['title'], 
                    'Date' : article['published_at'], 
                    'Slug' : article['slug'], 
                    'Currencies' : currencies, 
                    'URL' : article['url'],
                    'Created_at' : article['created_at'], 
                    'Language' : article['source']['region']}
        
        collection.insert_one(data_dict)
 
        counter += 1
        print('Message: New Article Nr.' + str(counter) +' added to Database')      
        
    
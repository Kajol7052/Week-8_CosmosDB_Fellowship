import json
import requests

url = "https://api.covid19india.org/raw_data.json"
r = requests.get(url)
#print(r.json())

import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
from pymongo import MongoClient
import datetime
import os
from bson.objectid import ObjectId


def run_sample():
    client = MongoClient("mongodb://crud-cosmosdb:5t1vUaoyE97UKvR97BnVXBgsOE9cMk7zV6GBfRz3m1Vu66ryb2uelPweAkMMBTVmkO0XhNw5zrjICqnwE7NE5A==@crud-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@crud-cosmosdb@")
    db = client['Covid_DB']
    con = db['Col_Covid']

def insert_collection():
        insert = r.json()['raw_data'][0:20]
        con.insert_many(insert)



def find_collection():
        print("Find one: " ,con.find_one({"nationality" : "India"}))
        print("Find all: " , con.find({"nationality" : "India"}))



def update_collection():
        #con.update_one({'_id': ObjectId("602c049259ec81b0f4baf46c")},  {'$set': {"author": "Google"}})
        myquery = { "statecode" : "KL", }
        newvalues = { "$set": { "statecode" : "KEL", } }
        con.update_one(myquery, newvalues)
        for x in con.find():
                print(x)


def delete_collection():
        myquery = { "patientnumber" : "9" }
        con.delete_one(myquery)
        #x =con.delete_many({}) this deletes all documents in collection
        #print(x.deleted_count, " documents deleted.")




#sort("name", 1) #ascending
#sort("name", -1) #descending
def sort_collection_by_age():
        mydoc = con.find().sort("agebracket")
        for x in mydoc:
                print(x)



#The limit() method takes one parameter, a number defining how many documents to return.
def limit():
        myresult = con.find().limit(5)
        for x in myresult:
                print(x)


def aggregation():
        agg_result= con.aggregate( 
        [{ 
        "$group" :  
                {"_id" : "$currentstatus",  
                "num_tutorial" : {"$sum" : 1} 
                }} 
        ]) 
        for i in agg_result: 
                print(i)
        print(con.count_documents( {} )) # count the no. of documents



if __name__ == '__main__':
    client = MongoClient("mongodb://crud-cosmosdb:5t1vUaoyE97UKvR97BnVXBgsOE9cMk7zV6GBfRz3m1Vu66ryb2uelPweAkMMBTVmkO0XhNw5zrjICqnwE7NE5A==@crud-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@crud-cosmosdb@")
    db = client['Covid_DB']
    con = db['Col_Covid']
    #run_sample()
    #limit()
    #sort_collection_by_age()
    #delete_collection()
    #insert_collection()
    #update_collection()
    #find_collection()
    aggregation()


import pandas

cursor = con.find()
#print ("total docs in collection:", con.count_documents( {} ))
#print ("total docs returned by find():", len(list(cursor)))
lis = list(cursor)
mongo_docs = lis[:50]
series_obj = pandas.Series({"a key":"a value"})
print ("series_obj:", type(series_obj))

series_obj = pandas.Series( {"one":"index"} )
series_obj.index = [ "one" ]
print ("index:", series_obj.index)

docs = pandas.DataFrame(columns=[])
for num, doc in enumerate( mongo_docs ):
    doc["_id"] = str(doc["_id"])       
    doc_id = doc["_id"]
    series_obj = pandas.Series( doc, name=doc_id )
    docs = docs.append( series_obj )
json_export = docs.to_json() # return JSON data
print ("\nJSON data:", json_export)
docs.to_json("object_rocket.json")
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
    client = MongoClient("MONGO_DB_CLIENT")
    db = client['DATABASE']
    con = db['CONTAINER']
    limit()
    sort_collection_by_age()
    delete_collection()
    insert_collection()
    update_collection()
    find_collection()
    aggregation()

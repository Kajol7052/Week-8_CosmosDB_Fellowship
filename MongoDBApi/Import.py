import pandas

cursor = con.find()
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
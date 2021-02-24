import azure.cosmos.cosmos_client as cosmos_client

with open('./temp/udfTax.js') as file:
    file_contents = file.read()
udf_definition = {
    'id': 'Tax',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(HOST, MASTER_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)
udf = container.scripts.create_user_defined_function(udf_definition)
print("UDF Created")

#results = list(container.query_items('SELECT * FROM Incomes t WHERE udf.Tax(t.income) > 20000'))
results = list(container.query_items({"query":"SELECT * FROM Incomes t WHERE udf.Tax(t.income) > 20000","parameters":{"enableCrossPartitionQuery":True}}))
#results = list(container.query_items({"query":"SELECT * FROM Incomes "}))

print(results)

import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
with open('./temp/trgPreValidateToDoItemTimestamp.js') as file:
    file_contents = file.read()

trigger_definition = {
    'id': 'trgPreValidateToDoItemTimestamp3',
    'serverScript': file_contents,
    'triggerType': documents.TriggerType.Pre,
    'triggerOperation': documents.TriggerOperation.All
}
client = cosmos_client.CosmosClient(HOST, MASTER_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)
trigger = container.scripts.create_trigger(trigger_definition)

import uuid

new_id= str(uuid.uuid4())
item = {'id':new_id,'category': 'Personal', 'name': 'Groceries',
        'description': 'Pick up hello', 'isComplete': False}
container.create_item(item, {'pre_trigger_include': 'trgPreValidateToDoItemTimestamp2'})
from pymongo import MongoClient

def extract_mongodb_schema(uri):
    client = MongoClient(uri)
    databases = client.list_database_names()
    schema = {}

    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()
        schema[db_name] = {}

        for collection in collections:
            sample_document = db[collection].find_one()
            schema[db_name][collection] = list(sample_document.keys()) if sample_document else []

    return schema

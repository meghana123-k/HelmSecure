from mongo import violations_collection

violations_collection.insert_one({"test": "mongodb working"})

print("Inserted Successfully")

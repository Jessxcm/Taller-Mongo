from pymongo import MongoClient
con = MongoClient()
db = con["bd03"] # reemplace X por el número que corresponde a su usuario
db.authenticate("bd03", "$bd03!", "admin")

coll = db["Movies2"]

#pruebadeclonar
doc = {}
doc["Title"] = "Twelve Monkeys"
doc["Year"] = 1995
doc["Runtime"] = "129 min"
doc["Directors"] = ["Terri Gilliam"]
db.Movies2.insert_one(doc)

for movie in db.Movies2.find():
    print (movie)


from connection import datetime,db


#------------------------------------
#Punto A : listar los mensajes puestos en el año 2020 y que no han tenido respuesta
#------------------------------------

#Query en el shell:
#db.Tweets.find( { $and: [ {"created_date": {$gte: ISODate("2020-01-01T00:00:00.000Z"),$lt: ISODate("2021-01-01T00:00:00.000Z"),}}, { "responses": { $eq: 2 } } ] } )

#Pymongo
query= {"$and": [ {"created_date": {"$gte": datetime.datetime(2020,1,1),"$lt": datetime.datetime(2021,1,1) ,}}, { "responses": { "$eq": 2 } } ]}

print ("\n")
print ("Resultado punto A: \n")
for tweets in db.Tweets.find(query):
    print (tweets)
print ("\n")
from connection import datetime,db


#------------------------------------
#Punto B :Listar los mensajes puestos en el año 2020 y que tienen 10 o más re-envíos
#------------------------------------

#Query en el shell:
#db.Tweets.find( { $and: [ {"created_date": {$gte: ISODate("2020-01-01T00:00:00.000Z"),$lt: ISODate("2021-01-01T00:00:00.000Z"),}}, { "retweets": { $gte: 5 } } ] } )


#Pymongo
query= { "$and": [ {"created_date": {"$gte": datetime.datetime(2020,1,1),"$lt": datetime.datetime(2021,1,1) ,}}, { "retweets": { "$gte": 5 } } ] }

print ("\n")
print ("Resultado punto B: \n")
for tweets in db.Tweets.find(query):
    print (tweets)
print ("\n")

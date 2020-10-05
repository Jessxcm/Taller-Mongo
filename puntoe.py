from connection import db

#------------------------------------
#Punto E: Encontrar el usuario que tiene mayor promedio en la cantidad de reenvío (re-tweets) de sus mensajes
#------------------------------------


#Query en el shell:
""" db.Tweets.aggregate( 
    [ 
        {
            $group : {
                _id : "$author",
                avg_total :  {$avg:"$retweets"}
            }
        },
        {
            $group : {
                _id: null,
                maxtotal : { $max: "$avg_total" },
                fullDocument : {$push:"$$ROOT"}
            }
        },
        {
            $unwind : "$fullDocument"
        },
        {
            $project : {
                _id : 0,
                username: "$fullDocument._id",
                prom_retweets : "$fullDocument.avg_total",
                isMaximo: { $eq : ["$fullDocument.avg_total","$maxtotal"]} 
            }
        },
        {
            $match : { isMaximo: true}
        }
    ] 
)
 """

#Pymongo
pipeline = [
            {
            '$group' : {
                '_id' : "$author",
                'avg_total' :  {'$avg':"$retweets"}
            }
        },
        {
            '$group' : {
                '_id': 'null',
                'maxtotal' : { '$max': "$avg_total" },
                'fullDocument' : {'$push':"$$ROOT"}
            }
        },
        {
            '$unwind' : "$fullDocument"
        },
        {
            '$project' : {
                '_id' : 0,
                'username': "$fullDocument._id",
                'prom_retweets' : "$fullDocument.avg_total",
                'isMaximo': { '$eq' : ["$fullDocument.avg_total","$maxtotal"]} 
            }
        },
        {
            '$match' : { 'isMaximo': True}
        }
 ]


print ("\n")
print ("Punto E: \n")
result = db.Tweets.aggregate(pipeline)
print (list(result))
print ("\n")
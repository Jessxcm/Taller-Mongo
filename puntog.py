from connection import db

#------------------------------------
#Punto G: Encontrar los usuarios que tienen mas seguidores que el promedio de seguidores que tienen los usuarios
#------------------------------------


#En el shell

""" db.Users.aggregate( 
    [ 
        {
            $group : {
                _id: null,
                avg_total :  {$avg:"$followers_counter"},
                fullDocument : {$push:"$$ROOT"}
            }
        }, 
        {
            $unwind : "$fullDocument",
        },
        {
            $addFields: {
                isMayor: { $gt: ["$fullDocument.followers_counter", "$avg_total" ] }
            }   
        },
        {
            $match : { isMayor : true}
        },

        {
            $project : {
                _id: 0,
                avg_total: 0,
                isMayor:0
            }
        }
    ] 
) """


#Pymongo
 
pipeline=[
            {
            '$group' : {
                '_id': 'null',
                'avg_total' :  {'$avg':"$followers_counter"},
                'fullDocument' : {'$push':"$$ROOT"}
            }
        }, 
        {
            '$unwind' : "$fullDocument",
        },
        {
            '$addFields': {
                'isMayor': { '$gt': ["$fullDocument.followers_counter", "$avg_total" ] }
            }   
        },
        {
            '$match' : { 'isMayor' : True}
        },
        {
            '$project' : {
                '_id': 0,
                'avg_total': 0,
                'isMayor':0
            }
        }
]

print ("\n")
print ("Punto G: \n")
result = db.Users.aggregate(pipeline)
print (list(result))
print ("\n")

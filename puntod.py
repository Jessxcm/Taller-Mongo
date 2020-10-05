from connection import db


#------------------------------------
#Punto D : Encontrar para cada usuario el promedio de mensajes que escribe por mes
#------------------------------------

#Query en el shell:
""" db.Tweets.aggregate( 
    [ 
        {
            $group : {
                _id :  {$month: "$created_date"} ,
                cantidad : {$sum:1},
                fullDocument : {$push:"$$ROOT"}
            }
        },
        {
                $unwind : "$fullDocument",
        },
        {
            $group : {
                _id : "$fullDocument.author",
                promedio : { $avg : "$cantidad"}

            }
        } 
    ] 
) """


#Pymongo

pipeline = [
            {
            '$group' : {
                '_id' :  {'$month': "$created_date"} ,
                'cantidad' : {'$sum':1},
                'fullDocument' : {'$push':"$$ROOT"}
            }
        },
        {
                '$unwind' : "$fullDocument",
        },
        {
            '$group' : {
                '_id' : "$fullDocument.author",
                'promedio' : { '$avg' : "$cantidad"}

            }
        }
]


print ("\n")
print ("Punto D: \n")
result = db.Tweets.aggregate(pipeline)
print (list(result))
print ("\n")
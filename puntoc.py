from connection import db


#------------------------------------
#Punto C : Encontrar el (los) usuario(s) que tiene(n) el mayor número de seguidores
#------------------------------------
#Query en el shell:
""" db.Users.aggregate( [ 
    {
        $group : {
            _id: null,
            maxtotal : { $max: "$followers_counter" },
            fullDocument : {$push:"$$ROOT"}
        },
    },
    {
        $unwind : "$fullDocument"
    },
    {
        $addFields: {
            isMax: { $eq : ["$fullDocument.followers_counter","$maxtotal"]} 
            }   
    },
    {
        $match : { isMax : true}
    }
]) """

#Pymongo

pipeline= [
        {
        '$group' : {
            '_id': 'null',
            'maxtotal' : { '$max': "$followers_counter" },
            'fullDocument' : {'$push':"$$ROOT"}
        },
    },
    {
        '$unwind' : "$fullDocument"
    },
    {
        '$addFields': {
            'isMax': { '$eq' : ["$fullDocument.followers_counter","$maxtotal"]} 
            }   
    },
    {
        '$match' : { 'isMax' : True}
    }
]

print ("\n")
print ("Punto C: \n")
result = db.Users.aggregate(pipeline)
print (list(result))
print ("\n")
from connection import datetime,db

#------------------------------------
#Extraer los datos de la base de datos
#------------------------------------

#recorriendo el query para obtener todos los datos de la base de datos
#for user in db.Users2.find():
    #print (user)

#for tweets in db.Tweets2.find():
    #print (user)


#Entrada a la aplicacion

#1. Los últimos 10 mensajes que el usuario ha publicado, en orden cronológico, empezando por el más reciente. Si son réplicas, indica el mensaje original y el usuario que lo publicó. Si son mensajes re-enviados, indica el usuario que publicó el mensaje original.
""" db.UsersTweets.aggregate( 
    [ 
        {
            $match : { creator : "rcator1@hubpages.com"}
        },
        {
            $sort : { fecha : -1 }
        },
        {
            $limit : 10
        },
        {
            $project : {
                creator: 0,
                _id:0
            }
        }
    ] 
) """

#pymongo

pipeline=[
            {
            '$match' : { 'creator' : "rcator1@hubpages.com"}
        },
        {
            '$sort' : { 'fecha' : -1 }
        },
        {
            '$limit' : 10
        },
        {
            '$project' : {
                'creator': 0,
                '_id':0
            }
        }
]


print ("\n")
print ("entrando a la aplicación: \n")
print ("usuario: rcator1@hubpages.com \n")

print ("mensajes propios de rcator1@hubpages.com \n")
for result in db.UsersTweets.aggregate(pipeline):
    print ("tipo mensaje : ",result['type_message'])
    print ("fecha : ",result['fecha'])
    print ("contenido : ",result['content'])
    if result['type_message']!="original":
        print ("original de : ",result['from'])
    print ("--------------------------------------")


#2. Los últimos 5 mensajes que han publicado cada uno de los usuarios a los que sigue, agrupados por el usuario que los publica. Los usuarios deben estar en orden alfabético y, los mensajes de cada usuario, en orden cronológico, empezando por el más reciente.

for user in db.Users.find({ "username": "rcator1@hubpages.com" }):
    for seguidos in user['following']:
        cmd = seguidos['username']
        pipeline=[
            {
                '$match' : { 'creator' : cmd}
            },
            {
                '$sort' : { 'fecha' : -1 }
            },
            {
                '$limit' : 5
            },
            {
                '$project' : {
                                'creator': 0,
                                '_id':0
                            }
            }
        ]
        print ("====================================================================================================")
        print ("mensajes de usuario seguido:  ", cmd)
        print ("====================================================================================================")
        for result in db.UsersTweets.aggregate(pipeline):
            print ("tipo mensaje : ",result['type_message'])
            print ("fecha : ",result['fecha'])
            print ("contenido : ",result['content'])
            if result['type_message']!="original":
                print ("original de : ",result['from'])
            print ("--------------------------------------")
        print ("\n")






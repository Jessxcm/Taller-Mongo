from connection import datetime,db


#------------------------------------
#Punto F: Encontrar para cada mes del año 2020, el(los) usuarios que escribieron la mayor cantidad de mensajes
#------------------------------------

""" db.Tweets.aggregate( 
    [ 
        {
            $match : {
                created_date : {
                    $gte: ISODate("2020-01-01T00:00:00.000Z"),
                    $lt : ISODate("2021-01-01T00:00:00.000Z")
                }
            }
        },
        {
            $group : {
                _id: { Month: { $month: "$created_date"}, username : "$author" },
                total_Tweets_User_Mes : {$sum:1}
            }
        },
        {
            $group : {
                _id : "$_id.Month",
                maxTweetsMes : { $max: "$total_Tweets_User_Mes" },
                users : {
                $push : {username: "$_id.username", totalTweets: "$total_Tweets_User_Mes"}     
                } 
            }
        },
        {
            $project : {
                _id:0,
                Month: "$_id",
                maxTweets:"$maxTweetsMes",
                users : {
                    $filter : {
                        input: "$users",
                        as : "user",
                        cond : { $eq : ["$$user.totalTweets","$maxTweetsMes"]}
                    }
                }
            }
        },
        {
            $sort : {
                Month : 1
            }
        }
    ] 
) """




#Pymongo

pipeline=[        {
            '$match' : {
                'created_date' : {
                    '$gte': datetime.datetime(2020,1,1),
                    '$lt' : datetime.datetime(2021,1,1)
                }
            }
        },
        {
            '$group' : {
                '_id': { 'Month': { '$month': "$created_date"}, 'username' : "$author" },
                'total_Tweets_User_Mes' : {'$sum':1}
            }
        },
        {
            '$group' : {
                '_id' : "$_id.Month",
                'maxTweetsMes' : { '$max': "$total_Tweets_User_Mes" },
                'users' : {
                '$push' : {'username': "$_id.username", 'totalTweets': "$total_Tweets_User_Mes"}     
                } 
            }
        },
        {
            '$project' : {
                '_id':0,
                'Month': "$_id",
                'maxTweets':"$maxTweetsMes",
                'users' : {
                    '$filter' : {
                        'input': "$users",
                        'as' : "user",
                        'cond' : { '$eq' : ["$$user.totalTweets","$maxTweetsMes"]}
                    }
                }
            }
        },
        {
            '$sort' : {
                'Month' : 1
            }
        }]

print ("\n")
print ("Punto F: \n")
result = db.Tweets.aggregate(pipeline)
print (list(result))
print ("\n")
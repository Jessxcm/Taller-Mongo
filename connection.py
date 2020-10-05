#importanto librerias
from pymongo import MongoClient
import datetime
#conexion a la base de datos
con = MongoClient()
db = con["bd03"] #conectarse a una base de datos
db.authenticate("bd03", "$bd03!", "admin")


#------------------------------------
#Colecciones
#------------------------------------

usuarios = db['Users'] #datos de los usuarios
mensajes = db['Tweets'] #mensajes de los usuarios
UsersTweets = db['UsersTweets'] #relacion entre usuarios y mensajes


#------------------------------------
#Declarar los datos de la base de datos
#------------------------------------
#ejemplos de datos (Users)
user1 = {"username":"lgreenlees0@china.com.cn","password":"BQYajNYNgmVl","profile_type":"private","city":"El Quebrachal","country":"Argentina","following":[{"username":"lgreenlees0@china.com.cn"},{"username":"alavrick5@disqus.com"},{"username":"pharmeston7@com.com"},{"username":"aclappisont@examiner.com"},{"username":"aclappisont@examiner.com"}],"followers":[{"username":"rmetzingm@chronoengine.com"},{"username":"chempshall6@gizmodo.com"},{"username":"fmcorkilq@livejournal.com"},{"username":"alavrick5@disqus.com"}],"followers_counter":4,"following_counter":5}

#ejemplos de datos (Tweets)
tweet1 = {"id":1,"author":"jcowope9@mozilla.org","created_date":"2015-12-12T21:03:14Z","content":"duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices","retweets_list":[{"username":"ainfantino1@ameblo.jp","date":"2020-07-03T06:18:31Z"},{"username":"bjeavonsf@ask.com","date":"2020-01-20T22:18:27Z"},{"username":"sendsa@gravatar.com","date":"2020-08-15T22:55:55Z"},{"username":"eveaseyl@sogou.com","date":"2019-07-23T07:12:30Z"},{"username":"fmcorkilq@livejournal.com","date":"2019-09-23T13:32:15Z"}],"responses_list":[{"username":"zsollowayi@marketwatch.com","date":"2020-02-17T17:04:43Z","content":"pretium iaculis diam erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam"},{"username":"aclappisont@examiner.com","date":"2020-07-24T13:10:09Z","content":"mauris ullamcorper purus sit amet nulla quisque arcu libero rutrum ac lobortis vel"},{"username":"eveaseyl@sogou.com","date":"2020-07-04T16:51:57Z","content":"leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor"}],"retweets":5,"responses":3}

#ejemplos de datos (UsersTweets)
UserTweets1 = {"creator": "fmaccurtain0@bbc.co.uk", "type_message": "retweet","fecha": "2020-02-02T00:52:25Z","content": "lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti","from": "dizakov3@go.com"}
from pymongo import MongoClient
db = 0
def connect_Mongo():
	client = MongoClient("mongodb://rejuntis:uergs123@juntis-shard-00-00-gwz7q.mongodb.net:27017,juntis-shard-00-01-gwz7q.mongodb.net:27017,juntis-shard-00-02-gwz7q.mongodb.net:27017/test?ssl=true&replicaSet=Juntis-shard-0&authSource=admin",
		ssl = True)
	global db	
	db = client.test

def insert_Aluno(nome,cpf,nasc,ingr,curso,fingr):
	result = db.test.insert_one(
		{
			"Nome"		:	nome,
			"Ingresso"	:	ingr,
			"Forma de Ingresso"		:	fingr,
			"Curso"		:	curso,
			"CPF"		:	cpf,
			"Data Nasc"	:	nasc
		})
connect_Mongo()
insert_Aluno("oi2","13111","19/19/91","2121/1","E2NG","2SISU")
cursor = db.test.find()
for document in cursor:
	print(document)
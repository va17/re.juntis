# -*- coding: utf-8 -*-
import os, time, sys, csv
def connect_Mongo():
+	client = MongoClient("mongodb://rejuntis:uergs123@juntis-shard-00-00-gwz7q.mongodb.net:27017,juntis-shard-00-01-gwz7q.mongodb.net:27017,juntis-shard-00-02-gwz7q.mongodb.net:27017/test?ssl=true&replicaSet=Juntis-shard-0&authSource=admin",
+		ssl = True)
+	global db	
+	db = client.test
+	global db_Disc
+	db_Disc = client.Professores 
+
+#Função que insere os professores no banco;
+def insert_Professor(nome,disciplina,horarios,pesquisas):
+	result = db.test.insert_one(
+		{
+			"Nome"			:	nome,
+			"disciplina"	:	disciplina,
+			"Horários"		:	horarios,
			"Pesquisas"		:	pesquisas
+		})
+	print(nome," inserido com sucesso!")

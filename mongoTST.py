from pymongo import MongoClient
import os, time, sys, csv,io,codecs,re
db = 0

def Menu():
	print("-----------MENU REJUNTIS-----------")
	print("\t1) Listar Aluno;")
	print("\t2) Listar Disciplinas;")
	print("\t3) Inserir Aluno;")
	print("\t4) Inserir Disciplina;")
	print("\t5) Pesquisar Aluno;")
	print("\t6) Pesquisar Disciplina;")
	op = input("\nDigite uma das opções:")
	print(op)



def connect_Mongo():
	client = MongoClient("mongodb://rejuntis:uergs123@juntis-shard-00-00-gwz7q.mongodb.net:27017,juntis-shard-00-01-gwz7q.mongodb.net:27017,juntis-shard-00-02-gwz7q.mongodb.net:27017/test?ssl=true&replicaSet=Juntis-shard-0&authSource=admin",
		ssl = True)
	global db	
	db = client.test
	global db_Disc
	db_Disc = client.Discplinas 

def insert_Aluno(nome,cpf,nasc,ingr,curso,fingr,aprov):
	result = db.test.insert_one(
		{
			"Nome"		:	nome,
			"Ingresso"	:	ingr,
			"Forma de Ingresso"		:	fingr,
			"Curso"		:	curso,
			"CPF"		:	cpf,
			"Data Nasc"	:	nasc,
			"Aprovadas"	:	aprov
		})
	print("Objeto inserido com sucesso!")

def insert_Disciplina(nome,cred,horas,prio):
	result = db_Disc.Discplinas.insert_one(
		{
			"Nome"			:	nome,
			"Créditos"		:	cred,
			"CH"			:	horas,
			"Prioridade"	:	prio
		})
	print("Objeto inserido com sucesso!")

def list_Aluno():
	cursor = db.test.find()
	if cursor.count() == 0:
		print("Sem Registros no Banco!")
	else:	
		for document in cursor:	
			print(document)

def list_Disciplinas():
	cursor = db_Disc.Discplinas.find()
	if cursor.count() == 0:
		print("Sem Registros no Banco!")
	else:	
		for document in cursor:	
			print(document)

def aluno_removeAll():
	db.test.remove()			

def disciplina_removeAll():
	db_Disc.Discplinas.remove()

def open_Disciplinas():
	#lista = os.listdir("C:/Users/Dymytry/Desktop/CSVs")# pega os nomes dos arquivos na pasta
	#global csvs
	#csvs = [arq for arq in lista if arq.lower().endswith(".csv") and arq != 'disciplinas0.csv']# pega os nomes dos arquivos que são CSVs
	#curso = []
	with open("C:/Users/Dymytry/Desktop/disciplinas0.csv",  "r", encoding="utf-8") as disciplinas:
		read = csv.reader(disciplinas)   
		for linha in read:
			#print(linha)
			#curso.append(linha[0])
			insert_Disciplina(linha[0],linha[1],linha[3],linha[4])#Descomentar depois#
			#TESTES do CSV
			#print(linha[0])
			#print(linha[1])
			#print(linha[2])
			#print(linha[3])
			#print(linha[4])					

def set_Arq():
	global lista
	lista = os.listdir("C:/Users/Dymytry/Desktop")# pega os nomes dos arquivos na pasta
	global csvs
	csvs = [arq for arq in lista if arq.lower().endswith(".csv") and arq != 'disciplinas0.csv']

def open_Aluno():
	#set_Arq()
	for x in range(0,len(csvs)):# para cada arquivo, gerar um novo arquivo somente com o que interessa
		nome_arq = csvs[x]
		nome_arq_new_temp = csvs[x]
		aluno = []
		nome_arq_new = nome_arq_new_temp.replace('.csv','-new.csv')# acrescenta um número no nome do aluno para não sobrescrever o arquivo original
		#target = open(nome_arq_new,'w',encoding="latin-1")
		aprovadas = []
		#reprovadas = []
		#cursando = []
		#pendentes = []
		with open(nome_arq_new, "r",encoding='latin-1') as arquivo:
			print(arquivo)
			reader = csv.reader(arquivo)   
			cont = 0
			for linha in reader:
				i=0
				while(i < len(linha) and cont<6):
					if linha[i].startswith('Nome') == True or linha[i].startswith('CPF') == True or linha[i].startswith('Nascimento') == True or linha[i].startswith('Curso') == True or linha[i].startswith('Forma de') == True or linha[i].startswith('Ano/') == True:
						#aluno.append(linha[i])
						#r = re.search('(?<=: \w+',linha[i])
						#print(r)
						#r.group(0)
						#print(r)
						#result = linha[i].replace(r.group(0),"")
						#print(result)
						print(re.search('.+?[:]+\W',linha[i]))
						print(re.sub(".+?[:]+\W","",linha[i]))
						#print(r)
						aluno.append(re.sub(".+?[:]+\W","",linha[i]))
						print(aluno)
						#target.write(linha[i])
						#target.write("\n")
						cont += 1										
					i += 1
			arquivo.seek(0)

			for linha in reader:
				i=0
				while(i < len(linha)):
					print("AQUI")
					print(linha[0])
					if linha[2] == "A" or linha[2] == "B" or linha[2] == "C":
						#target.write(linha[0])
						#target.write(",")
						#target.write(linha[2])
						#target.write(",")
						#target.write(linha[i-1])
						#target.write("\n")
						print(linha[0])	
						print(linha[1])	
						print(linha[2])
						aprovadas.append(linha[2])
						#print(aprovadas[i])
					i += 1
			#print(aprovadas)				
			#Descomentar depois#insert_Aluno(aluno[0],aluno[1],aluno[2],aluno[5],aluno[4],aluno[3],aprovadas)			


##TESTES DAS FUNÇÕES CRIADAS##
connect_Mongo()
set_Arq()
Menu()
#insert_Aluno("0","0","0","0","0","0","0")
#aluno_removeAll()
#open_Disciplinas()
#open_Aluno()
#list_Aluno()

#list_Disciplinas()
#disciplina_removeAll()
#list_Disciplinas()
#db2.test2.remove()
#list_Disciplinas()
##TESTES DAS FUNÇÕES CRIADAS##
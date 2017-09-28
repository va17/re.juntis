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
	print("\t7 Aluno")
	print("\t8 Disciplinas")
	op = input("\nDigite uma das opções:")
	if op == "1":
		list_Aluno()
	elif op == "2":
		list_Disciplinas()
	elif op == "3":
		open_Aluno()
	elif op == "4":
		open_Disciplinas()
	elif op == "5":
		print("5")
		opp = input("\nDigite o CPF do aluno:")
		find_Aluno(opp)
	elif op == "6":	
		print("6")
	elif op == "7":
		aluno_removeAll()
	elif op == "8":
		disciplina_removeAll()
	else:	
		print(op)
		sys.exit(0)

	Menu()	


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

def insert_Disciplina(nome,cred,horas,prio,semestre):
	result = db_Disc.Discplinas.insert_one(
		{
			"Nome"			:	nome,
			"Créditos"		:	cred,
			"CH"			:	horas,
			"Prioridade"	:	prio,
			"Semestre"		:	semestre
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

def find_Aluno(cpf):
	cursor = db.test.find({"CPF" : cpf})
	if cursor.count == 0:
		print("Nenhum registro encontrado!")
	else:
		for document in cursor:
			print(document)	

def find_Disciplina(nome):
	cursor = db_Disc.Discplinas.find({"Nome"})	

def aluno_removeAll():
	db.test.remove()
	print("BOOOM")			

def disciplina_removeAll():
	db_Disc.Discplinas.remove()
	print("BOOOM")

def open_Disciplinas():
	with open("C:/Users/Dymytry/Desktop/disciplinas0.csv",  "r", encoding="utf-8") as disciplinas:
		read = csv.reader(disciplinas)   
		for linha in read:
			linha[0] = linha[0].replace('\ufeff','')
			insert_Disciplina(linha[0],linha[1],linha[3],linha[4],linha[5])				

def set_Arq():
	global lista
	lista = os.listdir("C:/Users/Dymytry/Desktop")# pega os nomes dos arquivos na pasta
	global csvs
	csvs = [arq for arq in lista if arq.lower().endswith("-new.csv") and arq != 'disciplinas0.csv']

def open_Aluno():
	#set_Arq()
	for x in range(0,len(csvs)):# para cada arquivo, gerar um novo arquivo somente com o que interessa
		nome_arq = csvs[x]
		nome_arq_new_temp = csvs[x]
		aluno = []
		nome_arq_new = nome_arq_new_temp.replace('.csv','-new.csv')# acrescenta um número no nome do aluno para não sobrescrever o arquivo original
		aprovadas = []
		with open(nome_arq, "r",encoding='utf-8') as arquivo:
			print(arquivo)
			reader = csv.reader(arquivo)   
			cont = 0
			for linha in reader:
				i=0
				while(i < len(linha) and cont<6):
					if linha[i].startswith('Nome') == True or linha[i].startswith('CPF') == True or linha[i].startswith('Nascimento') == True or linha[i].startswith('Curso') == True or linha[i].startswith('Forma de') == True or linha[i].startswith('Ano/') == True:
						print(re.search('.+?[:]+\W',linha[i]))
						print(re.sub(".+?[:]+\W","",linha[i]))
						#print(r)
						aluno.append(re.sub(".+?[:]+\W","",linha[i]))
						print(aluno)
						cont += 1											
					i += 1
			arquivo.seek(0)
			print("!!! AQUI 2 !!!")
			d = {}
			dlist = []	
			for linha in reader:
				if len(linha) < 3:
					print("PULEI")
				else:	
					i=0
					while(i < len(linha)):
						if linha[i] == "A" or linha[i] == "B" or linha[i] == "C":
							d['Cadeira'] = linha[i-1]
							d['Conceito'] = linha[i]
							dlist.append(d.copy())
							print(d)							
						i += 1
			print(dlist)
			insert_Aluno(aluno[0],aluno[1],aluno[2],aluno[5],aluno[4],aluno[3],dlist)#Descomentar depois#			


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
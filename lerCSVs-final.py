# -*- coding: utf-8 -*-
import os, time, sys, csv,io,codecs
def gera_csvs():
	pass
	lista = os.listdir("C:/Users/Dymytry/Desktop")# pega os nomes dos arquivos na pasta
	csvs = [arq for arq in lista if arq.lower().endswith(".csv") and arq != 'disciplinas0.csv']# pega os nomes dos arquivos que são CSVs
	curso = []
	with open("C:/Users/Dymytry/Desktop/disciplinas0.csv",  "r", encoding="latin-1") as disciplinas:#Alterei esta linha
		read = csv.reader(disciplinas)   
		for linha in read:
			curso.append(linha[0])
			print(linha[0])# TESTE

	for x in range(0,len(csvs)):# para cada arquivo, gerar um novo arquivo somente com o que interessa

		nome_arq = csvs[x]
		nome_arq_new_temp = csvs[x]
		nome_arq_new = nome_arq_new_temp.replace('.csv','new.csv')# acrescenta um número no nome do aluno para não sobrescrever o arquivo original
		target = open(nome_arq_new,"w",encoding="utf-8")
		aprovadas = []
		reprovadas = []
		cursando = []
		pendentes = []
		with open(nome_arq, "r",encoding='utf-8') as arquivo:
			reader = csv.reader(arquivo)   
			cont = 0
			for linha in reader:
				i=0
				while(i < len(linha) and cont<6):
					if linha[i].startswith('Nome') == True or linha[i].startswith('CPF') == True or linha[i].startswith('Nascimento') == True or linha[i].startswith('Curso') == True or linha[i].startswith('Forma de') == True or linha[i].startswith('Ano/') == True:
						target.write(linha[i])
						target.write("\n")
						print(linha[i])
						cont += 1
					i += 1
			arquivo.seek(0)

			for linha in reader:
				i=0
				while(i < len(linha)):
					if linha[i] == "APROVADO":
						target.write(linha[0])
						target.write(",")
						target.write(linha[2])
						target.write(",")
						target.write(linha[i-1])
						target.write("\n")
						aprovadas.append(linha[2])
						#print(linha[2])
					i += 1
			print(len(aprovadas))
	# Fim do laço for
			arquivo.seek(0)

			for linha in reader:
				k=0
				while(k < len(linha)):
					if linha[k] == "REPROVADO":
						target.write(linha[0])
						target.write(",")
						target.write(linha[2])
						target.write(",")
						target.write(linha[k-1])
						target.write("\n")
						reprovadas.append(linha[2])
					k += 1
	# Fim do laço for
			arquivo.seek(0)

			for linha in reader:
				j=0
				while(j < len(linha)):
					if linha[j] == "MATRICULADO":
						target.write(linha[0])
						target.write(",")
						target.write(linha[2])
						target.write(",")
						target.write(linha[j])
						target.write("\n")
						cursando.append(linha[2])
					j += 1
	# Fim do laço for # 
	pendentes = list(set(curso)-set(aprovadas))

	print ('Curso:\n')					
	print(curso)	
	print ('Aprovadas:\n')					
	print(aprovadas)	
	print ('Reprovadas:\n')					
	print(reprovadas)	
	print ('Cursando:\n')	
	print(cursando)
	print ('Pendentes:\n')	
	print(pendentes)
	print ('Pronto') # Fim da função gera_csvs
gera_csvs()

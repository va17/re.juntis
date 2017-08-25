# -*- coding: utf-8 -*-
import os, time, sys, csv

lista = os.listdir('/home/miguel/Documentos/programasPython')# pega os nomes dos arquivos na pasta
#print lista
csvs = [arq for arq in lista if arq.lower().endswith(".csv")]# pega os nomes dos arquivos que são CSVs
#print csvs
#nome_arq = 'Ana.csv'
for x in xrange(0,len(csvs)):# para cada arquivo, gerar um novo arquivo somente com o que interessa
	#print x
	#print len(lista)
	nome_arq = csvs[x]
	#print nome_arq
	nome_arq_new_temp = csvs[x]
	nome_arq_new = nome_arq_new_temp.replace('.csv','-new.csv')# acrescenta '-new' no nome do aluno para não sobrescrever o arquivo original
	#print nome_arq_new
	target = open(nome_arq_new,'w')
	with open(nome_arq, 'rb') as arquivo:
		reader = csv.reader(arquivo)   
		cont = 0
		for linha in reader:
			i=0
			while(i < len(linha) and cont<6):
				if linha[i].startswith('Nome') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1
				if linha[i].startswith('CPF') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1     
				if linha[i].startswith('Nascimento') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1
				if linha[i].startswith('Curso') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1
				if linha[i].startswith('Forma de') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1
				if linha[i].startswith('Ano/') == True:
					#print linha[i]
					target.write(linha[i])
					target.write("\n")
					cont += 1
				i += 1
		arquivo.seek(0)

		for linha in reader:
			i=0
			while(i < len(linha)):
				if linha[i] == "APROVADO" or linha[i] == "REPROVADO":
					target.write(linha[0])
					target.write(",")
					target.write(linha[2])
					target.write(",")
					target.write(linha[i-1])
					target.write("\n")
					#print linha[0]+' '+linha[2]+' <---> '+linha[i-1]
				i += 1
# Fim do laço for
print 'Pronto'

#		conceitos = ['A','B','C']
#		cadeiras = ['ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA (GEOMETRIA ANALÍTICA)','ALGORITMOS E PROGRAMAÇÃO','ARQUITETURA DE COMPUTADORES I (ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES I)','CÁLCULO I (MATEMÁTICA I)','EPISTEMOLOGIA','INTRODUÇÃO À ENGENHARIA DA COMPUTAÇÃO (INTRODUÇÃO À ENGENHARIA)','LÓGICA PARA COMPUTAÇÃO','ARQUITETURA DE COMPUTADORES II (ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES II)','CÁLCULO II (MATEMÁTICA II)','ESTRUTURA DE DADOS','FÍSICA I','LABORATÓRIO DE FÍSICA I (LABORATÓRIO I)','TÉCNICAS DIGITAIS','FÍSICA II','LABORATÓRIO DE FÍSICA II (LABORATÓRIO II)','SISTEMAS DIGITAIS','CÁLCULO II','CIRCUITOS ELÉTRICOS I','LABORATÓRIO DE SISTEMAS OPERACIONAIS','ORGANIZAÇÃO DE COMPUTADORES','PROGRAMAÇÃO DE SISTEMAS','SISTEMAS OPERACIONAIS','"TECNOLOGIA, AMBIENTE E SOCIEDADE"','CÁLCULO III','CÁLCULO VETORIAL','ENGENHARIA DE SOFTWARE','ESTATÍSTICA E PROBABILIDADE','SISTEMAS DIGITAIS','TEORIA DA COMPUTAÇÃO','CÁLCULO IV','CIRCUITOS ELÉTRICOS II','FÍSICA III','LABORATÓRIO DE FÍSICA III','MÉTODOS NUMÉRICOS','METOLOGIA CIENTÍFICA','SISTEMAS DISTRIBUÍDOS','BARRAMENTOS E PROGRAMAÇÃO DE E/S','ELETRÔNICA I','FÍSICA IV','MATERIAIS DE ENGENHARIA','SISTEMAS DE TEMPO REAL','ELETRÔNICA II','FUNDAMENTOS DE CIRCUITOS INTEGRADOS','REDES DE COMPUTADORES','SISTEMAS E MODELAGEM','ECONOMIA PARA ENGENHARIA','INSTRUMENTAÇÃO','LABORATÓRIO DE MICROCONTROLADORES','LABORATÓRIO DE SISTEMAS INTEGRADOS I','PROJETOS DE SISTEMAS INTEGRADOS I','TRABALHO DE CONCLUSÃO DE CURSO I','ELETROMAGNETISMO APLICADO','PROCESSAMENTO DIGITAL DE SINAIS','QUALIDADE E TESTES DE SISTEMAS','PRODUÇÃO TEXTUAL','LÍNGUA INGLESA - NÍVEL I','LÍNGUA INGLESA - NÍVEL II','BANCO DE DADOS','TÓPICOS ESPECIAIS EM SISTEMAS ELETRÔNICOS','TÓPICOS ESPECIAIS EM ENGENHARIA DE SOFTWARE','PRODUÇÃO TEXTUAL - LABORATÓRIO DE EXPRESSÃO I','PRODUÇÃO TEXTUAL - LABORATÓRIO DE EXPRESSÃO II']

# comparando duas listas para ver se um item de uma lista esta contido na outra lista
#    for string in some_list:
#        for item in bad:
#            if item in string:
#                print 'To na bad ', string
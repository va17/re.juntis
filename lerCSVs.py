# -*- coding: utf-8 -*-
import os, time, sys, csv
def gera_csvs():
	pass
	lista = os.listdir('/home/miguel/Documentos/programasPython')# pega os nomes dos arquivos na pasta
	csvs = [arq for arq in lista if arq.lower().endswith(".csv") and arq != 'disciplinas.csv']# pega os nomes dos arquivos que são CSVs
	curso = []
	with open('disciplinas.csv', 'rb') as disciplinas:
		read = csv.reader(disciplinas)   
		for linha in read:
			curso.append(linha[0])

	for x in xrange(0,len(csvs)):# para cada arquivo, gerar um novo arquivo somente com o que interessa

		nome_arq = csvs[x]
		nome_arq_new_temp = csvs[x]
		nome_arq_new = nome_arq_new_temp.replace('.csv',str(x)+'.csv')# acrescenta um número no nome do aluno para não sobrescrever o arquivo original
		target = open(nome_arq_new,'w')
		aprovadas = []
		reprovadas = []
		cursando = []
		pendentes = []
		with open(nome_arq, 'rb') as arquivo:
			reader = csv.reader(arquivo)   
			cont = 0
			for linha in reader:
				i=0
				while(i < len(linha) and cont<6):
					if linha[i].startswith('Nome') == True or linha[i].startswith('CPF') == True or linha[i].startswith('Nascimento') == True or linha[i].startswith('Curso') == True or linha[i].startswith('Forma de') == True or linha[i].startswith('Ano/') == True:
						target.write(linha[i])
						target.write("\n")
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

	print 'Curso:\n'					
	print(curso)	
	print 'Aprovadas:\n'					
	print(aprovadas)	
	print 'Reprovadas:\n'					
	print(reprovadas)	
	print 'Cursando:\n'	
	print(cursando)
	print 'Pendentes:\n'	
	print(pendentes)
	print 'Pronto' # Fim da função gera_csvs
# !!!! fazer função para separar as cadeiras em listas uma para aprovadas outra para reprovadas, outra matriculado e outra paras as que faltam
#gera_csvs()
#		conceitos = ['A','B','C']
#		cadeiras = ['ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA (GEOMETRIA ANALÍTICA)','ALGORITMOS E PROGRAMAÇÃO','ARQUITETURA DE COMPUTADORES I (ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES I)','CÁLCULO I (MATEMÁTICA I)','EPISTEMOLOGIA','INTRODUÇÃO À ENGENHARIA DA COMPUTAÇÃO (INTRODUÇÃO À ENGENHARIA)','LÓGICA PARA COMPUTAÇÃO','ARQUITETURA DE COMPUTADORES II (ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES II)','CÁLCULO II (MATEMÁTICA II)','ESTRUTURA DE DADOS','FÍSICA I','LABORATÓRIO DE FÍSICA I (LABORATÓRIO I)','TÉCNICAS DIGITAIS','FÍSICA II','LABORATÓRIO DE FÍSICA II (LABORATÓRIO II)','SISTEMAS DIGITAIS','CÁLCULO II','CIRCUITOS ELÉTRICOS I','LABORATÓRIO DE SISTEMAS OPERACIONAIS','ORGANIZAÇÃO DE COMPUTADORES','PROGRAMAÇÃO DE SISTEMAS','SISTEMAS OPERACIONAIS','"TECNOLOGIA, AMBIENTE E SOCIEDADE"','CÁLCULO III','CÁLCULO VETORIAL','ENGENHARIA DE SOFTWARE','ESTATÍSTICA E PROBABILIDADE','SISTEMAS DIGITAIS','TEORIA DA COMPUTAÇÃO','CÁLCULO IV','CIRCUITOS ELÉTRICOS II','FÍSICA III','LABORATÓRIO DE FÍSICA III','MÉTODOS NUMÉRICOS','METOLOGIA CIENTÍFICA','SISTEMAS DISTRIBUÍDOS','BARRAMENTOS E PROGRAMAÇÃO DE E/S','ELETRÔNICA I','FÍSICA IV','MATERIAIS DE ENGENHARIA','SISTEMAS DE TEMPO REAL','ELETRÔNICA II','FUNDAMENTOS DE CIRCUITOS INTEGRADOS','REDES DE COMPUTADORES','SISTEMAS E MODELAGEM','ECONOMIA PARA ENGENHARIA','INSTRUMENTAÇÃO','LABORATÓRIO DE MICROCONTROLADORES','LABORATÓRIO DE SISTEMAS INTEGRADOS I','PROJETOS DE SISTEMAS INTEGRADOS I','TRABALHO DE CONCLUSÃO DE CURSO I','ELETROMAGNETISMO APLICADO','PROCESSAMENTO DIGITAL DE SINAIS','QUALIDADE E TESTES DE SISTEMAS','PRODUÇÃO TEXTUAL','LÍNGUA INGLESA - NÍVEL I','LÍNGUA INGLESA - NÍVEL II','BANCO DE DADOS','TÓPICOS ESPECIAIS EM SISTEMAS ELETRÔNICOS','TÓPICOS ESPECIAIS EM ENGENHARIA DE SOFTWARE','PRODUÇÃO TEXTUAL - LABORATÓRIO DE EXPRESSÃO I','PRODUÇÃO TEXTUAL - LABORATÓRIO DE EXPRESSÃO II']

# comparando duas listas para ver se um item de uma lista esta contido na outra lista
#    for string in some_list:
#        for item in bad:
#            if item in string:
#                print 'To na bad ', string

#! /usr/local/bin/python3
# -*- coding: utf-8 -*-


## intervalos
##
##                        segunda     terca   quarta  quinta  sexta   sabado
## manha 08:00 - 09:00    1           13      25      37      49      61
## manha 09:00 - 10:00    2           14      26      38      50      62
## manha 10:00 - 11:00    3           15      27      39      51      63
## manha 11:00 - 12:00    4           16      28      40      52      64
## tarde 13:00 - 14:00    5           17      29      41      53      65
## tarde 14:00 - 15:00    6           18      30      42      54      66
## tarde 15:00 - 16:00    7           19      31      43      55      67
## tarde 16:00 - 17:00    8           20      32      44      56      68
## noite 18:00 - 19:00    9           21      33      45      57      69
## noite 19:00 - 20:00    10          22      34      46      58      70
## noite 20:00 - 21:00    11          23      35      47      59      71
## noite 21:00 - 22:00    12          24      36      48      60      72

def get_professores():
    return [{'id': 1, 'nome': 'Prof 1', 'disciplinas': [1,3,5,45,46], 'horarios': [1,2,3,4,17,18,19,20,49,50,51,52,53,54,55,56]},         # segunda de manha; terca de tarde; sexta dia todo
            {'id': 2, 'nome': 'Prof 2', 'disciplinas': [2,4,6,44,47], 'horarios': [1,2,3,4,5,6,7,8,25,26,27,28,29,30,31,32,37,38,39,40]}, # segunda de dia todo; quarta dia todo; quinta de manha
            {'id': 3, 'nome': 'Prof 3', 'disciplinas': [9,10,12,43,48], 'horarios': [5,6,7,8,13,14,15,16,17,18,19,20,41,42,43,44]},       # segunda de tarde; dia todo terca; quinta de tarde
            {'id': 4, 'nome': 'Prof 4', 'disciplinas': [1,2,7,11,42,49], 'horarios': [13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,32,49,50,51,52,53,54,55,56]}, # terca dia todo; quarta dia todo; sexta dia todo
            {'id': 5, 'nome': 'Prof 5', 'disciplinas': [13,14,17,41,50,61], 'horarios': [5,6,7,8,17,18,19,20,41,42,43,44,53,54,55,56]}, # segunda tarde; terca tarde; quinta tarde; sexta tarde;
            {'id': 6, 'nome': 'Prof 6', 'disciplinas': [18,19,16,20,40,51,60], 'horarios': [1,2,3,4,13,14,15,16,25,26,27,28,37,38,39,40,49,50,51,52,53]}, # segunda manha; terca manha; quarta manha; quinta manha; sexta manha
            {'id': 7, 'nome': 'Prof 7', 'disciplinas': [21,22,23,39,52,59], 'horarios': [5,6,7,8,17,18,19,20,41,42,43,44,53,54,55,56]},  # segunda tarde; terca tarde; quinta tarde; sexta tarde;
            {'id': 8, 'nome': 'Prof 8', 'disciplinas': [24,25,30,31,33,38,53,58], 'horarios': [1,2,3,4,5,6,7,8,25,26,27,28,29,30,31,32,37,38,39,40]}, # segunda de dia todo; quarta dia todo; quinta de manha
            {'id': 9, 'nome': 'Prof 9', 'disciplinas': [26,27,28,29,32,37,54,57], 'horarios': [5,6,7,8,13,14,15,16,17,18,19,20,41,42,43,44]},       # segunda de tarde; dia todo terca; quinta de tarde
            {'id': 10, 'nome': 'Prof 10', 'disciplinas': [8,15,34,35,36,55,56], 'horarios': [1,2,3,4,5,6,7,8,25,26,27,28,29,30,31,32,37,38,39,40]}] # segunda de dia todo; quarta dia todo; quinta de manha


def get_disciplinas(filter=0):
    return [{'id': 1, 'nome': 'Epistemologia', 'semestre': 1, 'creditos': 2, 'prioridade': 1},
            {'id': 2, 'nome': 'Produção Textual', 'semestre': 1, 'creditos': 4,'prioridade': 0},
            {'id': 3, 'nome': 'Álgebra Linear e Geometria Analítica', 'semestre': 1, 'creditos': 4,'prioridade': 8},
            {'id': 4, 'nome': 'Cálculo 1', 'semestre': 1, 'creditos': 4,'prioridade': 8},
            {'id': 5, 'nome': 'Algoritmos e Programação', 'semestre': 1, 'creditos': 4,'prioridade': 5},
            {'id': 6, 'nome': 'Lógica para Computação', 'semestre': 1, 'creditos': 4,'prioridade': 5},
            {'id': 7, 'nome': 'Arquitetura de Computadores 1', 'semestre': 1, 'creditos': 4,'prioridade': 6},
            {'id': 8, 'nome': 'Introdução à Engenharia de Computação', 'semestre': 1, 'creditos': 2,'prioridade': 0},
            {'id': 9, 'nome': 'Arquitetura de Computadores 2', 'semestre': 2, 'creditos': 4, 'prioridade': 5},
            {'id': 10, 'nome': 'Cálculo 2', 'semestre': 2, 'creditos': 4, 'prioridade': 7},
            {'id': 11, 'nome': 'Técnicas Digitais', 'semestre': 2, 'creditos': 4, 'prioridade': 3},
            {'id': 12, 'nome': 'Física 1', 'semestre': 2, 'creditos': 4, 'prioridade': 4},
            {'id': 13, 'nome': 'Laboratório de Física 1', 'semestre': 2, 'creditos': 2, 'prioridade': 3},
            {'id': 14, 'nome': 'Estrutura de Dados', 'semestre': 2, 'creditos': 4, 'prioridade': 4},
            {'id': 15, 'nome': 'Metodologia Científica', 'semestre': 2, 'creditos': 2, 'prioridade': 0},
            {'id': 16, 'nome': 'Tecnologia Ambiente e Sociedade', 'semestre': 2, 'creditos': 4, 'prioridade': 0},
            {'id': 17, 'nome': 'Física 2', 'semestre': 3, 'creditos': 4, 'prioridade': 3},
            {'id': 18, 'nome': 'Laboratório de Física 2', 'semestre': 3, 'creditos': 2, 'prioridade': 2},
            {'id': 19, 'nome': 'Cálculo Vetorial', 'semestre': 3, 'creditos': 4, 'prioridade': 0},
            {'id': 20, 'nome': 'Cálculo 3', 'semestre': 3, 'creditos': 4, 'prioridade': 6},
            {'id': 21, 'nome': 'Sistemas Digitais', 'semestre': 3, 'creditos': 4, 'prioridade': 0},
            {'id': 22, 'nome': 'Circuitos Elétricos 1', 'semestre': 3, 'creditos': 4, 'prioridade': 6},
            {'id': 23, 'nome': 'Engenharia de Software', 'semestre': 3, 'creditos': 4, 'prioridade': 0},
            {'id': 24, 'nome': 'Física 3', 'semestre': 4, 'creditos': 4, 'prioridade': 3},
            {'id': 25, 'nome': 'Laboratório de Física 3', 'semestre': 4, 'creditos': 4, 'prioridade': 2},
            {'id': 26, 'nome': 'Circuitos Elétricos 2', 'semestre': 4, 'creditos': 4, 'prioridade': 5},
            {'id': 27, 'nome': 'Cálculo 4', 'semestre': 4, 'creditos': 4, 'prioridade': 4},
            {'id': 28, 'nome': 'Métodos Numéricos', 'semestre': 4, 'creditos': 4, 'prioridade': 4},
            {'id': 29, 'nome': 'Programação de Sistemas', 'semestre': 4, 'creditos': 4, 'prioridade': 0},
            {'id': 30, 'nome': 'Organização de Computadores', 'semestre': 4, 'creditos': 4, 'prioridade': 1},
            {'id': 31, 'nome': 'Materiais de Engenharia', 'semestre': 5, 'creditos': 4, 'prioridade': 0},
            {'id': 32, 'nome': 'Eletrônica 1', 'semestre': 5, 'creditos': 4, 'prioridade': 4},
            {'id': 33, 'nome': 'Teoria da Computação', 'semestre': 5, 'creditos': 4, 'prioridade': 0},
            {'id': 34, 'nome': 'Física 4', 'semestre': 5, 'creditos': 4, 'prioridade': 1},
            {'id': 35, 'nome': 'Laboratório de Sistemas Operacionais', 'semestre': 5, 'creditos': 2, 'prioridade': 2},
            {'id': 36, 'nome': 'Sistemas Operacionais', 'semestre': 5, 'creditos': 4, 'prioridade': 3},
            {'id': 37, 'nome': 'Probabilidade e Estatística', 'semestre': 5, 'creditos': 2, 'prioridade': 1},
            {'id': 38, 'nome': 'Sistemas e Modelagem', 'semestre': 6, 'creditos': 4, 'prioridade': 3},
            {'id': 39, 'nome': 'Eletrônica 2', 'semestre': 6, 'creditos': 4, 'prioridade': 3},
            {'id': 40, 'nome': 'Legislação e ética', 'semestre': 6, 'creditos': 2, 'prioridade': 0},
            {'id': 41, 'nome': 'Microcontroladores', 'semestre': 6, 'creditos': 4, 'prioridade': 1},
            {'id': 42, 'nome': 'Laboratório de Microcontroladores', 'semestre': 6, 'creditos': 2, 'prioridade': 0},
            {'id': 43, 'nome': 'Rede de Computadores', 'semestre': 6, 'creditos': 4, 'prioridade': 2},
            {'id': 44, 'nome': 'Sistemas de Tempo Real', 'semestre': 6, 'creditos': 4, 'prioridade': 1},
            {'id': 45, 'nome': 'Eletromagnetismo Aplicado', 'semestre': 7, 'creditos': 4, 'prioridade': 0},
            {'id': 46, 'nome': 'Fundamentos de Circuitos Integrados', 'semestre': 7, 'creditos': 4, 'prioridade': 2},
            {'id': 47, 'nome': 'Comunicação de Dados', 'semestre': 7, 'creditos': 4, 'prioridade': 1},
            {'id': 48, 'nome': 'Barramentos e Programação de E/S', 'semestre': 7, 'creditos': 4, 'prioridade': 0},
            {'id': 49, 'nome': 'Instrumentação', 'semestre': 7, 'creditos': 4, 'prioridade': 3},
            {'id': 50, 'nome': 'Sistemas Distribuídos', 'semestre': 7, 'creditos': 4, 'prioridade': 1},
            {'id': 51, 'nome': 'Economia para Engenharia', 'semestre': 7, 'creditos': 2, 'prioridade': 2},
            {'id': 52, 'nome': 'Sistemas de Controle', 'semestre': 8, 'creditos': 4, 'prioridade': 1},
            {'id': 53, 'nome': 'Projeto de Sistemas Integrados 1', 'semestre': 8, 'creditos': 4, 'prioridade': 1},
            {'id': 54, 'nome': 'Laboratório de Sistemas Integrados', 'semestre': 8, 'creditos': 2, 'prioridade': 1},
            {'id': 55, 'nome': 'Processamento Digital de Sinais', 'semestre': 8, 'creditos': 4, 'prioridade': 1},
            {'id': 56, 'nome': 'Trabalho de Conclusão 1', 'semestre': 9, 'creditos': 2, 'prioridade': 0},
            {'id': 57, 'nome': 'Automação', 'semestre': 9, 'creditos': 4, 'prioridade': 0},
            {'id': 58, 'nome': 'Gestão e Empreendedorismo', 'semestre': 9, 'creditos': 4, 'prioridade': 0},
            {'id': 59, 'nome': 'Trabalho de Conclusão 2', 'semestre': 10, 'creditos': 2, 'prioridade': 0},
            {'id': 60, 'nome': 'Qualidade e Testes de Sistemas', 'semestre': 10, 'creditos': 4, 'prioridade': 0},
            {'id': 61, 'nome': 'Estágio Profissional Supervisionado', 'semestre': 10, 'creditos': 12, 'prioridade': 0}]


def get_alunos():
    return [{'id': 1, 'nome': 'Vanessa', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 2, 'nome': 'Ana', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 3, 'nome': 'Vitor', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 4, 'nome': 'Alleff', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 5, 'nome': 'Miguel', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 6, 'nome': 'Francisco', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 7, 'nome': 'Fernanda', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 8, 'nome': 'Marcos', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 9, 'nome': 'Gabrieli', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 10, 'nome': 'Amanda', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 11, 'nome': 'Lincoln', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 12, 'nome': 'Gabriel', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 13, 'nome': 'Felipe', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 14, 'nome': 'Ulisses', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 15, 'nome': 'Carlos', 'semestre': 5, 'porcentagem': 45, 'preferencias': [6,7,8,9,10,11]},
            {'id': 16, 'nome': 'Denis', 'semestre': 7, 'porcentagem': 65, 'preferencias': [52,53,54,55]},
            {'id': 17, 'nome': 'Lorenzo', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 18, 'nome': 'Kenny', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 19, 'nome': 'Juliana', 'semestre': 1, 'porcentagem': 5, 'preferencias': [9,10,11,12,13,14,15,16]},
            {'id': 20, 'nome': 'Adão', 'semestre': 1, 'porcentagem': 5, 'preferencias': [1,2,3,4,5,6,9,10]},
            {'id': 21, 'nome': 'Eva', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 22, 'nome': 'Caroline', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 23, 'nome': 'Maurício', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 24, 'nome': 'Gisele', 'semestre': 3, 'porcentagem': 25, 'preferencias': [24,25,26,27,28,29,30]},
            {'id': 25, 'nome': 'João', 'semestre': 4, 'porcentagem': 35, 'preferencias': [31,32,33,34,35,36,37]},
            {'id': 26, 'nome': 'Cesar', 'semestre': 3, 'porcentagem': 25, 'preferencias': [24,25,26,27,28,29,30]},
            {'id': 27, 'nome': 'Luiza', 'semestre': 5, 'porcentagem': 45, 'preferencias': [38,39,40,41,42,43,44]},
            {'id': 28, 'nome': 'Júlio', 'semestre': 5, 'porcentagem': 45, 'preferencias': [38,39,40,41,42,43,44]},
            {'id': 29, 'nome': 'Jeferson', 'semestre': 7, 'porcentagem': 65, 'preferencias': [52,53,54,55]},
            {'id': 30, 'nome': 'Natalia', 'semestre': 7, 'porcentagem': 65, 'preferencias': [52,53,54,55]},
            {'id': 31, 'nome': 'Viviane', 'semestre': 9, 'porcentagem': 85, 'preferencias': [59,60,61]},
            {'id': 32, 'nome': 'Guilherme', 'semestre': 9, 'porcentagem': 85, 'preferencias': [59,60,61]},
            {'id': 33, 'nome': 'William', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 34, 'nome': 'Érico', 'semestre': 3, 'porcentagem': 25, 'preferencias': [24,25,26,27,28,29,30]}, 
            {'id': 35, 'nome': 'Eduardo', 'semestre': 5, 'porcentagem': 45, 'preferencias': [38,39,40,41,42,43,44]},
            {'id': 36, 'nome': 'Eduarda', 'semestre': 7, 'porcentagem': 65, 'preferencias': [52,53,54,55]},
            {'id': 37, 'nome': 'Pedro', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 38, 'nome': 'Israel', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 39, 'nome': 'Aline', 'semestre': 10, 'porcentagem': 95, 'preferencias': [59,60,61]},
            {'id': 40, 'nome': 'Isabel', 'semestre': 1, 'porcentagem': 5, 'preferencias': [1,2,3,4,5,6,7,8]},
            {'id': 41, 'nome': 'Ismael', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 42, 'nome': 'Emerson', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 43, 'nome': 'Vitor K', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]},
            {'id': 44, 'nome': 'Vitor D', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 45, 'nome': 'Leonardo', 'semestre': 5, 'porcentagem': 45, 'preferencias': [38,39,40,41,42,43,44]},
            {'id': 46, 'nome': 'Patrícia', 'semestre': 3, 'porcentagem': 23, 'preferencias': [24,25,26,27,28,29,30]}, 
            {'id': 47, 'nome': 'Elisa', 'semestre': 1, 'porcentagem': 5, 'preferencias': [1,2,3,4,5,6,7,8]},
            {'id': 48, 'nome': 'Robson', 'semestre': 5, 'porcentagem': 45, 'preferencias': [38,39,40,41,42,43,44]},
            {'id': 49, 'nome': 'Alison', 'semestre': 4, 'porcentagem': 35, 'preferencias': [31,32,33,34,35,36,37]},
            {'id': 50, 'nome': 'Rodrigo', 'semestre': 4, 'porcentagem': 35, 'preferencias': [31,32,33,34,35,36,37]},
            {'id': 51, 'nome': 'Giovani', 'semestre': 4, 'porcentagem': 35, 'preferencias': [31,32,33,34,35,36,37]},
            {'id': 52, 'nome': 'Welingnton', 'semestre': 6, 'porcentagem': 55, 'preferencias': [45,46,47,48,49,50,51]},
            {'id': 53, 'nome': 'Delvin', 'semestre': 4, 'porcentagem': 35, 'preferencias': [31,32,33,34,35,36,37]},
            {'id': 54, 'nome': 'Anderson', 'semestre': 3, 'porcentagem': 25, 'preferencias': [24,25,26,27,28,29,30]},
            {'id': 55, 'nome': 'Jeferson', 'semestre': 9, 'porcentagem': 85, 'preferencias': [59,60,61]},
            {'id': 56, 'nome': 'Fabiano', 'semestre': 7, 'porcentagem': 65, 'preferencias': [52,53,54,55]},
            {'id': 57, 'nome': 'Fabiana', 'semestre': 1, 'porcentagem': 5, 'preferencias': [1,2,3,4,5,6,7,8]},
            {'id': 58, 'nome': 'Maria', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 59, 'nome': 'José', 'semestre': 8, 'porcentagem': 75, 'preferencias': [56,57,58]},
            {'id': 60, 'nome': 'Daniela', 'semestre': 2, 'porcentagem': 15, 'preferencias': [17,18,19,20,21,22,23]}]


def get_disciplina(Id):
    disciplinas = get_disciplinas()
    for d in disciplinas:
        if(d['id'] == Id):
            resultado = d
    return resultado

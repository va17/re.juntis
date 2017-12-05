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

import time
import os
import argparse
import csv
from collections import defaultdict
from sys import argv
import datetime
import rejuntis_db
import operator
from random import shuffle
import json
from prettytable import PrettyTable
import make_csv

DISCIPLINAS_SEM_HORARIO = [56, 59, 61]

def run(Filename, Num, RandNum, semestre, csv_enabled, pretty_table_enabled):
    start_time = time.time()
    alunos = rejuntis_db.get_alunos()
    professores = rejuntis_db.get_professores()
    disciplinas = rejuntis_db.get_disciplinas()
    disciplinas_semestre = rejuntis_db.get_disciplinas(filter=semestre)
    disciplinas_semestre = add_time_disciplina(disciplinas_semestre, professores)
    alunos = ensure_preferences(alunos, semestre)
    poll_result = poll(disciplinas_semestre, alunos)
    clear_result = [item for item in poll_result if item['votos'] > 0]
    ordered_result = sorted(clear_result, key=operator.itemgetter('votos'), reverse=True)
    creditos_semestre = get_creditos_semestre(professores)
    total_creditos = get_total_creditos(ordered_result)
    final_result = fit_disciplinas(ordered_result, total_creditos, creditos_semestre)
    schedules = generate_schedules(final_result, professores, [], RandNum)
    schedules = count_conflicts(schedules, alunos)
    top_schedules = filter_schedules(schedules, Num)
    write_json(top_schedules, Filename)
    make_csv.write_csv(top_schedules, csv_enabled, pretty_table_enabled)
    x = PrettyTable()
    x.add_column("Tempo de exec.", ["%s segundos" % (time.time() - start_time)])
    x.add_column("Total alunos", ["%s " % len(alunos)])
    x.add_column("Total professores", ["%s " % len(professores)])
    x.add_column("Total disciplinas semestre", ["%s " % len(final_result)])
    x.add_column("Carga semestre", ["%s créditos" % get_total_creditos(final_result)])
    print x


def count_conflicts(schedules, alunos):
    f = open('conflicts.log','w')
    result = []
    i = 1
    for schedule in schedules:
        conflicts = 0
        for aluno in alunos:
            w = 72
            conflict_vector = [0 for x in range(w)]
            for disciplina in schedule:
                if disciplina['id'] in aluno['preferencias']:
                    conflict_vector[disciplina['time']] = conflict_vector[disciplina['time']] + 1
                    if(conflict_vector[disciplina['time']] > 1):
                        conflicts = conflicts + 1
                        L = "LOG: Aluno(a) %s tem conflito para fazer disciplina %s no momento %s no schedule com ID %s\n" % (aluno['nome'], disciplina['nome'], disciplina['time'], i)
                        f.write(L)
        result.append({'conflitos': conflicts, 'schedule': schedule, 'schedule_id': i})
        i += 1
    f.close()
    return result


def filter_schedules(schedules, num):
    schedules = sorted(schedules, key=operator.itemgetter('conflitos'))
    x = 0
    result = []
    for s in schedules:
        if(x < num):
            result.append(s)
        x = x +1
    return result


def generate_schedules(disciplinas, professores0, acc, N=100):
    schedule = []
    professores = professores0
    updated_professores = []
    for d in disciplinas:
        creditos = d['creditos']
        horarios_possiveis = get_horarios_possiveis(d['horarios'], creditos)
        horarios_mesmo_semestre = [s['time'] for s in schedule if s['semestre'] == d['semestre']]
        horarios_possiveis = [h for h in horarios_possiveis if h not in horarios_mesmo_semestre]
        shuffle(horarios_possiveis)
        if horarios_possiveis == []:
            if d['id'] not in DISCIPLINAS_SEM_HORARIO:
                print "Disciplina", d['nome'], "nao podera ser ministrada porque nao existem mais horarios disponiveis"
        else:
            when = horarios_possiveis[0]
            for p in professores:
                if d['id'] in p['disciplinas']:
                    removed_professor = p
                    p['horarios'] = [item for item in p['horarios'] if not ((item >= when) and (item < when+creditos))]
                    updated_professor = p
                    break
            professores.remove(removed_professor)
            professores.append(updated_professor)
            i = when
            while(i < (when+creditos)):
                schedule.append({'time': i, 'id': d['id'], 'semestre': d['semestre'], 'nome': d['nome']})
                i = i+1
    if N != 0:
        acc.append(sorted(schedule, key=operator.itemgetter('time')))
        return generate_schedules(disciplinas, professores0, acc, N-1)
    else:
        return acc


def get_horarios_possiveis(horarios, creditos):
    result = []
    for h in horarios:
        if h in [1, 13, 25, 37, 49, 61, 3, 15, 27, 39, 51, 63, 5, 17, 29, 41, 53, 65, 7, 19, 31, 43, 55, 67, 9, 21, 33, 45, 57, 69, 11, 23, 35, 47, 59, 71] and creditos == 2:
            result.append(h)
        elif h in [1, 13, 25, 37, 49, 61, 5, 17, 29, 41, 53, 65, 9, 21, 33, 45, 57, 69] and creditos == 4:
            result.append(h)
    return result


def add_time_disciplina(disciplinas, professores):
    acc = []
    for d in disciplinas:
        horarios = []
        for p in professores:
            if d['id'] in p['disciplinas']:
                horarios = horarios + p['horarios']
                horarios = list(set(horarios))
        d['horarios'] = horarios
        acc.append(d)
    return acc


def fit_disciplinas(disciplinas, creditos, creditos_semestre):
    while creditos > creditos_semestre:
        disciplinas.pop()
        creditos = get_total_creditos(disciplinas)
    return disciplinas


def get_creditos_semestre(professores):
    total = 0
    for p in professores:
        intervalos = p['horarios']
        for i in intervalos:
            total = total + 1
    return total


def get_total_creditos(disciplinas):
    acc = 0
    for d in disciplinas:
        creditos = d['creditos']
        acc = acc + creditos
    return acc


def poll(disciplinas, alunos):
    acc = []
    for d in disciplinas:
        id = d['id']
        d['votos'] = 0
        for aluno in alunos:
            semestre_aluno = aluno['semestre']
            porcentagem_aluno = aluno['porcentagem']
            if semestre_aluno == 2:
                peso = 2
            elif porcentagem_aluno >= 80:
                peso = 5
            else:
                peso = 1
            if id in aluno['preferencias']:
                d['votos'] = d['votos'] + (1 * peso)
        acc.append(d)
    return acc


def ensure_preferences(alunos, semestre):
    acc = []
    disciplinas = rejuntis_db.get_disciplinas()
    ids_disciplinas = get_ids(disciplinas)
    for aluno in alunos:
        if(aluno['preferencias'] == []):
            aluno['preferencias'] = generate_preferences(aluno, ids_disciplinas, semestre)
        else:
            aluno['preferencias'] = order_preferences(aluno)
        acc.append(aluno)
    return acc


def current_year_semester():
    month = current_month()
    if(month>7):
        return 2
    else:
        return 1


def current_month():
    datetime.datetime.now()


def generate_preferences(aluno, ids_disciplinas, semester):
    disciplinas_periodo = rejuntis_db.get_disciplinas(filter=semester)
    ids_periodo = get_ids(disciplinas_periodo)
    disciplinas_a_fazer = [item for item in ids_disciplinas if item not in aluno['disciplinas']] # ids_disciplinas - disciplinas feitas
    disciplinas_possiveis = [item for item in disciplinas_a_fazer if item in ids_periodo]
    aluno['preferencias'] = disciplinas_possiveis
    disciplinas_possiveis_ordenadas = order_preferences(aluno)
    return disciplinas_possiveis_ordenadas


def get_ids(list_of_objects):
    ids = []
    for i in list_of_objects:
        id = i['id']
        ids.append(id)
    return ids


def order_preferences(aluno):
    preferences = aluno['preferencias']
    listdist = []
    for i in preferences:
        disciplina = rejuntis_db.get_disciplina(i)
        prioridade = disciplina['prioridade']
        listdist.append({'key':i,
                         'prioridade':prioridade})
    preferences = []
    for r in sorted(listdist, key=operator.itemgetter('prioridade')):
        preferences.append(r['key'])
    return preferences


def write_json(Dict, Filename='result.json'):
    # print(json.dumps(Dict))
    with open(Filename, 'wb') as outfile:
        json.dump(Dict, outfile, indent=2, sort_keys=True)


if __name__ == "__main__":
    def main():
        parser = argparse.ArgumentParser(description="Gera cinco horarios a partir de dados no banco re.juntis")
        optional_group = parser.add_argument_group('argumentos opcionais')
        optional_group.add_argument('-p', '--path', dest='path',
                                     type=str, required=False, default='result.json',
                                     help='Caminho para armazenar resultado. Default: result.json')
        optional_group.add_argument('-rn', '--randnum', dest='randnum',
                                     type=int, required=False, default=100,
                                     help='Numero de calendarios a serem randomizados. Default: 100. Max: 900')
        optional_group.add_argument('-n', '--num', dest='num',
                                     type=int, required=False, default=3,
                                     help='Numero de melhores resultados a serem retornados. Default: 3')
        optional_group.add_argument('-s', '--s', dest='sem',
                                     type=int, required=False, default=current_year_semester(),
                                     help='Calcular calendario para um dado semestre do ano (1|2). Default: semestre atual')
        optional_group.add_argument('-c', '--csv', dest='csv',
                                     type=bool, required=False, default=True,
                                     help='Gera um csv (result.csv) do melhor resultado. Default: True')
        optional_group.add_argument('-t', '--prettytable', dest='pr',
                                     type=bool, required=False, default=False,
                                     help='Gera um arquivo texto em pretty table (result.txt) do melhor resultado. Default: False')
        args = parser.parse_args()
        path = args.path
        randnum = args.randnum
        sem = args.sem
        num = args.num
        csv = args.csv
        pretty = args.pr
        if num <= 0:
            num = 3
        run(path, num, randnum, sem, csv, pretty)
    main()

#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import operator
import csv
from prettytable import PrettyTable
from unicodedata import normalize

def write_csv(Schedules, csv_enabled, pretty_table_enabled, CsvFilename = 'result.csv', PrettyTableFilename='result.txt'):
    if csv_enabled or pretty_table_enabled:
        Semestre = ["1", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "2", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "3", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "4", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "5", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "6", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "7", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "8", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "9", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    "10", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        Horarios = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00",
                    "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00"]
        best = Schedules[0]['schedule']
        best = sorted(best, key=operator.itemgetter('time'))
        d = [[] for i in range(6)]
        for s in best:
            if s['time'] <= 12:
                d[0].append(s)
            elif s['time'] <= 24:
                d[1].append(s)
            elif s['time'] <= 36:
                d[2].append(s)
            elif s['time'] <= 48:
                d[3].append(s)
            elif s['time'] <= 60:
                d[4].append(s)
            else:
                d[5].append(s)
        dia = [[" " for iy in range(120)] for ix in range(6)]

        for ix in range(6):
            sem = 1
            while sem <= 10:
                for item in d[ix]:
                    if item['semestre'] == sem:
                        pos = item['time']+((sem-1)*12)-(ix*12)-1
                        dia[ix][pos] = item['nome']
                sem += 1
        if pretty_table_enabled:
            x = PrettyTable()
            x.add_column("Semestre", Semestre)
            x.add_column("Horario", Horarios)
            x.add_column("Segunda", dia[0])
            x.add_column("Terca", dia[1])
            x.add_column("Quarta", dia[2])
            x.add_column("Quinta", dia[3])
            x.add_column("Sexta", dia[4])
            x.add_column("Sabado", dia[5])
            with open(PrettyTableFilename, 'w') as w:
                w.write(str(x))
        if csv_enabled:
            write_csv_impl(CsvFilename, Semestre, Horarios, dia)


def write_csv_impl(Filename, column1, column2, columns):
    column1.insert(0,"Semestre")
    column2.insert(0,"Horario")
    columns[0].insert(0,"Segunda")
    columns[1].insert(0,"Terca")
    columns[2].insert(0,"Quarta")
    columns[3].insert(0,"Quinta")
    columns[4].insert(0,"Sexta")
    columns[5].insert(0,"Sabado")
    csv_data = [column1, column2, columns[0], columns[1], columns[2], columns[3], columns[4], columns[5]]
    csv_data = zip(*csv_data)
    # print csv_data
    with open(Filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n', dialect='excel')
        for val in csv_data:
            writer.writerow([remover_acentos(v) for v in val])


def remover_acentos(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

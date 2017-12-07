# Script gerador de horários (schedule generator)

## Functionamento:

A partir de um shell, execute:

```sh
$> python generate_schedule.py
```

### Parâmetros optionais:

`-p` : define o path do arquivo de saída. Ex:
``` $> python generate_schedule.py -p 'arquivo.json' ```

`-rn` : Número de calendários a serem randomizados. Default: 100. Max: 900. Ex:
``` $> python generate_schedule.py -rn 200 ```

`-n` : Número de melhores resultados a serem retornados. Default: 3. Ex:
``` $> python generate_schedule.py -n 1 ```

`-s` : Calcula calendário para um dado semestre do ano (1 ou 2). Default: semestre atual. Ex: ``` $> python generate_schedule.py -s 2 ```

`-c` : Gera um csv (result.csv) do melhor resultado. Default: True
 
`-t` : Gera um arquivo texto em pretty table (result.txt) do melhor resultado. Default: False

## Dependências:

rejuntis_db (atualmente usando dados "mockados"), PrettyTable, json, csv.

## TODOs:

- [ ] Considerar que uma disciplina pode ter mais de um professor possível;
- [ ] Adicionar condicionais de laboratório, salas de aula, etc;
- [ ] Gerar lista de preferencias (alunos) considerando hierarquia das disciplinas;
- [ ] Garantir funcionamento do gerador de preferências dos alunos com lista de disciplinas feitas (testar, já implementado);
- [x] Garantir disciplinas do primeiro semestre se semestre atual = 1;
- [ ] Gerenciar disciplinas eletivas;
- [x] Gerar CSV
- [ ] Linkar com UI e BD.

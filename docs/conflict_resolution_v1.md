# Resolução de Conflitos

Este documento deverá conter toda a documentação relacionada a resolução de conflitos, bem como descrições, fluxogramas e diagramas que representem o mesmo.

## Idéia geral

### Primeira etapa:

- Lê disciplinas (separadas por semestre e priorizadas);
- Lê alunos (nome, matricula, % do curso) e disciplinas que tem permissão de fazer;
- Lê professores (horários disponíveis em intervalos e lista de disciplinas que podem lecionar).

### Segunda etapa:
- Remover disciplinas que não podem ser lecionadas (não há professores ou não é o semestre dela);
- Montar lista de disciplinas para cada aluno;
- Se o aluno montou lista de preferência, usá-la, se não, verifica número de disciplinas semestre ativo (primeiro semestre com disciplina(s) a fazer) do aluno;
	- Com este número, selecionar uma lista de disciplinas (do menor semestre com disciplina a fazer até o maior);
- Priorizar as disciplinas, maior prioridade para disciplinas que são pré-requisito de alguma;
- Adicionar disciplinas possíveis ao fim da lista (menor prioridade, serão utilizadas em caso de conflitos).

### Terceira etapa:
- Decidir a prioridade geral das disciplinas possíveis pelo número de estudantes que farão a mesma; Prioridade para alunos de segundo semestre e com mais 80% do curso;
- Priorização por votos, alunos de segundo semestre peso 2, alunos com mais de 80% peso 5, outros peso 1;
- Remover disciplinas com 0 votos;
- Definir X créditos (soma total dos créditos possíveis): somar total de horas disponíveis dos professores, 1 hora = 1 crédito;
- Por semestre é possível ter X créditos, somar número de créditos das disciplinas e verificar se é > X; se sim, remover disciplinas com < 2 votos suficientes para que se obtenha X créditos na soma total; Também é possível remover disciplinas que passem da carga horária de um professor (exemplo: Professor Blah tem 12 créditos na semana mas existem 4 disciplinas com votos, remover a que tiver menos votos).

### Quarta etapa:
- Definir horários (intervalos) possíveis para cada disciplina pelos professores que podem ministrá-las (utilizar professor prioritário da disciplina);
- Definir o que é conflito exclusivo: disciplinas que precisam de laboratórios no mesmo horário; projetores (?) ...
	* Opção 1:
		- Montar horários (300+) desconsiderando conflitos com alunos, porém, considerando conflitos de semestre e salas (utilização do algoritmo [Given n appointments, find all conflicting appointments] ou semelhantes como [Hopcroft–Karp algorithm] e [Bipartite_matching]);
		- Dar um score para cada horário considerando os conflitos com alunos;
		- Selecionar 10 horários com menores scores de conflito;



## Referências:

"Given n appointments, find all conflicting appointments": http://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/

[Hopcroft–Karp algorithm]: https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm

Assignment problem: https://en.wikipedia.org/wiki/Assignment_problem

Harold W. Kuhn, "The Hungarian Method for the assignment problem", Naval Research Logistics Quarterly, 2: 83–97, 1955

[Bipartite_matching]: https://en.wikipedia.org/wiki/Matching_(graph_theory)#Bipartite_matching

[Given n appointments, find all conflicting appointments]: http://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/


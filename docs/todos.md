# Lista de TODOs


### Primeira etapa:

Esta etapa incluí todo o trabalho por trás do carregamento de dados do sistema. Os dados devem ser convertidos de seu valor original para objetos Dictionary do Python, [ler mais aqui](https://docs.python.org/2/tutorial/datastructures.html#dictionaries).

- Lê disciplinas (separadas por semestre e priorizadas);
	- [ ] Criar função que lê CSV contendo as disciplinas com suas respectivas prioridades (prioridade = cadeia/caminho de disciplinas trancadas) e armazena no banco de dados `load_disciplinas()`
	- [ ] Criar função que lê disciplinas do banco de dados `get_disciplinas()` (Nome, CH, CR, Semestre, Pre-requisitos, Prioridade, Projetor (bool), Laboratório Eletrônica (bool), Laboratório Informática (bool))
- Lê alunos (nome, matricula, % do curso) e disciplinas que tem permissão de fazer;
	* [ ] Criar função que lê CSV de cada aluno e carrega seus dados em uma lista de dictionaries `store_alunos()`;
		* Campos dict: `nome` (string), `matricula` (string), `porcentagem_curso` (float), `disciplinas_pendentes_possiveis` (list of strings)
	* [ ] Criar formulário de pesquisa para alunos (salvar diretamente no banco)  
	* [ ] Criar função que obtém as preferências (pesquisa) de alunos do banco de dados e adiciona ao objeto dict (list);
		* `get_preferences(Id ou Matricula ou Email)` // Retorna as preferências de um dado aluno;
		* `get_preferences()` // Retorna as preferências de todos os alunos;
	* [ ] Criar funções para leitura de alunos do banco de dados (`get_aluno(Matricula)` e `get_alunos()`)
- Lê professores (horários disponíveis em intervalos e lista de disciplinas que podem lecionar).
	* [ ] Criar formulário para professores para obter seus horários de disponibilidade;
	* [ ] Adicionar ao objeto professor no banco uma lista de disciplinas que o mesmo pode lecionar;
	* [ ] Criar função `get_professores()` que retorna uma lista de objetos professor;
	* [ ] Criar função `get_professor(Id ou Email)` que retorna o objeto professor solicitado;

### Segunda etapa:

- Remover disciplinas que não podem ser lecionadas (não há professores ou não é o semestre dela);
	* [ ] Criar função que retorna todas as disciplinas possíveis do semestre (`get_valid_disciplinas(int Semestre)`)
- [ ] Criar função que gera uma lista de disciplinas para cada aluno:
	- Se o aluno montou lista de preferência, usá-la, se não, verifica número de disciplinas semestre ativo (primeiro semestre com disciplina(s) a fazer) do aluno;
		- Com este número, selecionar uma lista de disciplinas (do menor semestre com disciplina a fazer até o maior);
	- Priorizar as disciplinas, maior prioridade para disciplinas que são pré-requisito de alguma;
	- Adicionar disciplinas possíveis ao fim da lista (menor prioridade, serão utilizadas em caso de conflitos).

### Terceira etapa:

- [ ] Criar função que gera uma lista de disciplinas que DEVEM ser ministradas baseada nos critérios abaixo:
	- Decidir a prioridade geral das disciplinas possíveis pelo número de estudantes que farão a mesma; Prioridade para alunos de segundo semestre e com mais 80% do curso;
	- Priorização por votos, alunos de segundo semestre peso 2, alunos com mais de 80% peso 5, outros peso 1;
	- Remover disciplinas com 0 votos;
	- Definir X créditos (soma total dos créditos possíveis): somar total de horas disponíveis dos professores, 1 hora = 1 crédito;
	- Por semestre é possível ter X créditos, somar número de créditos das disciplinas e verificar se é > X; se sim, remover disciplinas com < 2 votos suficientes para que se obtenha X créditos na soma total; Também é possível remover disciplinas que passem da carga horária de um professor (exemplo: Professor Blah tem 12 créditos na semana mas existem 4 disciplinas com votos, remover a que tiver menos votos).

### Quarta etapa:

- [ ] Gerador de horários
- Definir horários (intervalos) possíveis para cada disciplina pelos professores que podem ministrá-las (utilizar professor prioritário da disciplina);
- Definir o que é conflito exclusivo: disciplinas que precisam de laboratórios no mesmo horário; projetores (?) ...
	* Opção 1:
		- Montar horários (300+) desconsiderando conflitos com alunos, porém, considerando conflitos de semestre e salas (utilização do algoritmo [Given n appointments, find all conflicting appointments] ou semelhantes como [Hopcroft–Karp algorithm] e [Bipartite_matching]);
		- Dar um score para cada horário considerando os conflitos com alunos;
		- Selecionar 10 horários com menores scores de conflito;
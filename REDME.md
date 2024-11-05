HTTPX
 - bibliotéca para fazer requisições
 - criado por Tom Christie (uvicon, mkdocs, starllet, DRF, etc.)
 - API para requisições modernas assincrónas
 - versão inicial 0.0.1 - março 2015
 - O requests não está adaptado para coisas novas
 - Programação estruturada
 - Suporte para AnyIO
 - pip install httpx / poetry install httpx 
Um resumo sobre I/O
 - Bound de IO, estamos desperdiçando tempo com as entradas e saídas
 - em outras palavras, o python conversou com o sistema operacional, o OS abriu uma porta, e essa porta eestá esperando a resposta do site para a maquina
Requests assíncronos
 - escalonamento de tarefas
 - o que define onde o escalonamento é o await
 - quando ele encontra o await ele troca de tarefa
iometer
 - controlando o eventloopt
 - para que ele não faça um milhão de coisas
 - aoimeter foi criado por Florimond Manca
 - lançado em março de 2020
 - run_all (rode tudo) ele funciona diferente do gather (max_at_once, max_per_second)

RESPX -> mocks para requests
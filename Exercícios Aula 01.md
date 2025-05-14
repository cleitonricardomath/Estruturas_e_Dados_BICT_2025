# Exercícios Aula 01
Revisão Básica de Python
## Exercício 01
### Verificador de Palíndromo
* **Descrição:** Peça ao usuário para digitar uma palavra ou frase. O programa deve verificar se é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda, desconsiderando espaços e maiúsculas/minúsculas).
* **Conceitos Envolvidos:**
    * Entrada de dados: `input()`
    * Manipulação de strings: métodos como `.lower()`, `.replace()`, fatiamento `[::-1]`.
    * Estruturas condicionais: `if`, `else`.
* **Desafio Extra:** Fazer a verificação ignorando acentuação.

## Exercício 02
### Lista de Tarefas (To-Do List) Simples
* **Descrição:** Crie um programa que permita ao usuário:
    * Adicionar uma nova tarefa a uma lista.
    * Visualizar todas as tarefas na lista.
    * Remover uma tarefa da lista (pelo índice ou pelo nome).
* **Conceitos Envolvidos:**
    * Listas: criação, `append()`, `remove()`, `pop()`, iteração com `for`.
    * Loops: `while` para o menu principal.
    * Entrada de dados: `input()`
    * Estruturas condicionais para as opções do menu.
    * Funções para cada funcionalidade (adicionar, ver, remover).
* **Desafio Extra:** Permitir marcar uma tarefa como "concluída" sem removê-la, ou salvar/carregar a lista de um arquivo de texto simples (introdução básica a manipulação de arquivos).

## Exercício 03
### Gerador de Tabuada
* **Descrição:** Solicite ao usuário um número e, em seguida, exiba a tabuada de multiplicação desse número (geralmente de 1 a 10).
* **Conceitos Envolvidos:**
    * Entrada de dados: `input()`
    * Conversão de tipos: `int()`
    * Loops: `for` (usando `range()`).
    * Formatação de strings para exibir a tabuada de forma organizada.

## Exercício 04
### Contador de Vogais e Consoantes
* **Descrição:** Peça ao usuário para digitar uma frase. O programa deve contar e exibir o número de vogais e o número de consoantes na frase.
* **Conceitos Envolvidos:**
    * Entrada de dados: `input()`
    * Manipulação de strings: iteração sobre a string, método `.lower()` ou `.upper()`.
    * Estruturas condicionais para verificar se um caractere é vogal ou consoante.
    * Variáveis para contagem.
* **Desafio Extra:** Contar também espaços ou outros tipos de caracteres.

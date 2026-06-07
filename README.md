# Sistema de Atendimento em Clínicas

Trabalho desenvolvido para a disciplina **INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I**.

## Descrição

Este projeto implementa um sistema orientado a objetos em **Python** para gerenciamento de clínicas, pacientes, profissionais de saúde, atendimentos, procedimentos e pagamentos.

O sistema foi desenvolvido seguindo o padrão **MVC** e contempla as funcionalidades exigidas no enunciado do trabalho.

## Funcionalidades

### Cadastros
- Clínicas
- Pacientes
- Profissionais de saúde
- Tipos de atendimento

Para cada cadastro, o sistema permite:
- Incluir
- Listar
- Alterar
- Excluir

### Registros
- Atendimentos (e procedimentos realizados em atendimento)
- Pagamentos

Para os registros, o sistema permite:
- Incluir
- Listar
- Alterar
- Excluir

### Relatórios
- Clínicas com maior número de atendimentos
- Atendimentos mais caros e mais baratos
- Procedimentos mais realizados
- Procedimentos mais caros e mais baratos

## Regras de negócio implementadas
- Somente pacientes com mais de 18 anos completos podem realizar atendimentos de forma independente.
- Os atendimentos devem ocorrer dentro do horário de funcionamento da clínica.
- A hora de início do atendimento deve ser menor que a hora de fim.
- Os pagamentos devem ser realizados até a data do atendimento.
- Os pagamentos podem ser feitos nas modalidades:
  - Dinheiro
  - PIX
  - Cartão de crédito

## Estrutura do projeto

```bash
trabalho1/
├── main.py
├── controller/
├── model/
├── view/
└── arquivos auxiliares
```

### Organização
- `model/`: entidades do sistema
- `controller/`: logica de controle e operacoes do sistema
- `view/`: menus e interacao com o usuario no terminal
- `main.py`: ponto de entrada do sistema

## Tecnologias utilizadas
- Python
- Programacao Orientada a Objetos
- MVC
- Terminal/CLI

## Como executar

1. Abra o terminal na pasta do projeto
2. Execute o arquivo principal:

```bash
python main.py
```
## Diagrama

O projeto possui diagrama UML representando:
- Entidades do sistema
- Relacionamentos
- Herança
- Classes abstratas
- Estrutura MVC da Parte 2

## Conceitos de orientação a objetos utilizados
- Herança
- Classes abstratas
- Associação
- Agregação
- Composição
- Encapsulamento

## Observações

Este projeto foi desenvolvido com foco nas exigências do trabalho, priorizando:
- coerência com o enunciado
- funcionamento completo no terminal
- separação em MVC
- tratamento de exceções
- implementação das regras de negócio principais

## Autores
- Adhriano Machado de Oliveira
- Davi Ferreira de Souza
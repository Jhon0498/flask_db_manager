# Flask Database Manager

Aplicação web desenvolvida com **Flask** e **Python** para praticar desenvolvimento web, integração com banco de dados, formulários, relacionamentos entre tabelas e gerenciamento de usuários e funções.

Este projeto faz parte dos meus estudos de desenvolvimento de software, com foco em compreender na prática como uma aplicação Flask é estruturada e como seus componentes se comunicam com um banco de dados.

## Tecnologias

* Python
* Flask
* Flask-WTF
* SQLAlchemy
* Flask-Migrate
* SQLite
* Jinja2
* HTML5
* CSS3
* Bootstrap
* Git e GitHub

## Funcionalidades

### Cadastro de usuários

* Formulário para informar o nome do usuário.
* Campo **"What is your name?"**.
* Validação do campo utilizando Flask-WTF.
* Persistência dos usuários no banco de dados SQLite.
* Verificação para evitar o cadastro duplicado do mesmo usuário.

### Saudação personalizada

Após informar o nome, a aplicação apresenta uma saudação personalizada:

> Olá, Jhonatan!

E abaixo:

> Prazer em conhecê-lo!

Quando nenhum nome foi informado, a aplicação apresenta:

> Olá, Stranger!

### Gerenciamento de funções

Os usuários podem estar associados a funções.

As funções utilizadas no projeto incluem:

* Administrator
* Moderator
* User

Quando um novo usuário é cadastrado, ele é associado automaticamente à função **User**.

### Relacionamento entre usuários e funções

A aplicação utiliza um relacionamento entre as tabelas `users` e `roles`.

Cada usuário possui uma função por meio da chave estrangeira:

```text
users.role_id → roles.id
```

A relação permite consultar os usuários associados a cada função.

### Listagem de usuários

A aplicação apresenta uma tabela contendo:

* Nome do usuário
* Função associada

Também existe um contador com a quantidade de usuários cadastrados.

### Listagem de funções

A aplicação apresenta as funções cadastradas e os usuários associados a cada uma delas.

Também existe um contador com a quantidade de funções cadastradas.

## Estrutura do projeto

```text
flask_db_manager/
│
├── migrations/
│
├── static/
│   └── favicon.ico
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── app.py
├── forms.py
├── models.py
├── routes.py
├── requirements.txt
└── .gitignore
```

## Banco de dados

O projeto utiliza **SQLite** como banco de dados e **SQLAlchemy** para realizar a comunicação entre a aplicação e o banco.

O projeto possui dois modelos principais:

### User

Representa os usuários cadastrados.

Principais campos:

```text
id
username
role_id
```

### Role

Representa as funções dos usuários.

Principais campos:

```text
id
name
```

O relacionamento entre os modelos é realizado por meio de `role_id`.

O banco de dados local não deve ser versionado no Git.

## Formulários

Os formulários são desenvolvidos utilizando **Flask-WTF** e **WTForms**.

### NameForm

Utilizado para receber o nome do usuário:

```text
What is your name?
```

### UserForm

Utilizado para cadastro de usuários e seleção de função.

### RoleForm

Utilizado para cadastro de funções.

## Migrações

O projeto utiliza **Flask-Migrate** para controlar alterações na estrutura do banco de dados.

As migrações ficam armazenadas no diretório:

```text
migrations/
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Jhon0498/flask_db_manager.git
```

### 2. Entre no diretório

```bash
cd flask_db_manager
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
flask run
```

A aplicação estará disponível em:

```text
http://127.0.0.1:5000
```

## O que estou praticando

Este projeto está sendo utilizado para desenvolver conhecimentos em:

* Estrutura de aplicações Flask
* Rotas e views
* Templates e Jinja2
* Flask-WTF
* WTForms
* SQLAlchemy
* Modelos e relacionamentos
* Chaves estrangeiras
* SQLite
* Operações CRUD
* Flask-Migrate
* Migrações de banco de dados
* Validação de formulários
* Organização de projetos Python
* Git e GitHub

## Próximos passos

* Melhorar a interface da aplicação
* Implementar autenticação de usuários
* Adicionar controle de permissões por função
* Implementar validações adicionais
* Melhorar o tratamento de erros
* Adicionar testes automatizados
* Melhorar a documentação
* Expandir as funcionalidades de gerenciamento de usuários e funções

## Objetivo

O objetivo deste projeto é transformar conceitos estudados em prática, evoluindo gradualmente uma aplicação Flask enquanto desenvolvo minhas habilidades em:

* Python
* Flask
* Bancos de dados
* SQLAlchemy
* Desenvolvimento web
* Git e GitHub

O projeto também serve como prática para compreender como diferentes partes de uma aplicação web trabalham juntas: **formulários → rotas → modelos → banco de dados → templates**.

---


# Flask Database Manager

Aplicação web desenvolvida com **Flask** para praticar desenvolvimento web em Python, integração com banco de dados e operações CRUD.

Este projeto faz parte dos meus estudos de **Python, Flask e desenvolvimento web**, com foco em compreender como uma aplicação Flask é estruturada e como ela se comunica com um banco de dados.

## Tecnologias

* Python
* Flask
* Flask-WTF
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* Bootstrap

## Funcionalidades

* Cadastro e gerenciamento de registros
* Operações CRUD
* Integração com banco de dados SQLite
* Modelos utilizando SQLAlchemy
* Formulários com Flask-WTF
* Rotas e views com Flask
* Templates utilizando Jinja2
* Migrações de banco de dados

## Estrutura do projeto

```text
flask_db_manager/
├── migrations/
├── static/
│   └── favicon.ico
├── templates/
│   ├── base.html
│   └── index.html
├── app.py
├── forms.py
├── models.py
├── routes.py
├── requirements.txt
└── .gitignore
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Jhon0498/flask_db_manager.git
cd flask_db_manager
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
flask run
```

A aplicação estará disponível em:

```text
http://127.0.0.1:5000
```

## Banco de dados

O projeto utiliza **SQLite** como banco de dados e **SQLAlchemy** para comunicação com o banco.

O arquivo do banco de dados não é versionado no Git, pois está incluído no `.gitignore`.

## O que estou praticando

Este projeto está sendo utilizado para desenvolver conhecimentos em:

* Estrutura de aplicações Flask
* Rotas e views
* Templates e Jinja2
* Formulários com Flask-WTF
* SQLAlchemy
* Modelos e relacionamentos
* Operações CRUD
* SQLite
* Migrações de banco de dados
* Organização de projetos Python
* Git e GitHub

## Próximos passos

* [ ] Melhorar a interface
* [ ] Adicionar autenticação de usuários
* [ ] Implementar validações adicionais
* [ ] Melhorar o tratamento de erros
* [ ] Adicionar testes automatizados
* [ ] Melhorar a documentação
* [ ] Implementar novas funcionalidades de gerenciamento de dados

## Objetivo

O objetivo deste projeto é transformar conceitos estudados em **prática**, evoluindo gradualmente a aplicação enquanto desenvolvo minhas habilidades em Python, Flask, bancos de dados e desenvolvimento web.

---

Desenvolvido por **Jhonatan** como parte dos meus estudos em desenvolvimento de software.

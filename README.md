# Todo List

## Descrição

O **Todo List** é uma aplicação web desenvolvida com **Django** para gerenciamento de tarefas. O sistema permite cadastrar, visualizar, atualizar, excluir e marcar tarefas como concluídas, além de organizar as atividades por meio de tags.

O projeto tem como objetivo praticar os principais conceitos do desenvolvimento web com Django, incluindo criação de modelos, formulários, views baseadas em classes, rotas, templates e integração com banco de dados.

## Funcionalidades

* Listagem de tarefas cadastradas;
* Criação de novas tarefas;
* Edição de tarefas existentes;
* Exclusão de tarefas;
* Marcação de tarefas como concluídas ou não concluídas;
* Definição de prazo para conclusão da tarefa;
* Associação de tags às tarefas;
* Criação, edição, listagem e exclusão de tags;
* Interface simples baseada em templates Django.

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* Django Templates

## Estrutura do projeto

```text
todo-list/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Modelos principais

### Task

Representa uma tarefa cadastrada no sistema.

Principais campos:

* `content`: descrição da tarefa;
* `created_at`: data e horário de criação;
* `deadline`: prazo opcional para conclusão;
* `is_completed`: indica se a tarefa foi concluída;
* `tags`: relação com uma ou mais tags.

### Tag

Representa uma categoria ou marcador utilizado para organizar tarefas.

Principal campo:

* `name`: nome da tag.

## Como executar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/WalterMatheusgg/todo-list.git
```

### 2. Acesse a pasta do projeto

```bash
cd todo-list
```

### 3. Acesse a branch de desenvolvimento

```bash
git checkout dev
```

### 4. Crie e ative um ambiente virtual

No Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Depois, acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Rotas principais

* `/` - lista de tarefas;
* `/tasks/create/` - criação de tarefa;
* `/tags/` - lista de tags;
* `/tags/create/` - criação de tag;
* `/admin/` - painel administrativo do Django.

## Objetivo do projeto

Este projeto foi desenvolvido com finalidade educacional, buscando consolidar conhecimentos sobre desenvolvimento web com Django. A aplicação demonstra a construção de um CRUD completo, utilizando separação entre modelos, formulários, views, rotas e templates.

## Autor

Desenvolvido por **Walter Matheus**.

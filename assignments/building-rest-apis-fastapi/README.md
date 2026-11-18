# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo endpoints para consultar, criar, atualizar e excluir dados. Pratique também validação de dados com Pydantic e respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Executar a aplicação e explorar a documentação

#### Descrição
Use o código inicial para executar uma aplicação FastAPI e explore a documentação interativa gerada automaticamente.

#### Requisitos
A aplicação concluída deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Iniciar com `python starter-code.py` e ficar disponível em `http://127.0.0.1:8000`.
- Responder a uma requisição `GET /` com uma mensagem indicando que a API está em execução.
- Exibir a documentação interativa em `http://127.0.0.1:8000/docs`.

### 🛠️ Criar endpoints para consultar e adicionar tarefas

#### Descrição
Modele uma tarefa usando Pydantic e implemente endpoints para adicionar tarefas à API e consultar a lista ou uma tarefa específica. Os dados podem ficar em uma lista em memória; não é necessário usar um banco de dados.

#### Requisitos
A aplicação concluída deve:

- Definir um modelo `Task` com um título, uma descrição e um indicador `completed` que começa como `False`.
- Implementar `POST /tasks` para adicionar uma tarefa e responder com o status HTTP `201`.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Responder com status HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Atualizar e excluir tarefas

#### Descrição
Complete a API implementando operações para atualizar e excluir tarefas existentes, mantendo respostas consistentes para identificadores válidos e inválidos.

#### Requisitos
A aplicação concluída deve:

- Implementar `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente e responder com status HTTP `204`.
- Responder com status HTTP `404` ao tentar atualizar ou excluir uma tarefa inexistente.
- Permitir testar e inspecionar os endpoints pela documentação interativa em `/docs`.

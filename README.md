# 📚 API de Gerenciamento de Livros com Flask

Este projeto é uma API simples para gerenciar livros usando **Python** com **Flask**. Ela permite **listar, buscar, adicionar e atualizar livros**.

---

## 🚀 Tecnologias Utilizadas
- Python 3
- Flask (framework para APIs)
- Postman (para testar as requisições, opcional)

---

## 📂 Estrutura do Projeto
```
📁 Api_Com_Python/
│-- 📄 app.py  # Código principal da API
│-- 📄 README.md  # Documentação do projeto
```

---

## 🎯 Como Rodar a API

### 1️⃣ Instale o Flask (se ainda não tiver)
Abra o terminal e execute:
```sh
pip install flask
```

### 2️⃣ Execute a API
No terminal, na pasta do projeto, rode:
```sh
python app.py
```
Se tudo estiver correto, verá:
```
 * Running on http://127.0.0.1:5000/
```
Agora a API está rodando! 🎉

---

## 🔄 Rotas Disponíveis

### 📌 1️⃣ Listar todos os livros
**Método:** `GET`  
**URL:** `http://127.0.0.1:5000/livros`  
📌 **Resposta esperada:**
```json
[
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien"}
]
```

---

### 📌 2️⃣ Buscar um livro pelo ID
**Método:** `GET`  
**URL:** `http://127.0.0.1:5000/livros/2`  
📌 **Resposta esperada:**
```json
{"id": 2, "titulo": "1984", "autor": "George Orwell"}
```
Caso o ID **não exista**, retorna:
```json
{"erro": "Livro não encontrado"}
```

---

### 📌 3️⃣ Adicionar um novo livro
**Método:** `POST`  
**URL:** `http://127.0.0.1:5000/livros`  
**Corpo da requisição (JSON):**
```json
{
    "titulo": "A Revolução dos Bichos",
    "autor": "George Orwell"
}
```
📌 **Resposta esperada:**
```json
{
    "id": 4,
    "titulo": "A Revolução dos Bichos",
    "autor": "George Orwell"
}
```

---

### 📌 4️⃣ Atualizar um livro pelo ID
**Método:** `PUT`  
**URL:** `http://127.0.0.1:5000/livros/3`  
**Corpo da requisição (JSON):**
```json
{
    "titulo": "O Hobbit - Edição Especial",
    "autor": "J.R.R. Tolkien"
}
```
📌 **Resposta esperada:**
```json
{
    "id": 3,
    "titulo": "O Hobbit - Edição Especial",
    "autor": "J.R.R. Tolkien"
}
```
Caso o ID **não exista**, retorna:
```json
{"erro": "Livro não encontrado"}
```

---

## 📌 Observações
✅ O ID do livro é gerado automaticamente ao adicionar um novo livro.  
✅ Se tentar buscar ou atualizar um ID inexistente, retorna erro `404 Not Found`.  
✅ A API usa **JSON** para comunicação.

---

## 📜 Licença
Este projeto é de **uso livre** para estudos e melhorias. Contribuições são bem-vindas! 😃


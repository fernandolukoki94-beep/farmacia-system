# Sistema de Gestão de Farmácia

Este projeto implementa um sistema simples de gestão de farmácia com um backend em Flask (Python) e SQLite, e um frontend em HTML, CSS (Bootstrap) e JavaScript.

## Estrutura do Projeto

```
farmacia-system/
├── backend/
│   └── app.py
├── frontend/
│   └── index.html
└── README.md
```

## Backend (Flask API)

O backend é uma API RESTful desenvolvida com Flask que interage com uma base de dados SQLite. Ele fornece endpoints para:

- `GET /products`: Obter todos os produtos.
- `POST /products`: Adicionar um novo produto.
- `PUT /products/<id>`: Atualizar um produto existente.
- `DELETE /products/<id>`: Remover um produto.

### Como Executar o Backend

1. Navegue até a pasta `backend`:
   ```bash
   cd farmacia-system/backend
   ```
2. Instale as dependências (se ainda não o fez):
   ```bash
   pip install flask flask-cors
   ```
3. Execute a aplicação Flask:
   ```bash
   python app.py
   ```

O servidor estará a correr em `http://127.0.0.1:5000`.

## Frontend (HTML, CSS, JavaScript)

O frontend é uma aplicação web simples que permite visualizar, adicionar e remover produtos do inventário da farmácia. Ele consome a API RESTful fornecida pelo backend.

### Como Executar o Frontend

1. Certifique-se de que o backend está a correr.
2. Abra o ficheiro `index.html` no seu navegador web.

## Testar a API (Exemplo com `curl`)

### Adicionar um Produto

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Paracetamol", "price": 5.50, "quantity": 100}' http://127.0.0.1:5000/products
```

### Obter Todos os Produtos

```bash
curl http://127.0.0.1:5000/products
```

### Atualizar um Produto (ID 1)

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Paracetamol 500mg", "price": 6.00, "quantity": 90}' http://127.0.0.1:5000/products/1
```

### Remover um Produto (ID 1)

```bash
curl -X DELETE http://127.0.0.1:5000/products/1
```

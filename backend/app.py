from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'thisissecret'
DB = "farmacia.db"

# criar base de dados
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Decorator para proteger rotas
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token está em falta!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            conn = sqlite3.connect(DB)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (data['user_id'],))
            current_user = cursor.fetchone()
            conn.close()
        except:
            return jsonify({'message': 'Token é inválido!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Rota de registo de utilizador
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (data['username'], hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Utilizador registado com sucesso!'})
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'message': 'Nome de utilizador já existe.'}), 409

# Rota de login de utilizador
@app.route('/login', methods=['POST'])
def login_user():
    auth = request.json

    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Não foi possível verificar', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (auth['username'],))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({'message': 'Não foi possível verificar', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401

    if check_password_hash(user[2], auth['password']):
        token = jwt.encode({'user_id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'message': 'Não foi possível verificar', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401

# GET produtos
@app.route("/products", methods=["GET"])
@token_required
def get_products(current_user):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "quantity": row[3]
        })
    return jsonify(products)

# ADD produto
@app.route("/products", methods=["POST"])
@token_required
def add_product(current_user):
    data = request.json
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (data["name"], data["price"], data["quantity"])
    )

    conn.commit()
    conn.close()
    return jsonify({"message": "Produto adicionado"})

# UPDATE stock
@app.route("/products/<int:id>", methods=["PUT"])
@token_required
def update_product(current_user, id):
    data = request.json
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET name=?, price=?, quantity=? WHERE id=?",
        (data["name"], data["price"], data["quantity"], id)
    )

    conn.commit()
    conn.close()
    return jsonify({"message": "Produto atualizado"})

# DELETE produto
@app.route("/products/<int:id>", methods=["DELETE"])
@token_required
def delete_product(current_user, id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=?", (id,))

    conn.commit()
    conn.close()
    return jsonify({"message": "Produto removido"})

# RUN server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import sqlite3

conn = sqlite3.connect('demandas.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute("DROP TABLE IF EXISTS demandas")
cursor.execute("DROP TABLE IF EXISTS comentarios")

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    senha TEXT
)
""")

cursor.execute("""
CREATE TABLE demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    descricao TEXT,
    solicitante TEXT,
    data_criacao TEXT,
    prioridade TEXT
)
""")

cursor.execute("""
CREATE TABLE comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    demanda_id INTEGER,
    comentario TEXT,
    autor TEXT,
    data TEXT
)
""")

usuarios = [
    ('admin', '123'),
    ('João Silva', '123'),
    ('Maria Santos', '123'),
    ('Pedro Costa', '123')
]

cursor.executemany("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", usuarios)

conn.commit()
conn.close()

print("Banco criado!")
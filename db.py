import sqlite3

def crear_tabla():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER,
            precio REAL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()

def obtener_productos():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

def buscar_producto_por_nombre(nombre):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, categoria, precio FROM productos WHERE nombre = ?", (nombre,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def eliminar_producto(id_producto):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()

def obtener_producto_por_id(id_producto):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    """, (nombre, descripcion, cantidad, precio, categoria, id_producto))
    conn.commit()
    conn.close()

@app.route("/")
def inicio():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM inventario ORDER BY id")

    inventario = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "inventario.html",
        inventario=inventario
    )

@app.route("/")
def inicio():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM inventario ORDER BY id")

    inventario = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("inventario.html", inventario=inventario)

@app.route("/agregar", methods=["POST"])
def agregar():

    nombre = request.form["nombre"]
    precio = request.form["precio"]
    activo = request.form["activo"]
    categoria = request.form["categoria"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO inventario(nombre, precio, activo, categoria)
        VALUES(%s, %s, %s, %s)
        """,
        (nombre, precio, activo, categoria)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/")

@app.route("/editar/<int:id>")
def editar(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM inventario WHERE id=%s",
        (id,)
    )

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template("editar.html", producto=producto)

@app.route("/actualizar", methods=["POST"])
def actualizar():

    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    activo = request.form["activo"]
    categoria = request.form["categoria"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE inventario
        SET nombre=%s,
            precio=%s,
            activo=%s,
            categoria=%s
        WHERE id=%s
        """,
        (nombre, precio, activo, categoria, id)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM inventario WHERE id=%s",
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/")

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="Dias_L_M_M_J",
        user="postgres",
        password="12345"
    )

@app.route("/lunes")
def lunes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM lunes")
    actividades = cursor.fetchall()

    cursor.close()
    conexion.close()

    lista = []
    for actividad in actividades:
        lista.append({
            "id": actividad[0],
            "actividad": actividad[1]
        })

    return jsonify(lista)


@app.route("/martes")
def martes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM martes")
    actividades = cursor.fetchall()

    cursor.close()
    conexion.close()

    lista = []
    for actividad in actividades:
        lista.append({
            "id": actividad[0],
            "actividad": actividad[1]
        })

    return jsonify(lista)


@app.route("/miercoles")
def miercoles():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM miercoles")
    actividades = cursor.fetchall()

    cursor.close()
    conexion.close()

    lista = []
    for actividad in actividades:
        lista.append({
            "id": actividad[0],
            "actividad": actividad[1]
        })

    return jsonify(lista)


@app.route("/jueves")
def jueves():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM jueves")
    actividades = cursor.fetchall()

    cursor.close()
    conexion.close()

    lista = []
    for actividad in actividades:
        lista.append({
            "id": actividad[0],
            "actividad": actividad[1]
        })

    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True)
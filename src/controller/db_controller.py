from flask import Flask, request, Response


from src.app import app
from src.helpers.db_helper import crear_pueblo, crear_sitio_interes


@app.route('/crear_pueblo', methods=['POST'])
def crear_pueblo_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_pueblo = crear_pueblo(json_data)
    if response_crear_pueblo["mensaje"] == "OK":
        response = Response(response=response_crear_pueblo["mensaje"], status=200)
    else:
        response = Response(response=response_crear_pueblo["mensaje"], status=500)
    return response


@app.route('/crear_sitio_interes', methods=['POST'])
def crear_sitio_interes_controller():
    # mandamos a un metodo helper el request completo
    json_data = request.json
    response_crear_pueblo = crear_sitio_interes(json_data)
    if response_crear_pueblo["mensaje"] == "OK":
        response = Response(response=response_crear_pueblo["mensaje"], status=200)
    else:
        response = Response(response=response_crear_pueblo["mensaje"], status=500)
    return response
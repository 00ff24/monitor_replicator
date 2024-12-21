import os
import re
import time
import subprocess
import threading
import socket
from datetime import datetime
from flask import Flask, render_template_string, render_template

app = Flask(__name__)

# Función para obtener el hostname
def obtener_ip_local():
    try:
        return socket.gethostname()
    except Exception:
        return "No se pudo obtener hostname"

@app.route("/")
def home():
    hostname = obtener_ip_local()
    # Datos para la tabla: Lista de diccionarios (puedes cargar estos datos dinámicamente)
    data = [
        {"col1": "Dato 1A", "col2": "Dato 1B", "col3": "Dato 1C", "col4": "Dato 1D", "col5": "Dato 1E"},
        {"col1": "Dato 2A", "col2": "Dato 2B", "col3": "Dato 2C", "col4": "Dato 2D", "col5": "Dato 2E"},
        {"col1": "Dato 3A", "col2": "Dato 3B", "col3": "Dato 3C", "col4": "Dato 3D", "col5": "Dato 3E"},
    ]
    return render_template("index.html", table_data=data, hostname=hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
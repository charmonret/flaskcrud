from flask import Flask
from contacts import contacts

# Inicialización de la aplicación
app = Flask(__name__)

# Configuraciones
app.secret_key = "mysecretkey"

# Registro del Blueprint para activar las rutas de contactos
app.register_blueprint(contacts)
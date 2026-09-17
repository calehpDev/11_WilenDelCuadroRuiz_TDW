import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Cargar configuraciones desde config.py
    app.config.from_object('app.config.Config')

    # Crear la carpeta de subidas si no existe
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Registrar Blueprints (Rutas)
    from app.routes.productos import productos_bp
    app.register_blueprint(productos_bp)

    # Ruta de redirección o bienvenida raíz
    @app.route('/')
    def index():
        from flask import redirect, url_for
        return redirect(url_for('productos.index'))

    return app
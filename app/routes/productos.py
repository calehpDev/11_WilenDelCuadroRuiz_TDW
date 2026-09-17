import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.services.imagen_service import optimizar_y_guardar_imagen

# La variable debe llamarse EXACTAMENTE igual que la importación
productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/')
def index():
    return render_template('productos/index.html')

@productos_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        file = request.files.get('imagen')
        if file:
            upload_path = os.path.join(current_app.root_path, 'static', 'uploads')
            nombre_opt = optimizar_y_guardar_imagen(file, upload_path)
            return redirect(url_for('productos.index'))
    return render_template('productos/form.html')
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('form-producto');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    const inputImagen = document.getElementById('imagen');
    const file = inputImagen.files[0];

    if (!file) {
      alert('Por favor selecciona una imagen.');
      e.preventDefault();
      return;
    }

    // Validar formato
    const tiposPermitidos = ['image/jpeg', 'image/png', 'image/webp'];
    if (!tiposPermitidos.includes(file.type)) {
      alert('Solo se permiten archivos JPG, PNG o WEBP.');
      e.preventDefault();
      return;
    }

    // Validar tamaño máximo (2MB)
    if (file.size > 2 * 1024 * 1024) {
      alert('La imagen no debe superar los 2MB.');
      e.preventDefault();
    }
  });
});
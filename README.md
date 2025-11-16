# Proyecto Flask con CI/CD

## Descripción

Esta es una aplicación web simple construida con Flask que despliega un mensaje de "¡Hola Mundo desde Flask con Traefik!". La aplicación está contenerizada con Docker y utiliza un pipeline de CI/CD para automatizar pruebas, construcción y despliegue.

## Ciclo de CI/CD

El ciclo de Integración Continua (CI) y Despliegue Continuo (CD) es un proceso automatizado que permite integrar cambios de código de manera frecuente y confiable, asegurando que el software esté siempre listo para producción.

### Integración Continua (CI)
La CI se enfoca en automatizar la integración de cambios de código de múltiples colaboradores. Incluye:
- **Compilación automática**: Verificar que el código compile sin errores.
- **Ejecución de pruebas**: Ejecutar pruebas unitarias, de integración y funcionales para detectar bugs temprano.
- **Análisis de código**: Revisar calidad del código, cobertura de pruebas y vulnerabilidades.
- **Feedback rápido**: Notificar a los desarrolladores sobre fallos inmediatamente.

En este proyecto, la CI se implementa mediante GitHub Actions, que ejecuta las pruebas automáticamente al hacer push a la rama `david`.

### Despliegue Continuo (CD)
El CD automatiza el proceso de liberación del software a producción. Incluye:
- **Construcción de artefactos**: Crear paquetes o imágenes listas para despliegue (en este caso, una imagen Docker).
- **Despliegue automático**: Publicar la aplicación en el entorno de producción.
- **Monitoreo**: Verificar que el despliegue sea exitoso.

En este proyecto, el CD construye y empuja la imagen Docker a GitHub Container Registry (GHCR) después de pasar las pruebas.

### Flujo Completo del Pipeline
1. **Desarrollador hace commit**: Cambios locales se confirman en Git.
2. **Push al repositorio**: Los cambios se suben a GitHub.
3. **Trigger del workflow**: GitHub Actions detecta el push y inicia el pipeline.
4. **Instalación de dependencias**: Se instalan las librerías requeridas.
5. **Ejecución de pruebas**: Se corren las pruebas unitarias con pytest.
6. **Construcción del paquete**: Si las pruebas pasan, se construye la imagen Docker.
7. **Despliegue**: La imagen se empuja a GHCR, lista para ser desplegada con Docker Compose o Kubernetes.

### Ejemplo Práctico
Supongamos que queremos agregar una nueva ruta a la aplicación.

1. **Clona el repositorio**:
   ```
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. **Crea una nueva rama** (opcional pero recomendado):
   ```
   git checkout -b feature/nueva-ruta
   ```

3. **Edita el código**: Modifica `app.py` para agregar una nueva ruta, por ejemplo:
   ```python
   @app.route('/saludo')
   def saludo():
       return "¡Hola desde la nueva ruta!"
   ```

4. **Agrega pruebas**: Actualiza `test_app.py` para incluir una prueba para la nueva ruta:
   ```python
   def test_saludo():
       with app.test_client() as client:
           response = client.get('/saludo')
           assert response.status_code == 200
           assert "¡Hola desde la nueva ruta!" in response.get_data(as_text=True)
   ```

5. **Ejecuta pruebas localmente**:
   ```
   python -m pytest
   ```

6. **Commit y push**:
   ```
   git add .
   git commit -m "Agrega nueva ruta /saludo con pruebas"
   git push origin feature/nueva-ruta
   ```

7. **Crea un Pull Request**: En GitHub, crea un PR para fusionar a la rama principal.

8. **El pipeline se ejecuta**: GitHub Actions ejecutará automáticamente:
   - Instalación de dependencias
   - Ejecución de pruebas (incluyendo la nueva)
   - Si pasan, construcción y push de la imagen Docker

9. **Despliegue**: Una vez aprobado el PR, el pipeline en la rama principal desplegará la nueva versión.

Este proceso asegura que cualquier cambio pase por pruebas antes de llegar a producción, reduciendo errores y mejorando la calidad del software.

## Autor
David Cocha

LINK DE DESPLIEGUE : https://david-cocha.onrender.com/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola Mundo desde Flask con Traefik! 🚀"

def suma(a, b):
    """Función que suma dos números"""
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
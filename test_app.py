import pytest
from app import app, suma

def test_hello():
    """Prueba unitaria para la ruta principal '/'"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert "¡Hola Mundo desde Flask con Traefik!" in response.get_data(as_text=True)

def test_suma():
    """Prueba unitaria para la función suma"""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
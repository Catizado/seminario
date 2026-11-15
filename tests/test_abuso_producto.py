import pytest

from app.errores import ProductoInvalidoError
from app.registrar_salida import registrar_salida


@pytest.mark.parametrize(
    "producto",
    [
        None,
        {},
        {"cantidad_actual": 3},
        {"id": 1, "cantidad_actual": None},
        {"id": 1, "cantidad_actual": 2.5},
        {"id": 1, "cantidad_actual": "3"},
        {"id": 1, "cantidad_actual": -1},
        {"id": 1, "cantidad_actual": True},
        {"id": 1, "cantidad_actual": False},
    ],
    ids=[
        "none",
        "vacio",
        "sin-id",
        "existencias-none",
        "existencias-decimales",
        "existencias-texto",
        "existencias-negativas",
        "existencias-bool-true",
        "existencias-bool-false",
    ],
)
def test_producto_invalido_se_rechaza(producto):
    with pytest.raises(ProductoInvalidoError, match="El producto no es válido"):
        registrar_salida(producto, 1)

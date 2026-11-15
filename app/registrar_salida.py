from app.errores import (
    CantidadInvalidaError,
    ExistenciasInsuficientesError,
    ProductoInvalidoError,
)

TIPO_SALIDA = "salida"
CLAVE_ID = "id"
CLAVE_CANTIDAD_ACTUAL = "cantidad_actual"


def _validar_producto(producto):
    if not isinstance(producto, dict):
        raise ProductoInvalidoError()

    if CLAVE_ID not in producto or CLAVE_CANTIDAD_ACTUAL not in producto:
        raise ProductoInvalidoError()

    cantidad_actual = producto[CLAVE_CANTIDAD_ACTUAL]
    es_entero = isinstance(cantidad_actual, int) and not isinstance(
        cantidad_actual, bool
    )
    if not es_entero or cantidad_actual < 0:
        raise ProductoInvalidoError()


def _validar_cantidad(cantidad):
    es_entero = isinstance(cantidad, int) and not isinstance(cantidad, bool)
    if not es_entero or cantidad <= 0:
        raise CantidadInvalidaError()


def _validar_existencias(producto, cantidad):
    if cantidad > producto[CLAVE_CANTIDAD_ACTUAL]:
        raise ExistenciasInsuficientesError()


def registrar_salida(producto: dict, cantidad: int) -> dict:
    _validar_producto(producto)
    _validar_cantidad(cantidad)
    _validar_existencias(producto, cantidad)

    producto_actualizado = {
        **producto,
        CLAVE_CANTIDAD_ACTUAL: producto[CLAVE_CANTIDAD_ACTUAL] - cantidad,
    }
    movimiento = {
        "producto_id": producto[CLAVE_ID],
        "tipo": TIPO_SALIDA,
        "cantidad": cantidad,
    }
    return {"producto": producto_actualizado, "movimiento": movimiento}

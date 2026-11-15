from app.errores import CantidadInvalidaError, ExistenciasInsuficientesError

TIPO_SALIDA = "salida"
CLAVE_ID = "id"
CLAVE_CANTIDAD_ACTUAL = "cantidad_actual"


def _validar_cantidad(cantidad):
    es_entero = isinstance(cantidad, int) and not isinstance(cantidad, bool)
    if not es_entero or cantidad <= 0:
        raise CantidadInvalidaError()


def _validar_existencias(producto, cantidad):
    if cantidad > producto[CLAVE_CANTIDAD_ACTUAL]:
        raise ExistenciasInsuficientesError()


def registrar_salida(producto, cantidad):
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

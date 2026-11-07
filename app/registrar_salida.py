from app.errores import CantidadInvalidaError, ExistenciasInsuficientesError

TIPO_SALIDA = "salida"


def _validar_cantidad(cantidad):
    es_entero = isinstance(cantidad, int) and not isinstance(cantidad, bool)
    if not es_entero or cantidad <= 0:
        raise CantidadInvalidaError()


def _validar_existencias(producto, cantidad):
    if cantidad > producto["cantidad_actual"]:
        raise ExistenciasInsuficientesError()


def registrar_salida(producto, cantidad):
    _validar_cantidad(cantidad)
    _validar_existencias(producto, cantidad)

    producto_actualizado = {
        **producto,
        "cantidad_actual": producto["cantidad_actual"] - cantidad,
    }
    movimiento = {
        "producto_id": producto["id"],
        "tipo": TIPO_SALIDA,
        "cantidad": cantidad,
    }
    return {"producto": producto_actualizado, "movimiento": movimiento}

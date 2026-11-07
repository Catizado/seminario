class CantidadInvalidaError(Exception):
    def __init__(self):
        super().__init__("La cantidad debe ser mayor que cero")


class ExistenciasInsuficientesError(Exception):
    def __init__(self):
        super().__init__("No hay suficientes existencias")


def registrar_salida(producto, cantidad):
    if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
        raise CantidadInvalidaError()
    if cantidad > producto["cantidad_actual"]:
        raise ExistenciasInsuficientesError()
    return {
        "producto": {**producto, "cantidad_actual": producto["cantidad_actual"] - cantidad},
        "movimiento": {"producto_id": producto["id"], "tipo": "salida", "cantidad": cantidad},
    }

from app.errores import (
    CantidadInvalidaError,
    ExistenciasInsuficientesError,
    ProductoInvalidoError,
)

TIPO_SALIDA = "salida"
CLAVE_ID = "id"
CLAVE_CANTIDAD_ACTUAL = "cantidad_actual"


def _validar_producto(producto):
    """Valida las claves requeridas y las existencias del producto.

    Args:
        producto: Valor que debe ser un diccionario con ``id`` y
            ``cantidad_actual``.

    Returns:
        None: Si el producto cumple las reglas de validación.

    Raises:
        ProductoInvalidoError: Si el valor no es un diccionario, le falta una
            clave requerida o ``cantidad_actual`` no es un entero no negativo
            distinto de bool.
    """
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
    """Calcula la salida de existencias y el movimiento correspondiente.

    Args:
        producto: Diccionario con ``id`` y ``cantidad_actual`` entero no
            negativo.
        cantidad: Número entero positivo de unidades que salen.

    Returns:
        Diccionario con una copia actualizada del producto y el movimiento.

    Raises:
        ProductoInvalidoError: Si el producto no cumple la validación.
        CantidadInvalidaError: Si ``cantidad`` no es un entero positivo
            distinto de bool.
        ExistenciasInsuficientesError: Si la salida supera las existencias.
    """
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

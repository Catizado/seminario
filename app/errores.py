class CantidadInvalidaError(Exception):
    def __init__(self):
        super().__init__("La cantidad debe ser mayor que cero")


class ExistenciasInsuficientesError(Exception):
    def __init__(self):
        super().__init__("No hay suficientes existencias")


class ProductoInvalidoError(Exception):
    def __init__(self):
        super().__init__("El producto no es válido")

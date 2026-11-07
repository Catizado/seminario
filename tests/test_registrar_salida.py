import pytest

from app.registrar_salida import (
    CantidadInvalidaError,
    ExistenciasInsuficientesError,
    registrar_salida,
)


def arroz(cantidad_actual):
    return {"id": 1, "nombre": "Arroz 500 g", "cantidad_actual": cantidad_actual, "stock_minimo": 5}


# Casos normales

def test_salida_de_5_con_30_unidades_deja_25():
    resultado = registrar_salida(arroz(30), 5)
    assert resultado["producto"]["cantidad_actual"] == 25


def test_devuelve_el_movimiento_de_tipo_salida():
    resultado = registrar_salida(arroz(30), 5)
    assert resultado["movimiento"] == {"producto_id": 1, "tipo": "salida", "cantidad": 5}


# Casos límite

def test_salida_igual_a_las_existencias_deja_el_producto_en_0():
    resultado = registrar_salida(arroz(25), 25)
    assert resultado["producto"]["cantidad_actual"] == 0


def test_salida_de_una_sola_unidad_es_valida():
    resultado = registrar_salida(arroz(25), 1)
    assert resultado["producto"]["cantidad_actual"] == 24


def test_salida_de_existencias_mas_uno_se_rechaza():
    with pytest.raises(ExistenciasInsuficientesError):
        registrar_salida(arroz(25), 26)


# Casos de error

def test_salida_mayor_que_las_existencias_dice_no_hay_suficientes_existencias():
    with pytest.raises(ExistenciasInsuficientesError, match="No hay suficientes existencias"):
        registrar_salida(arroz(25), 30)


def test_cantidad_cero_se_rechaza():
    with pytest.raises(CantidadInvalidaError, match="La cantidad debe ser mayor que cero"):
        registrar_salida(arroz(25), 0)


def test_cantidad_negativa_se_rechaza():
    with pytest.raises(CantidadInvalidaError):
        registrar_salida(arroz(25), -3)


def test_cantidad_decimal_se_rechaza():
    with pytest.raises(CantidadInvalidaError):
        registrar_salida(arroz(25), 2.5)


# Efectos secundarios

def test_no_modifica_el_producto_original():
    original = arroz(30)
    registrar_salida(original, 5)
    assert original["cantidad_actual"] == 30

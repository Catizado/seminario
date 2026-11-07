# Inventario para tiendas de barrio

Sistema web de control de inventario para tiendas de barrio (React, Node.js y MySQL).
Este repositorio contiene la primera funcionalidad del proyecto final, con sus pruebas.

## Funcionalidad de la semana 5

### Historia de usuario

**HU-04.** Como dueño de la tienda, quiero registrar la salida de mercancía para que las existencias reflejen lo que realmente queda. Prioridad: Must.

**Criterio de aceptación**

- Escenario 1. Dado que «Arroz 500 g» tiene 30 unidades, cuando registra una salida de 5, entonces el producto queda con 25 unidades.
- Escenario 2 (error). Dado que el producto tiene 25 unidades, cuando intenta registrar una salida de 30, entonces no se guarda y aparece «No hay suficientes existencias».

Esta historia protege el requisito RNF-04: las existencias nunca pueden quedar en negativo.

### Contrato

Archivo: `app/registrar_salida.py`

```python
def registrar_salida(producto: dict, cantidad: int) -> dict:
    ...
```

**Qué recibe.**

- `producto`: un diccionario con las claves `id` (int), `nombre` (str), `cantidad_actual` (int, mayor o igual que 0) y `stock_minimo` (int).
- `cantidad`: un entero mayor que cero con las unidades que salen.

**Qué devuelve.** Un diccionario con dos claves:

- `producto`: una copia del producto con `cantidad_actual` ya descontada.
- `movimiento`: `{"producto_id": int, "tipo": "salida", "cantidad": int}`, que se debe guardar.

No modifica el producto que recibe.

**Errores.**

- `CantidadInvalidaError` con el mensaje «La cantidad debe ser mayor que cero», si la cantidad es 0, negativa, decimal o no es un entero.
- `ExistenciasInsuficientesError` con el mensaje «No hay suficientes existencias», si la cantidad es mayor que las existencias. La API lo traducirá a un código 409.

**Supuestos.**

- La función solo aplica la regla de negocio. No lee ni escribe en la base de datos; eso lo hace la API en una transacción (ver documento de diseño, ADR-001).
- Las existencias y la cantidad son números enteros.

**Casos límite.**

- Salida igual a las existencias: es válida y deja el producto en 0.
- Salida de una sola unidad: es el mínimo permitido.
- Salida de existencias + 1: es un error.
- Cantidad 0, negativa o decimal: es un error.

**Ejemplos**

| Entrada | Salida |
|---|---|
| `registrar_salida({"id": 1, "nombre": "Arroz 500 g", "cantidad_actual": 30, "stock_minimo": 5}, 5)` | `{"producto": {..., "cantidad_actual": 25}, "movimiento": {"producto_id": 1, "tipo": "salida", "cantidad": 5}}` |
| `registrar_salida({"id": 1, "nombre": "Arroz 500 g", "cantidad_actual": 25, "stock_minimo": 5}, 25)` | `{"producto": {..., "cantidad_actual": 0}, "movimiento": {"producto_id": 1, "tipo": "salida", "cantidad": 25}}` |
| `registrar_salida({"id": 1, "nombre": "Arroz 500 g", "cantidad_actual": 25, "stock_minimo": 5}, 30)` | Lanza `ExistenciasInsuficientesError`: «No hay suficientes existencias» |

### Cómo ejecutar las pruebas

Requiere Python 3.9 o superior.

```
pip install -r requirements.txt
pytest
```

## Estructura

```
app/     código de la funcionalidad
tests/   pruebas
bitacora_ia.md   bitácora de uso de IA
```

# Inventario para tiendas de barrio

## 1. Qué es

Este repositorio contiene HU-04: la función Python `registrar_salida`, que
calcula la salida de mercancía y el movimiento correspondiente sin modificar
el producto original.

El diseño completo del sistema con React, Node.js, MySQL y una API REST está
previsto, pero todavía no existe en este repositorio. La función actual no
conecta con una base de datos ni persiste movimientos.

### Contrato de `registrar_salida`

```python
def registrar_salida(producto: dict, cantidad: int) -> dict:
    ...
```

- **Recibe:** un diccionario de producto con `id`, `nombre`,
  `cantidad_actual` y `stock_minimo`; `cantidad` debe ser un entero positivo.
  La implementación valida que el producto sea un diccionario, tenga las
  claves `id` y `cantidad_actual`, y que las existencias sean un entero no
  negativo distinto de `bool`. `cantidad` también debe ser un entero distinto
  de `bool`.
- **Devuelve:** un diccionario con `producto` (copia con las existencias
  descontadas) y `movimiento` (`producto_id`, `tipo: "salida"` y `cantidad`).
- **Errores:** `ProductoInvalidoError` si el producto no cumple la validación;
  `CantidadInvalidaError` si la cantidad no es un entero positivo; y
  `ExistenciasInsuficientesError` si la salida supera las existencias.

## 2. Requisitos

- Python 3.10 o superior.
- pytest 9.2.0, fijado en `requirements.txt`.

## 3. Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual e instala las
dependencias.

**Windows PowerShell** (con Python en la ruta indicada):

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**Linux o macOS:**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 4. Ejecución

La función se puede importar y ejecutar directamente; no inicia un servidor:

```sh
python -c "from app.registrar_salida import registrar_salida; p={'id': 1, 'nombre': 'Arroz', 'cantidad_actual': 30, 'stock_minimo': 5}; print(registrar_salida(p, 5))"
```

## 5. Pruebas

Con el entorno virtual activado, ejecuta:

```sh
pytest
```

## 6. Estructura

```text
app/
  errores.py
  registrar_salida.py
tests/
  test_abuso_producto.py
  test_registrar_salida.py
requirements.txt
pytest.ini
pyproject.toml
.env.example
.gitignore
bitacora_ia.md
README.md
```

`.env.example` solo indica que actualmente el proyecto no usa secretos; la
función no lee variables de entorno.

## 7. Uso de IA

Las interacciones y decisiones de uso de IA están registradas en
`bitacora_ia.md`.

## 8. Autor y licencia

- **Autor:** Emanuel Catizado Artunduaga.
- **Institución:** Fundación Escuela Tecnológica de Neiva.
- **Docente:** Jorge Trujillo.
- **Licencia:** este repositorio no especifica una licencia.

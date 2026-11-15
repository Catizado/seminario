# Informe de revisión de código y seguridad

- **Proyecto:** Sistema de control de inventario para tiendas de barrio.
- **Estudiante:** Emanuel Catizado Artunduaga.
- **Fecha:** 2026-11-14.
- **Commit revisado:** `ece82ec7254671e576a9d17458c25d74f58fc49d` (último de `main` antes de `cb1b46b`).

## 1. Herramientas y criterios

- **Linter:** Ruff 0.17.5, reglas E, F, B, S; configurado en `pyproject.toml`.
- **Dependencias:** `pip-audit` encontró 12 avisos en `pip 25.0.1`, componente de la herramienta, no del proyecto. Se actualizó a 26.3; auditoría limpia.
- **Criterios:** corrección y pruebas, diseño y legibilidad, seguridad.
- **Revisión con IA:** análisis de código y seguridad de la semana 6; ver [bitacora_ia.md](./bitacora_ia.md).

### Puntos de seguridad revisados

| Punto | ¿Aplica? | Resultado |
|---|---|---|
| Inyección | No: no hay base de datos ni consultas. | Sin superficie de inyección en el código presente. |
| Secretos | Sí. | Historial revisado, sin hallazgos. El patrón que bloqueaba `.env.example` se corrigió en H-04. |
| Contraseñas | No: no hay autenticación ni almacenamiento de contraseñas. | No aplica. |
| Control de acceso | No: no hay roles; el diseño contempla un único usuario, el dueño. | No aplica al código actual. |
| Dependencias | Sí. | `pytest==9.2.0`; `pip-audit` limpio tras actualizar la herramienta. Ver H-01. |

## 2. Tabla de hallazgos

| Id | Archivo y línea | Problema | Categoría | Severidad | Corrección | Commit |
|---|---|---|---|---|---|---|
| H-01 | `requirements.txt:1` | `pytest>=7` no fijaba versión. | A06 Componentes desactualizados | Baja | Fijar `pytest==9.2.0`. | `965141f` |
| H-02 | `app/registrar_salida.py:12–23` | El producto no se validaba; entradas inválidas podían fallar con excepciones nativas o dejar existencias decimales. | Validación de entradas | Media | Validar producto y agregar pruebas de abuso. | `8234055` |
| H-03 | `app/registrar_salida.py:17` | La función carecía de anotaciones y docstring. | Mantenibilidad | Baja | Agregar anotaciones y docstrings. | `8895334`, `a35438c` |
| H-04 | `.gitignore:2` | `.env.*` ignoraba `.env.example`, que no existía. | Secretos | Baja | Agregar ejemplo sin secretos y excepción de ignorado. | `981e3a3` |
| H-05 | `README.md:3,43,47` | Describía React, Node.js, MySQL y una API REST que no existen en el repo. | Documentación | Baja | Aclarar el alcance real y el diseño previsto. | `2a69728` |
| H-06 | `tests/test_registrar_salida.py:11,23,46,51` | Líneas largas (E501). | Estilo | Baja | Dividir las líneas. | `9579a89` |
| H-07 | `app/registrar_salida.py:13,23` | La clave `cantidad_actual` se repetía como cadena literal. | Mantenibilidad | Baja | Usar constantes para las claves del producto. | `2683abd` |

### Avisos del linter no corregidos

| Regla | Archivo y línea | Por qué se mantiene |
|---|---|---|
| S101 | `tests/`, 5 usos de `assert` | Es la forma normal de comprobar resultados en pytest; se ignora solo en `test_*.py` (`ea55946`). |

## 3. Revisión con IA

| Hallazgo de la IA | ¿Real o falso positivo? | Cómo lo verifiqué |
|---|---|---|
| H-02: producto sin validar. | Real. | En la versión revisada, `None` producía `TypeError`, `{}` producía `KeyError` y existencias `5.5` podían dejar `3.5`. |
| H-03: faltaban anotaciones y docstring. | Real. | La firma y el cuerpo de la versión revisada no incluían esos elementos. |
| H-05: README no coincidía con el repo. | Real. | Comparé el README con la estructura y el código disponibles. |

**Lo que la IA no encontró:** H-01, `pytest>=7` sin versión fijada, y H-04, el patrón `.env.*` que impedía incluir `.env.example`.

## 4. Pendientes

| Pendiente | Por qué no se corrigió todavía | Plan |
|---|---|---|
| Integrar HU-04 con la API REST y el diseño React/Node.js/MySQL. | Esos componentes todavía no existen en este repo; la HU-04 del seminario está implementada en Python. | Desarrollarlos e integrar la regla de negocio en una etapa posterior. |

**Claves expuestas:** Ninguna.

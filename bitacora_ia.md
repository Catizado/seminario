# Bitácora de uso de IA

Proyecto: Sistema web de control de inventario para tiendas de barrio
Estudiante: Emanuel Catizado Artunduaga
Funcionalidad: HU-04 Registrar la salida de mercancía
Asistente usado: Claude (Anthropic), modo chat; en la semana 6 también se usó el asistente de VS Code en modo agente, en una rama propia.

## Entradas

### Entrada 1

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** envié el PDF de la tarea con el mensaje «ahi ta el otro trabajo pa q toca hacer ff». El asistente propuso la HU-04, registrar la salida de mercancía, como la historia Must para esta tarea.
- **Decisión:** Aceptada
- **Por qué:** es una función pequeña con casos límite claros y un escenario de error en su criterio de aceptación («No hay suficientes existencias»). Además protege RNF-04.
- **Verificación:** comparé los dos escenarios de la HU-04 de mi documento de requisitos con el contrato del README.
- **Commit relacionado:** Contrato de registrar_salida (HU-04) y estructura inicial (5974678)

### Entrada 2

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente había hecho una primera versión de esta funcionalidad en JavaScript (Node), porque la tarea permite usar el marco de pruebas del lenguaje del proyecto. Yo le escribí: «pero si toca usar pyton segun el profe».
- **Decisión:** Rechazada (la versión en JavaScript)
- **Por qué:** el profesor pidió Python, así que rehicimos la funcionalidad con pytest. Como la función solo aplica la regla de negocio y no toca la base de datos, la misma lógica se puede llevar después al servidor Node.js de mi ADR-001.
- **Verificación:** reconstruí el repositorio desde cero con el flujo completo (contrato, pruebas en rojo, verde y refactor) y ejecuté `pytest` con 10 pruebas.
- **Commit relacionado:** Contrato de registrar_salida (HU-04) y estructura inicial (5974678)

### Entrada 3

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente propuso escribir antes de la implementación una lista de 10 pruebas: 2 normales, 3 de límite, 4 de error y 1 para comprobar que no se modifica el producto original.
- **Decisión:** Aceptada
- **Por qué:** cumple lo que pide la tarea (2 normales, 2 de límite y 1 de error) y agrega los casos de existencias + 1, decimal y no modificar el original.
- **Verificación:** ejecuté `pytest` sin implementación. Falló la colección de pruebas, porque el módulo `app.registrar_salida` no existía (0 pruebas pasaron).
- **Commit relacionado:** Pruebas de registrar_salida (en rojo) (02cc500)

### Entrada 4

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente consideró hacer que `registrar_salida` lea y escriba directamente en MySQL.
- **Decisión:** Rechazada
- **Por qué:** mi ADR-001 pone la transacción en la API. La función solo debe aplicar la regla de negocio, para poder probarla sin base de datos.
- **Verificación:** las 10 pruebas corren sin base de datos y en menos de un segundo.
- **Commit relacionado:** Implementación de registrar_salida (pruebas en verde) (11576c8)

### Entrada 5

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente escribió la implementación de `registrar_salida` con el contrato y las pruebas como contexto.
- **Decisión:** Aceptada
- **Por qué:** cumple el contrato: valida la cantidad, valida las existencias y devuelve el producto actualizado y el movimiento sin modificar el original. También rechaza los valores booleanos, que en Python cuentan como enteros.
- **Verificación:** leí el código línea por línea y ejecuté `pytest`: 10 de 10 pruebas pasaron. Esas mismas pruebas habían fallado antes de escribir el código.
- **Commit relacionado:** Implementación de registrar_salida (pruebas en verde) (11576c8)

### Entrada 6

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente propuso limpiar la primera implementación: separar los errores, darle nombre a las validaciones y quitar el texto suelto `"salida"`.
- **Decisión:** Aceptada con cambios
- **Por qué:** acepté separar los errores en `errores.py`, crear `_validar_cantidad` y `_validar_existencias` y usar la constante `TIPO_SALIDA`. El código queda más fácil de leer y los errores se pueden reutilizar.
- **Verificación:** `git diff` no muestra cambios en `tests/` y `pytest` sigue dando 10 de 10.
- **Commit relacionado:** Refactor de registrar_salida: errores aparte, validaciones con nombre y constante TIPO_SALIDA (69861a3)

### Entrada 7

- **Fecha:** 2026-11-07
- **Prompt o sugerencia:** el asistente consideró convertir el producto en una clase (por ejemplo, con `dataclass`) con un método `salida()`.
- **Decisión:** Rechazada
- **Por qué:** en mi modelo de datos el producto es una fila con sus campos, y la tarea pide una función pequeña. La clase agrega estructura que hoy no hace falta.
- **Verificación:** revisé que el contrato y las 10 pruebas se cumplen con la función sola.
- **Commit relacionado:** Refactor de registrar_salida: errores aparte, validaciones con nombre y constante TIPO_SALIDA (69861a3)

### Entrada 8

- **Fecha:** 2026-11-14
- **Prompt o sugerencia:** pedí al asistente de VS Code una segunda revisión del código, sin corregir nada, con una tabla de archivo, línea, problema, categoría y severidad, separando problemas seguros de sospechas. Marcó como seguro la falta de anotaciones de tipo (`registrar_salida.py:17`), como sospecha que `producto` no se valida (líneas 12 a 26) y como inconsistencia que el README describía React, Node.js y MySQL. Dijo que no había otros problemas.
- **Decisión:** Aceptada con cambios
- **Por qué:** acepté los tres hallazgos como reales. Traté la sospecha de `producto` como real, aunque la IA la dejó fuera del contrato, porque mi modelo de datos dice que `cantidad_actual` es un entero y una entrada inválida rompe la función con `TypeError` o `KeyError`. Además agregué dos hallazgos que la IA no encontró: `pytest>=7` sin versión fijada y el patrón `.env.*` del `.gitignore`, que habría bloqueado el `.env.example`.
- **Verificación:** antes de cambiar nada corrí `pytest` (10 pasaron), `ruff` (9 avisos) y `pip-audit`. Abrí la versión anterior de `registrar_salida.py` y confirmé que no había ninguna comprobación sobre `producto`. Revisé el historial de Git y no encontré claves.
- **Commit relacionado:** Agrega informe de revisión de seguridad (11caf17)

### Entrada 9

- **Fecha:** 2026-11-14
- **Prompt o sugerencia:** para corregir la validación de `producto`, el primer prompt que preparé con Claude reutilizaba el error de cantidad inválida. Lo cambié antes de enviarlo: pedí un error nuevo, `ProductoInvalidoError`, y una función `_validar_producto` que se llame primero en `registrar_salida`.
- **Decisión:** Aceptada con cambios
- **Por qué:** reutilizar el error de cantidad habría mostrado «La cantidad debe ser mayor que cero» cuando el problema es el producto. La validación exige un diccionario con `id` y `cantidad_actual`, y que las existencias sean un entero (sin contar booleanos) mayor o igual que 0. Esto cambia un comportamiento: unas existencias negativas antes daban `ExistenciasInsuficientesError` y ahora dan `ProductoInvalidoError`. Por eso agregué pruebas nuevas.
- **Verificación:** `pytest` pasó con 19 pruebas (las 10 anteriores y 9 nuevas en `tests/test_abuso_producto.py`) y `ruff` quedó sin avisos.
- **Commit relacionado:** Valida producto en registrar_salida y agrega pruebas de abuso (8234055)

### Entrada 10

- **Fecha:** 2026-11-14
- **Prompt o sugerencia:** puse al asistente de VS Code en modo agente, en la rama `semana6-revision`, con instrucciones delimitadas y un commit por cambio: fijar `pytest` (965141f), constantes para las claves del producto (2683abd), anotaciones de tipo (8895334), la validación de `producto` (8234055), docstrings (a35438c) y el README (2a69728). Le prohibí modificar las pruebas existentes.
- **Decisión:** Aceptada
- **Por qué:** cada cambio quedó en su propio commit y puedo explicarlo, y la rama protege `main` si algo sale mal.
- **Verificación:** `pytest` pasó después de cada cambio. Revisé el diff entre `main` y la rama: lo único que cambió en `tests/test_registrar_salida.py` es el formato de las líneas largas (E501, commit 9579a89), sin cambiar ningún `assert` ni valor.
- **Commit relacionado:** Agrega docstrings (a35438c)

## Resumen

| Decisión | Cantidad |
|---|---|
| Aceptadas | 4 |
| Aceptadas con cambios | 3 |
| Rechazadas | 3 |

## Errores que atraparon las pruebas

El código generado por el asistente no tuvo errores que las pruebas detectaran: las 10 pasaron en la primera ejecución. Por eso no tengo un error real del código generado que reportar.

Para comprobar que las pruebas sí detectan fallas, hice tres cambios deliberados en una copia del código, ejecuté `pytest` y volví a dejar el código original. Cada cambio hizo fallar una prueba distinta:

| Cambio deliberado | Prueba que falló |
|---|---|
| Cambié `>` por `>=` en la validación de existencias | `test_salida_igual_a_las_existencias_deja_el_producto_en_0` |
| Quité la validación de número entero | `test_cantidad_decimal_se_rechaza` |
| Modifiqué el producto original en lugar de crear uno nuevo | `test_no_modifica_el_producto_original` |

En los tres casos pasaron las otras 9 pruebas, así que cada prueba cubre algo distinto. Con el código original, las 10 pasan.

## Reflexión final (5 a 8 líneas)

El asistente me ayudó más a armar primero la lista de casos, sobre todo los límites: salida igual a las existencias, existencias + 1 y cantidad decimal. Esta vez mis pruebas no atraparon ningún error en el código generado, porque las 10 pasaron a la primera. Para confiar en ellas hice tres cambios deliberados al código y cada uno lo detectó una prueba distinta. También me protegieron durante el refactor: separé errores y validaciones y las pruebas siguieron en verde sin tocarlas. En la próxima funcionalidad probaría la función con una base de datos real dentro de la transacción de mi ADR-001, y le pediría al asistente que intente romper mis pruebas con casos raros, como un producto sin `cantidad_actual`.

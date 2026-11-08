# Checklist Tecnico de Code Review Profesional

En esta seccion presento el instrumento formal de revision tecnica que elabore y aplique sobre el repositorio del Sistema de Gestion de Solicitudes Academicas, contrastando la version inicial con la version refactorizada.

## 1. Informacion general de la revision

- Sistema evaluado: Sistema de Gestion de Solicitudes Academicas
- Autor de la revision: Desarrollador responsable de la revision tecnica (primera persona)
- Objeto de revision: Transicion desde `version_inicial/main.py` hacia el paquete modular `version_refactorizada/`
- Estado de la evaluacion: Aprobado con refactorings implementados

## 2. Matriz de evaluacion por categorias

| Categoria | Criterio de evaluacion | Estado en version inicial | Estado en version refactorizada | Observacion tecnica |
| :--- | :--- | :---: | :---: | :--- |
| **Arquitectura y modularidad** | Separacion de responsabilidades en capas claras (presentacion, dominio, datos) | NO CUMPLE | CUMPLE | Se paso de un script unico a tres capas: `modelos.py`, `repositorio.py`, `servicios.py` y `main.py`. |
| **Principios SOLID** | SRP: Cada clase o modulo posee un unico motivo de cambio | NO CUMPLE | CUMPLE | Inicialmente `main.py` hacia persistencia, I/O y calculos. Ahora cada clase tiene una unica responsabilidad. |
| **Principios SOLID** | DIP: Dependencia de abstracciones o inyeccion de dependencias | NO CUMPLE | CUMPLE | `ServicioSolicitudes` recibe su repositorio por inyeccion en su constructor, facilitando sustitucion y pruebas. |
| **Clean Code: Nombres** | Nombres descriptivos y representativos del dominio | REGULAR | CUMPLE | Se renombraron variables confusas y se crearon clases explicitas (`Estudiante`, `Responsable`, `Solicitud`). |
| **Clean Code: Funciones** | Funciones breves que realizan una unica tarea logica | NO CUMPLE | CUMPLE | Se descompusieron metodos extensos como `registrar_solicitud` y `asignar_responsable` en funciones concisas. |
| **Clean Code: Estado** | Ausencia de variables globales mutables | NO CUMPLE | CUMPLE | Se eliminaron por completo las variables globales `estudiantes`, `responsables`, `solicitudes` y la palabra `global`. |
| **Validacion y excepciones** | Validacion de precondiciones y manejo estructurado de errores | NO CUMPLE | CUMPLE | Se incorporo validacion de cadenas vacias, tipos y estados permitidos, con captura centralizada de `ValueError`. |
| **Persistencia** | Desacoplamiento de detalles de almacenamiento | NO CUMPLE | CUMPLE | Se encapsulo la lectura y escritura JSON en la clase `RepositorioSolicitudes`, protegiendo la logica ante fallos de disco. |
| **Generacion de IDs** | Algoritmo robusto que evita duplicaciones al eliminar o filtrar | NO CUMPLE | CUMPLE | Se reemplazo el peligroso `len() + 1` por `max(id) + 1` en el metodo auxiliar `_siguiente_id`. |
| **Comportamiento externo** | Preservacion de la funcionalidad visible para el usuario | CUMPLE | CUMPLE | Las 7 opciones del menu conservan exactamente su salida y flujo interactivo original. |

## 3. Observaciones tecnicas detalladas

Durante mi revision sobre el codigo inicial registre los siguientes hallazgos criticos:

1. **Alto acoplamiento con la consola**: Las funciones originales contenian llamadas directas a `input()` y `print()` entrelazadas con la transformacion de datos y el acceso a disco. Esto impedia cualquier tipo de automatizacion o prueba unitaria.
2. **Fragilidad de tipos con diccionarios planos**: Las entidades existian como diccionarios dinamicos sin garantia de estructura. Un error tipografico en cualquier clave causaba comportamientos anomalos o excepciones `KeyError` no controladas.
3. **Peligro latente de colision de identificadores**: El calculo de identificadores mediante `len(coleccion) + 1` generaba un riesgo severo de corrupcion relacional si se borraban registros intermedios.
4. **Vulnerabilidad a bloqueos por entrada de datos**: Las conversiones directas `int(input())` provocaban la finalizacion inmediata del programa si el usuario ingresaba un caracter no numerico.

## 4. Feedback profesional y acciones correctivas aplicadas

Como parte de mi revision tecnica, estableci las siguientes directivas de mejora que fueron implementadas satisfactoriamente:

- **Accion 1**: Extraer las estructuras de datos hacia clases de dominio en `modelos.py`, proveyendo metodos `to_dict()` para serializacion uniforme.
- **Accion 2**: Aislar el acceso a disco dentro de `repositorio.py`, agregando control de excepciones para `json.JSONDecodeError` y `OSError`, garantizando que la aplicacion inicie de forma segura aun con archivos inexistentes o dañados.
- **Accion 3**: Trasladar las reglas de validacion y busqueda hacia `servicios.py`, asegurando que `ServicioSolicitudes` controle la consistencia de los datos antes de persistirlos.
- **Accion 4**: Implementar un bloque general de captura de excepciones en el bucle principal de `main.py`, permitiendo que cualquier error de validacion (`ValueError`) sea informado al usuario amigablemente sin interrumpir la ejecucion del sistema.

## 5. Criterios de aceptacion tecnica (Definition of Done)

Para considerar aprobado el codigo y dar por concluida la etapa de refactorizacion, verifique el cumplimiento estricto de los siguientes criterios:

1. El codigo no contiene variables globales mutables ni referencias a la directiva `global`.
2. Toda la persistencia en formato JSON esta aislada en la capa de repositorio.
3. Las operaciones de entrada y salida por consola residen exclusivamente en la capa de aplicacion / presentacion.
4. Toda regla de negocio y transicion de estados se valida en la capa de servicios.
5. Se ejecutan con exito todas las pruebas de regresion manuales sobre las 7 opciones del menu sin alteracion del resultado visible.
6. El codigo respeta los estandares de estilo PEP 8 y buenas practicas de legibilidad de Clean Code.

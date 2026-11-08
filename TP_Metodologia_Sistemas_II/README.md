# Sistema de Gestion de Solicitudes Academicas

Trabajo Practico Integrador para la asignatura Metodologia de Sistemas II.

En este proyecto presento el analisis, diagnostico y evolucion profesional de un sistema de gestion de solicitudes academicas. El trabajo evidencia la distincion entre calidad externa e interna, la deteccion de deuda tecnica y code smells, la aplicacion de principios SOLID y Clean Code, la ejecucion de refactorings seguros y la realizacion de un code review profesional con criterios tecnicos de aceptacion.

## Estructura del repositorio

El repositorio se encuentra organizado en las siguientes carpetas y archivos:

- `version_inicial/`: Contiene la implementacion base del sistema (`main.py`), caracterizada por un diseño monolitico, variables globales y deuda tecnica identificada.
- `version_refactorizada/`: Contiene la version mejorada con arquitectura modular por capas:
  - `modelos.py`: Clases de dominio (`Estudiante`, `Responsable`, `Solicitud`).
  - `repositorio.py`: Capa de persistencia desacoplada para lectura y escritura en formato JSON.
  - `servicios.py`: Capa de logica de negocio, validaciones y reglas de dominio.
  - `main.py`: Capa de presentacion e interfaz de usuario por linea de comandos (CLI).
- `datos/`: Almacena el archivo de datos persistente `solicitudes.json`.
- `docs/`: Documentacion complementaria, checklist tecnico de revision de codigo y evidencias.

## Tecnologias utilizadas

- Lenguaje: Python 3
- Formato de almacenamiento: JSON
- Interfaz: Linea de comandos (CLI)
- Control de versiones: Git y GitHub

## Funcionalidades principales

1. Registrar estudiante con nombre y legajo.
2. Registrar responsable administrativo con nombre y area.
3. Registrar solicitud academica vinculada a un estudiante registrado, con tipo, prioridad y descripcion.
4. Cambiar el estado de una solicitud (Pendiente, En proceso, Resuelta).
5. Asignar un responsable del personal administrativo a una solicitud.
6. Buscar y filtrar solicitudes por estado o tipo.
7. Generar reporte consolidado con totales y detalle de solicitudes.

## Instrucciones de ejecucion

Para ejecutar la version inicial (sistema base):
```bash
python3 version_inicial/main.py
```

Para ejecutar la version refactorizada (sistema mejorado):
```bash
python3 version_refactorizada/main.py
```

## Video de defensa y demostracion

El video grupal explicativo se encuentra disponible en el siguiente enlace:
- [Video de Presentacion en Google Drive](https://drive.google.com/file/d/1qNMXisz7EI8inIM2FHM5edfrk_7orGlC/view?usp=drive_link)

## Tags de Git para la entrega academica

- Tags de estado general: `estado-inicial` y `estadorefactorizado`.
- Tags de etapas especificas: `etapa-diagnostico`, `etapa-refactoring`, `etapa-pruebas` y `etapa-docs`.
# Diagrama de Arquitectura y Clases del Sistema
## Metodologia de Sistemas II - Trabajo Practico Integrador

En este documento presentamos los diagramas tecnicos que evidencian la evolucion profesional del sistema, mostrando primero la transformacion estructural antes y despues del refactoring, y luego el detalle de la arquitectura por capas resultante.

---

### 1. Comparacion Estructural: Antes vs Despues

Muestra la transicion general desde el script monolitico inicial con deuda tecnica hacia la estructura modular desacoplada:

```mermaid
flowchart LR
    subgraph Inicial ["Antes: Version Inicial (Deuda Tecnica)"]
        Mono["main.py (Script Monolitico 214 lineas)<br/>- Variables globales mutables<br/>- Diccionarios sin clases<br/>- Consola y persistencia entrelazadas<br/>- Entradas fragiles sin try/except"]
    end

    subgraph Refactorizada ["Despues: Version Refactorizada (Clean Code y SOLID)"]
        direction TB
        M1["modelos.py (Clases de dominio)"]
        M2["servicios.py (Logica pura de negocio)"]
        M3["repositorio.py (Persistencia JSON)"]
        M4["main.py (Interfaz por consola)"]
    end

    Inicial ==>|Refactorings Seguros| Refactorizada
```

---

### 2. Diagrama de Arquitectura por Capas (Version Refactorizada)

Detalla la interaccion interna, la distribucion de responsabilidades y la inyeccion de dependencias en el sistema mejorado:

```mermaid
graph TD
    subgraph Capa_Presentacion ["Capa de Presentacion (Interfaz CLI)"]
        UI["Aplicacion (main.py)<br/>- mostrar_menu()<br/>- Captura de ValueError<br/>- Interaccion con el usuario"]
    end

    subgraph Capa_Servicios ["Capa de Logica de Negocio"]
        Service["ServicioSolicitudes (servicios.py)<br/>- registrar_estudiante()<br/>- registrar_responsable()<br/>- registrar_solicitud()<br/>- cambiar_estado()<br/>- asignar_responsable()<br/>- buscar_solicitudes()<br/>- generar_reporte()<br/>- _siguiente_id() / _buscar_por_id()"]
    end

    subgraph Capa_Dominio ["Capa de Dominio (Modelos)"]
        M1["Estudiante (modelos.py)<br/>id, nombre, legajo"]
        M2["Responsable (modelos.py)<br/>id, nombre, area"]
        M3["Solicitud (modelos.py)<br/>id, tipo, prioridad, estado"]
    end

    subgraph Capa_Persistencia ["Capa de Persistencia y Datos"]
        Repo["RepositorioSolicitudes (repositorio.py)<br/>- cargar()<br/>- guardar()<br/>- Control OSError y JSONDecodeError"]
        Data[("solicitudes.json")]
    end

    UI -->|invoca metodos| Service
    Service -->|utiliza modelos| M1
    Service -->|utiliza modelos| M2
    Service -->|utiliza modelos| M3
    Service -->|inyeccion de dependencias| Repo
    Repo -->|lectura y escritura| Data
```

---

### 3. Explicacion de las Decisiones de Diseño

1. **Principio de Responsabilidad Unica (SRP):** Cada clase tiene una sola razon para cambiar. Si cambia el almacenamiento, solo se modifica `repositorio.py`. Si cambia la interfaz de consola, solo se modifica `main.py`. Si cambian las reglas de aprobacion o estados, solo se modifica `servicios.py`.
2. **Principio de Inversion de Dependencias (DIP):** `ServicioSolicitudes` recibe su repositorio mediante su constructor `__init__`, evitando acoplamiento rigido con archivos fisicos de disco.
3. **Manejo Estructurado de Excepciones:** La logica de negocio lanza excepciones semanticas (`ValueError`) y la capa de interfaz las atrapa amigablemente sin reiniciar ni colapsar el programa.

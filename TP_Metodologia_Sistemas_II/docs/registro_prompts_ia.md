# Registro de Prompts e Interaccion con Inteligencia Artificial
## Metodologia de Sistemas II - Trabajo Practico Integrador

Presentamos el registro de las consultas realizadas a herramientas de inteligencia artificial.

Asumimos la autoria, el analisis del codigo base, la implementacion de las refactorizaciones y la toma de decisiones tecnicas. La inteligencia artificial se utilizo como soporte metodologico de revision, contraste bibliografico y asistencia de redaccion tecnica.

---

### 1. Declaracion de Autoria y Grado de Intervencion

- **Autoria del trabajo:** El diagnostico de problemas, la construccion de la version refactorizada, el diseño de clases y la verificacion funcional fueron realizadas por los integrantes del equipo.
- **Rol de la inteligencia artificial:** Consultor tecnico para validar la nomenclatura teorica de los code smells detectados por el equipo, contrastar decisiones de diseño arquitectonico, perfeccionar criterios de aceptacion y sintetizar la exposicion oral.
- **Grado de intervencion:** Asistencia metodologica y editorial.

---

### 2. Registro de Prompts de Direccion y Mejora Tecnica

#### Consulta 1: Validacion teorica de los code smells identificados por el equipo
- **Contexto del equipo:** Junto a mi compañera analizamos el archivo version_inicial/main.py y marcamos como debilidades tecnicas las variables globales mutables, el uso de diccionarios en vez de clases y la generacion de IDs con len() + 1.
- **Prompt realizado por el integrante:**
  > "Junto a mi compañera analizamos nuestro sistema base en version_inicial/main.py y encontramos variables globales en las lineas 9 a 16, entidades representadas como diccionarios planos en las lineas 87 a 95 y generacion insegura de IDs con len() + 1 en las lineas 44, 61 y 88. Queremos validar si nuestra justificacion tecnica de impacto y riesgo de mantenimiento coincide con la taxonomia academica de code smells, y como redactar formalmente estas debilidades para el informe."
- **Resultado y decision del equipo:**
  El asistente valido la clasificacion de Global Mutable State, Primitive Obsession y Fragile ID Generation. El equipo adopto la formulacion metodologica formal para documentar el impacto en la mantenibilidad.

#### Consulta 2: Revision critica de la arquitectura por capas diseñada por el equipo
- **Contexto del equipo:** Diseñamos una division en modulos: modelos.py con las entidades, repositorio.py para persistencia, servicios.py para logica y main.py para consola, inyectando el repositorio en el constructor del servicio.
- **Prompt realizado por el integrante:**
  > "Diseñamos una refactorizacion modular para nuestro proyecto separando la persistencia en RepositorioSolicitudes, el dominio en clases Estudiante, Responsable y Solicitud, y la logica de negocio en ServicioSolicitudes mediante inyeccion de dependencias. Revisa nuestra propuesta arquitectonica y decinos si se adecua correctamente a los principios SRP y DIP de SOLID, o si observas algun acoplamiento residual que debamos corregir."
- **Resultado y decision del equipo:**
  El asistente confirmo que el diseño respeta SRP y DIP. Sugirio aislar el control de excepciones (OSError y JSONDecodeError) en el repositorio y normalizar cadenas de entrada, mejoras que incorporamos en la version final.

#### Consulta 3: Formalizacion de criterios de aceptacion para el checklist de code review
- **Contexto del equipo:** Elaboramos un borrador con items de evaluacion de legibilidad, arquitectura y pruebas de no regresion para aplicar sobre nuestro repositorio.
- **Prompt realizado por el integrante:**
  > "Armamos un borrador de checklist tecnico para evaluar nuestro codigo refactorizado frente al original. Ayudanos a pulir la redaccion tecnica de los criterios de aceptacion de Definition of Done para que sean objetivos, verificables y profesionales conforme a las normas de revision de codigo de la asignatura."
- **Resultado y decision del equipo:**
  El equipo incorporo las pautas sugeridas en la matriz definitiva de checklist_code_review.md, asegurando que cada criterio cuente con estado verificable y evidencia tecnica.

#### Consulta 4: Estructuracion y control de tiempos para la exposicion en video
- **Contexto del equipo:** Teniamos definidos los puntos a defender en el video, pero necesitabamos organizar el tiempo de mi exposicion individual para no superar los seis minutos maximos y coordinar lo que se muestra en pantalla con lo que se explica.
- **Prompt realizado por el integrante:**
  > "Tengo definidos mis puntos de exposicion sobre el sistema base, los code smells detectados, las refactorizaciones y el code review. Ayudame a estructurar un guion conciso que me permita explicar claramente los archivos y las lineas de codigo que modifique, manteniendo un tiempo aproximado de cuatro minutos sin exceder el tope de seis minutos de la catedra."
- **Resultado y decision del equipo:**
  El asistente ayudo a ordenar la secuencia cronometrada en cuatro bloques tematicos con las lineas exactas a señalar en pantalla, permitiendo grabar la defensa oral con ritmo fluido.

---

### 3. Conclusion y Evaluacion Critica del Equipo

Todas las respuestas y sugerencias brindadas por la herramienta fueron analizadas por nosotros. Se descartaron respuestas genericas y se adaptaron las recomendaciones a las caracteristicas particulares de nuestro codigo, preservando en todo momento la autoria intelectual, el aprendizaje practico y el criterio exigido por la asignatura.

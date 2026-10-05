# Affinity42

Affinity42 es un proyecto para identificar estudiantes de 42 con perfiles y ritmos de trabajo compatibles, calculando y visualizando un **Índice de Afinidad** basado en proyectos completados y su cercanía temporal.

## 1) Equipo y logins de 42

> Completar los logins exactos en Intra donde corresponda.

| Miembro | Login 42 | Responsabilidad principal |
|---|---|---|
| Dobrin | `TODO_LOGIN_DOBRIN` | Frontend (Streamlit) |
| Lucas | `TODO_LOGIN_LUCAS` | Presentación (PowerPoint) y apoyo Frontend |
| Flor | `TODO_LOGIN_FLOR` | Backend / Datos |
| Durian | `TODO_LOGIN_DURIAN` | Backend / Datos |

## 2) Dolor atacado y solución propuesta

### Dolor
En proyectos grupales, encontrar compañeros con conocimientos recientes y experiencia similar suele depender de afinidad personal o información incompleta.

### Solución
Affinity42 calcula un **Índice de Afinidad** entre pares de estudiantes para sugerir colaboraciones futuras más compatibles, usando:
- Proyectos en común completados.
- Proyectos únicos entre ambos perfiles.
- Proximidad en fechas de finalización (con bonus temporal).

## 3) Metodología de ideación y prototipado

1. **Definición del problema**: detectar compatibilidad académica y de ritmo de entrega.  
2. **Selección de señal principal**: similitud de historial mediante índice de Jaccard.  
3. **Ajuste temporal**: incorporar “bonus time” para conocimiento fresco.  
4. **Diseño de prototipo**: visualización de afinidad por estudiante y matriz global.  
5. **Iteración**: validar filtros, calidad de datos y actualización vía API.

## 4) Cálculo del Índice de Afinidad

### 4.1 Índice de Jaccard

Sea A el conjunto de proyectos completados por un estudiante y B el conjunto del otro:

\[
Jaccard(A, B)=\frac{|A \cap B|}{|A \cup B|}
\]

Referencia: https://la.mathworks.com/help/images/ref/jaccard.html

### 4.2 Bonus temporal

Si un proyecto compartido fue terminado con una diferencia de **30 días o menos** entre ambos estudiantes, se suma:

- `+0.05` por proyecto compartido que cumpla la condición temporal.

### 4.3 Fórmula final

\[
Indice\_Afinidad=\min\left(1,\;Jaccard + Bonus\_Time\right)\times 100
\]

- Resultado expresado en porcentaje.
- Tope máximo: **100%**.

## 5) Datos, filtros y alcance

Para asegurar comparaciones homogéneas:

- Filtrar por **grade = cadet** (estudiantes, no piscineros).
- Campus Madrid: **código 22**.
- Considerar solo proyectos del cursus (excluir Piscina): **código 21**.
- Usar fechas de inscripción y finalización para enriquecer análisis temporal.

## 6) Arquitectura y responsabilidades

- **Frontend (Streamlit)**: interfaz para selección de estudiante, visualización de índice y matriz de afinidad.
- **Backend / Datos**: ingesta desde API de 42, normalización, cálculo de afinidades y generación de matriz.
- **Presentación**: narrativa del problema, demo, resultados y próximos pasos.

### Gestión del proyecto

- Reuniones cortas de seguimiento.
- División por entregables (datos, visualización, storytelling).
- Validación cruzada de resultados antes de integrar.

## 7) Memoria de trabajo (registro de horas)

> Sustituir con horas reales al cierre de cada jornada.

| Miembro | Fecha | Tarea | Horas |
|---|---|---|---:|
| Dobrin | 2026-10-03 | Estructura base Streamlit | 0.0 |
| Lucas | 2026-10-03 | Guion presentación | 0.0 |
| Flor | 2026-10-03 | Diseño de modelo de datos | 0.0 |
| Durian | 2026-10-03 | Investigación API 42 | 0.0 |

## 8) Guía de funcionamiento (setup)

> Ajustar según evolucione el código final.

### Prerrequisitos
- Python 3.10+
- `pip`
- Credenciales API de 42 (OAuth2)

### Instalación
1. Clonar repositorio.
2. Crear entorno virtual:
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Linux/macOS)
3. Instalar dependencias:
   - `pip install -r requirements.txt` *(si existe el archivo)*.

### Configuración
Definir variables de entorno (ejemplo):
- `CLIENT_ID`
- `CLIENT_SECRET`
- `REDIRECT_URI`

Consultar:
- https://api.intra.42.fr/apidoc/guides/getting_started
- https://api.intra.42.fr/apidoc/guides/web_application_flow

### Ejecución (frontend)
- `streamlit run app.py` *(ruta/nombre sujeto a implementación final)*.

## 9) Visualización propuesta

- **Tarjeta de afinidad** estudiante A vs B (porcentaje final).
- **Matriz de afinidad** entre estudiantes del cluster.
- **Heatmap** para detectar parejas/equipos potenciales.
- Filtros por campus, grade, cohorte y proyectos.

## 10) Actualización de datos con la API

Pendientes a medir en implementación:
- Número de requests para población objetivo.
- Tiempo total de refresco de matriz.
- Estrategia de cache y frecuencia de actualización.
- Manejo de rate limits y reintentos.

## 11) Problemas técnicos encontrados y soluciones aplicadas

| Problema | Impacto | Solución aplicada |
|---|---|---|
| Definición ambigua de compatibilidad | Dificultad para medir afinidad de forma objetiva | Se eligió Jaccard como base cuantitativa y se añadió bonus temporal |
| Riesgo de mezclar perfiles no comparables | Resultados poco representativos | Se definieron filtros: grade cadet, campus 22, exclusión de Piscina |
| Dependencia de actualización de API | Datos potencialmente desfasados | Se planificó matriz recalculable y estrategia de monitoreo de tiempos/requests |

## 12) Enlaces útiles

- Términos legales 42: https://profile.intra.42.fr/legal/terms/33  
- API 42 (Getting Started): https://api.intra.42.fr/apidoc/guides/getting_started  
- API 42 (Web Application Flow): https://api.intra.42.fr/apidoc/guides/web_application_flow  
- Presentación: https://docs.google.com/presentation/d/1z9DEqyjXUZOSI4vm4TkRrIBXEgf8_3f_BW0hcJiKJ7s/edit?usp=sharing
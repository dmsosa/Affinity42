This project has been created as part of the Hackathon 42442 by _durisosa_, _dflor_, _louliveira_, _dobrin_

# Affinity42

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![42 Madrid](https://img.shields.io/badge/42-Madrid-000000?logo=42&logoColor=white)](https://www.42madrid.com/)
[![Status](https://img.shields.io/badge/status-MVP%20documentation-blue)](https://github.com/dmsosa/Affinity42)

Herramienta para identificar estudiantes de 42 con perfiles y ritmos de trabajo compatibles para futuros proyectos en grupo.

## 1) Dolor detectado

En 42, formar equipos efectivos suele depender de contactos previos o intuición. Esto dificulta encontrar compañer@s con:

- experiencia técnica parecida,
- conocimientos recientes sobre proyectos similares,
- ritmo de entrega compatible.

## 2) Solución propuesta

Affinity42 calcula y visualiza un **Índice de Afinidad** entre estudiantes usando:

1. proyectos completados en común (similitud de experiencia),
2. cercanía temporal en finalización de proyectos (frescura de conocimientos).

El resultado se muestra como porcentaje para facilitar comparaciones y priorizar posibles parejas/equipos.

## 3) Fórmula del Índice de Afinidad

### 3.1 Índice de Jaccard

Para dos estudiantes `A` y `B`:

`jaccard(A,B) = |intersección de proyectos completados| / |unión de proyectos completados|`

### 3.2 Bonus temporal

Por cada proyecto en común terminado con diferencia de **<= 30 días**, se añade `+0.05`.

### 3.3 Índice final

`indice_final = (jaccard + bonus_time) * 100`

- El índice final se limita a un máximo de **100%**.
- Si no hay proyectos completados en ninguno de los dos perfiles, el índice se define como `0`.

## 4) Criterios de filtrado de datos

Para acotar la comparación a alumnado del cursus en Madrid:

- **Grade:** `cadet`
- **Campus:** código `22` (Madrid)
- **Cursus:** código `21` (excluye proyectos de Piscina)
- Solo estudiantes del cluster objetivo para el análisis de afinidad.

## 5) Representación gráfica recomendada (Frontend Streamlit)

- **Matriz de afinidad (heatmap):** filas/columnas = estudiantes, celdas = porcentaje de afinidad.
- **Top-N afinidades por estudiante:** barras ordenadas de mayor a menor.
- **Ficha comparativa par a par:** proyectos en común, bonus aplicado y score final.

## 6) Arquitectura de trabajo (prototipo)

- **Frontend:** Streamlit (visualización e interacción).
- **Backend/Data:** integración con API de 42 para recolectar datos, calcular índice y generar matriz.
- **Actualización:** ejecución periódica (batch) + refresco manual desde interfaz.

## 7) Estrategia de actualización con API 42

1. Obtener token OAuth según guías oficiales.
2. Consultar usuarios filtrados por campus/grade.
3. Extraer proyectos finalizados del cursus (id 21) y fechas de finalización.
4. Recalcular matriz de afinidad para el conjunto filtrado.
5. Persistir snapshot local para minimizar requests repetidos.

### Recomendaciones operativas

- Cachear respuestas con timestamp.
- Recalcular incrementalmente solo para usuarios con cambios recientes.
- Definir ventana de actualización (por ejemplo, cada 12-24h) según límites de rate.

## 8) Guía de funcionamiento

> Estado actual: documentación y definición funcional del MVP.

### 8.1 Requisitos

- Python 3.10+
- pip

### 8.2 Instalación

```bash
git clone https://github.com/dmsosa/Affinity42.git
cd Affinity42
python -m venv .venv
source .venv/bin/activate
pip install streamlit pandas numpy requests seaborn matplotlib
```

### 8.3 Ejecución (cuando exista `app.py`)

```bash
streamlit run app.py
```

## 9) Equipo, roles y gestión

> Completar/ajustar los logins exactos de intra42 si difieren de los identificadores usados abajo.

| Miembro | Login 42 | Responsabilidad principal |
|---|---|---|
| Dobrin | dobrin | Frontend (Streamlit) |
| Lucas | lucas | Presentación + apoyo frontend |
| Flor | flor | Backend/Data |
| Durian | durian | Backend/Data |

### Gestión del proyecto

- Planificación semanal de objetivos (cálculo, API, visualización, presentación).
- Seguimiento por bloques: datos, algoritmo, interfaz, comunicación.
- Revisión cruzada de resultados antes de demo.

### Registro de horas (memoria de trabajo)

| Miembro | Horas estimadas | Detalle |
|---|---:|---|
| Dobrin | 8h | Diseño UX Streamlit + prototipos de vistas |
| Lucas | 7h | Storytelling, PowerPoint, soporte de integración |
| Flor | 10h | Limpieza/normalización de datos API, filtros |
| Durian | 9h | Cálculo de afinidad, matriz y optimización |

## 10) Metodología (ideación y prototipado)

1. Definición del problema de emparejamiento.
2. Selección de métrica base (Jaccard).
3. Añadido de variable temporal para frescura de conocimiento.
4. Prototipo de visualizaciones para validar interpretabilidad.
5. Ajuste de filtros para evitar sesgos de datos (cadet/campus/cursus).

## 11) Problemas técnicos detectados y soluciones

1. **Datos heterogéneos de proyectos**  
   - *Problema:* proyectos fuera de cursus principal contaminan la similitud.  
   - *Solución:* filtrar por cursus `21`.

2. **Usuarios no comparables por contexto académico**  
   - *Problema:* mezclar perfiles no-cadet o de otros campus distorsiona el índice.  
   - *Solución:* filtrar por grade `cadet` y campus `22`.

3. **Coste de recálculo completo**  
   - *Problema:* matriz NxN crece rápidamente.  
   - *Solución:* cache + recalculo incremental por cambios recientes.

4. **Límites de consumo de API**  
   - *Problema:* muchas consultas consecutivas.  
   - *Solución:* agrupar solicitudes, persistir snapshots y espaciar refrescos.

## 12) Enlaces útiles

- Términos: https://profile.intra.42.fr/legal/terms/33
- API Getting Started: https://api.intra.42.fr/apidoc/guides/getting_started
- API Web Application Flow: https://api.intra.42.fr/apidoc/guides/web_application_flow
- Presentación: https://docs.google.com/presentation/d/1z9DEqyjXUZOSI4vm4TkRrIBXEgf8_3f_BW0hcJiKJ7s/edit?usp=sharing

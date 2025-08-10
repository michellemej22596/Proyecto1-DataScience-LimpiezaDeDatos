# Proyecto 1 – Obtención y Limpieza de Datos

## Descripción General

Este proyecto forma parte del curso **CC3084 – Data Science** de la Universidad del Valle de Guatemala y tiene como objetivo desarrollar habilidades en la **obtención, limpieza y documentación** de datos reales para que puedan ser utilizados en análisis posteriores.

El conjunto de datos corresponde a **establecimientos educativos de Guatemala** que imparten hasta el nivel **Diversificado**, recopilado desde el portal oficial del **Ministerio de Educación (MINEDUC)**.

---

## 🗂 Proceso del Proyecto

### 1. **Obtención de datos**

* Se descargaron los datos de los establecimientos para **cada departamento** desde:
  [http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO\_GE/](http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/)
* El portal genera archivos `.xls` que en realidad contienen tablas HTML, por lo que se desarrolló un script en Python para extraer correctamente la tabla con los registros.

### 2. **Unión de datos**

* Cada archivo por departamento se convirtió a `.csv`.
* Los `.csv` resultantes fueron unidos en un único archivo `establecimientos_unidos.csv`, asegurando que los encabezados fueran consistentes y eliminando filas innecesarias.

### 3. **Codebook**

* Se elaboró un **Libro de Códigos** (Codebook) con:

  * Definición de cada variable.
  * Tipo de dato.
  * Valores posibles y valores faltantes.
  * Fuente original.
  * Transformaciones aplicadas para limpieza.

### 4. **Limpieza de datos**

* En un **notebook**, se realizó la limpieza variable por variable:

  * **Establecimiento:** Mayúsculas, eliminación de comillas y caracteres especiales, corrección de errores tipográficos, detección de duplicados.
  * **Dirección:** Mayúsculas, estandarización de abreviaturas, eliminación de tildes y espacios extra.
  * **Teléfono:** Eliminación de caracteres no numéricos y validación de 8 dígitos.
  * **Municipio:** Unificación de nombres y eliminación de espacios extra.
  * **Supervisor / Director:** Mayúsculas, eliminación de tildes, corrección ortográfica.
  * **Departamental:** Comparación con “Departamento” y eliminación por redundancia.
* Se documentó cada transformación en una celda específica del notebook.

### 5. **Exportación final**

* El resultado del proceso se exportó como `establecimientos_limpios.csv`, listo para análisis posteriores.

---

## Estructura del repositorio

```
Proyecto1-DataScience-LimpiezaDeDatos
 ├── datos_xls/                # Archivos originales descargados del MINEDUC
 ├── datos_csv/                # Archivos CSV intermedios por departamento
 ├── scripts/                  # Scripts Python utilizados para conversión y unión
 ├── notebook_limpieza.ipynb   # Notebook con el proceso de limpieza paso a paso
 ├── codebook.pdf              # Libro de códigos de variables
 ├── establecimientos_unidos.csv  # Datos crudos unidos
 ├── establecimientos_limpios.csv # Datos finales limpios
 └── README.md                 # Descripción del proyecto
```

---

## Tecnologías utilizadas

* **Python 3**

  * `pandas`
  * `lxml` / `html5lib`
* **Jupyter Notebook**
* **Excel / LibreOffice** (validación visual)
* **Git** (control de versiones)

---

## Autores

* Michelle Mejía – Carnet 22596
* Silvia Illescas – Carnet 22376
* Emilio Reyes – Carnet 22674


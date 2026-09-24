# Escáner de Puertos TCP utilizando Python

## Universidad Estatal de Milagro - UNEMI

**Asignatura:** Seguridad Informática

**Práctica:** N.º 2

**Tema:** Desarrollo de un Escáner de Puertos de Red utilizando Python

**Carrera:** Tecnologías de la Información

**Modalidad:** En línea

---

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación básica en Python capaz de realizar un escaneo de puertos TCP sobre un equipo autorizado.

El programa permite ingresar una dirección IP, establecer un rango de puertos y realizar un análisis para identificar cuáles de ellos se encuentran abiertos.

Al finalizar el escaneo, la aplicación presenta un resumen con la dirección IP analizada, el rango de puertos utilizado, la cantidad de puertos analizados, los puertos abiertos encontrados y el tiempo empleado durante la ejecución.

---

## 2. Objetivo

Desarrollar una aplicación básica en Python que permita realizar un escaneo de puertos TCP de un equipo autorizado e identificar los puertos abiertos, promoviendo el uso responsable de herramientas digitales.

---

## 3. Tecnologías y herramientas utilizadas

El proyecto fue desarrollado utilizando:

* **Python**
* **Visual Studio Code**
* **GitHub**
* **Biblioteca `socket` de Python**
* **Biblioteca `ipaddress`**
* **Biblioteca `sys`**
* **Biblioteca `time`**

Las bibliotecas utilizadas pertenecen a la biblioteca estándar de Python, por lo que no se requiere instalar paquetes externos para ejecutar el programa.

---

## 4. Funcionalidades

El programa permite:

1. Ingresar una dirección IP.
2. Validar que la dirección IP tenga un formato válido.
3. Ingresar un puerto inicial.
4. Ingresar un puerto final.
5. Validar que los puertos estén dentro del rango permitido de 1 a 65535.
6. Validar que el puerto inicial no sea mayor que el puerto final.
7. Realizar un escaneo de puertos TCP.
8. Identificar los puertos que responden correctamente a la conexión.
9. Mostrar los puertos abiertos encontrados.
10. Mostrar un servicio aproximado asociado a determinados puertos.
11. Mostrar un resumen del escaneo.
12. Mostrar el tiempo de ejecución.
13. Cancelar el escaneo mediante `Ctrl + C`.

---

## 5. Estructura del proyecto

El repositorio está organizado de la siguiente manera:

```text
scanner-puertos-python/
│
├── scanner_puertos.py
├── README.md
└── MANUAL_USO.md
```

### `scanner_puertos.py`

Contiene el código fuente principal de la aplicación y todas las funciones necesarias para validar los datos, realizar el escaneo y mostrar los resultados.

### `README.md`

Contiene la descripción general del proyecto.

### `MANUAL_USO.md`

Contiene las instrucciones detalladas para utilizar la aplicación y comprender los resultados obtenidos.

---

## 6. Uso responsable

Este programa debe utilizarse únicamente sobre:

* Equipos propios.
* Máquinas virtuales propias.
* Laboratorios autorizados.
* Redes donde exista autorización para realizar el análisis.

No se debe utilizar para analizar equipos, servidores o redes de terceros sin autorización.

El propósito de esta aplicación es académico y está orientado al aprendizaje de conceptos básicos relacionados con el análisis de puertos TCP y la seguridad informática.


---

## 7. Manual de uso

Para consultar las instrucciones detalladas de instalación, ejecución e interpretación de resultados, revisar:

**[MANUAL_USO.md](MANUAL_USO.md)**

---

## 8. Repositorio

**Repositorio GitHub:**

> Enlace del repositorio creado por el grupo.


```text
[Repositorio del proyecto](https://github.com/sramirezd2-tech/scanner-puertos-python.git)
```

---

## 9. Integrantes

| N.º | Integrante                        |
| --: | --------------------------------- |
|   1 | Sthewart Bagner Ramirez Diaz      |
|   2 | Kerly Genesis Baño Pibaque        |
|   3 | Jessica Maribel Chillagana Chacho |
|   4 | Robinson Adonis Paredes Medrano   |
|   5 | Jonathan Andres Blacio Feijoo     |


---

## 10. Declaración de uso de Inteligencia Artificial

Para la elaboración del proyecto se puede utilizar Inteligencia Artificial como herramienta de apoyo, siempre que su utilización sea ética, responsable y complementaria al análisis realizado por los estudiantes.

La información obtenida mediante estas herramientas debe ser revisada y verificada antes de ser utilizada.

La declaración correspondiente también debe incluirse al final del documento entregable, de acuerdo con las indicaciones establecidas para la práctica.

---

## 11. Referencias

* Python Software Foundation. (2026). *socket — Low-level networking interface*. Documentación oficial de Python.
* Universidad Estatal de Milagro. (2026). *G002-S04-TICS-EN LÍNEA-SEGURIDAD INFORMÁTICA-C1: Práctica 2*. Guía de práctica.

---

## 12. Licencia y propósito

Este proyecto fue desarrollado con fines exclusivamente académicos para la asignatura **Seguridad Informática** de la Universidad Estatal de Milagro.

El código debe utilizarse de manera responsable y únicamente en entornos donde exista autorización para realizar pruebas de conectividad y análisis de puertos.

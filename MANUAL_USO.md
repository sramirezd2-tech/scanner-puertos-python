# MANUAL DE USO

## Escáner de Puertos TCP utilizando Python

### 1. Descripción

El presente manual explica el funcionamiento y uso del programa **Escáner de Puertos TCP**, desarrollado en Python como parte de la Práctica N.º 2 de la asignatura Seguridad Informática.

La aplicación permite ingresar una dirección IP y un rango de puertos para comprobar cuáles se encuentran abiertos mediante conexiones TCP. El programa también presenta un resumen con la cantidad de puertos analizados, los puertos abiertos encontrados y el tiempo de ejecución.

El programa utiliza la biblioteca `socket` de Python para realizar las conexiones TCP. La función `connect_ex()` permite obtener un indicador de error de la conexión, donde un resultado `0` indica que la conexión se realizó correctamente. [1]

> **Importante:** El programa debe utilizarse únicamente sobre equipos propios, máquinas virtuales, laboratorios autorizados o redes donde se tenga autorización para realizar el análisis.

---

# 2. Requisitos

Para ejecutar correctamente el programa se necesita:

* Computadora con Windows, Linux o macOS.
* Python instalado.
* Visual Studio Code u otro editor de código.
* Archivo `scanner_puertos.py`.
* Acceso a una terminal o consola.
* Una dirección IP perteneciente a un equipo autorizado para realizar la prueba.

El programa utiliza las siguientes bibliotecas de Python:

* `socket`
* `ipaddress`
* `sys`
* `time`

No es necesario instalar estas bibliotecas mediante `pip`, ya que forman parte de la biblioteca estándar de Python.

---

# 3. Instalación de Python

Si Python no está instalado en el equipo, se debe descargar e instalar desde su sitio oficial.

Durante la instalación en Windows se recomienda activar la opción:

**Add Python to PATH**

Una vez instalado, se puede comprobar la instalación desde una terminal.

Abrir **CMD**, PowerShell o la terminal de Visual Studio Code y ejecutar:

```bash
python --version
```

Si el comando anterior no funciona, en algunos sistemas se puede utilizar:

```bash
py --version
```

Debe aparecer la versión instalada de Python.

**Captura:**

<img width="300" height="147" alt="image" src="https://github.com/user-attachments/assets/8e6feda5-f55f-4a15-af9a-269d275f5c59" />



---

# 4. Preparación del programa

Crear una carpeta para el proyecto, por ejemplo:

```text
scanner-puertos-python
```

Dentro de esta carpeta debe encontrarse el archivo:

```text
scanner_puertos.py
```

La estructura básica del proyecto es:

```text
scanner-puertos-python/
│
├── scanner_puertos.py
├── README.md
└── MANUAL_USO.md
```

Abrir la carpeta utilizando **Visual Studio Code**.

---

# 5. Iniciar la aplicación

Abrir una terminal dentro de la carpeta del proyecto.

Ejecutar:

```bash
python scanner_puertos.py
```

En Windows también puede utilizarse:

```bash
py scanner_puertos.py
```

Al iniciar, el programa mostrará el título:

```text
=======================================================
               ESCÁNER DE PUERTOS TCP
=======================================================
        Práctica de Seguridad Informática
=======================================================
```

Posteriormente aparecerá un aviso de uso responsable.

---

# 6. Confirmación de autorización

Antes de iniciar el análisis, el programa solicita confirmar que se tiene autorización para realizar el escaneo.

Se mostrará:

```text
¿Confirma que tiene autorización para realizar el escaneo? (S/N):
```

Para continuar se debe ingresar:

```text
S
```

También se aceptan:

```text
s
si
sí
```

Si se responde con otra opción, el programa cancela la operación.

Esta medida busca evitar el uso del programa sobre equipos o redes sin autorización.

---

# 7. Ingresar la dirección IP

Después de confirmar la autorización, el programa solicita la dirección IP.

Se mostrará:

```text
-------------------------------------------------------
PASO 1 - DIRECCIÓN IP
-------------------------------------------------------
Ingrese la dirección IP que desea analizar:
```

Ingresar la dirección IP del equipo autorizado.

Por ejemplo:

```text
127.0.0.1
```

La aplicación comprueba que la dirección ingresada tenga un formato válido.

Si la dirección es correcta aparecerá:

```text
Dirección IP válida.
```

Si la dirección no es válida, el programa mostrará un mensaje de error y solicitará ingresarla nuevamente.

**Captura:**

<img width="424" height="130" alt="image" src="https://github.com/user-attachments/assets/f298cc45-1ede-49de-a076-5e87a34a0ecb" />


---

# 8. Ingresar el puerto inicial

A continuación, el programa solicita el primer puerto del rango que se desea analizar.

Se mostrará:

```text
-------------------------------------------------------
PASO 2 - PUERTO INICIAL
-------------------------------------------------------
Ingrese el puerto inicial:
```

Ingresar un número entre:

```text
1 y 65535
```

Por ejemplo:

```text
1
```

**Captura:**

<img width="425" height="97" alt="image" src="https://github.com/user-attachments/assets/8cb96ef7-2624-4891-beaf-0a18da8282af" />



---

# 9. Ingresar el puerto final

Después se solicita el último puerto del rango:

```text
-------------------------------------------------------
PASO 3 - PUERTO FINAL
-------------------------------------------------------
Ingrese el puerto final:
```

Por ejemplo:

```text
100
```

En este caso, el programa analizará los puertos desde el **1 hasta el 100**.

Si se introduce un valor fuera del rango permitido o un dato que no sea un número entero, el programa mostrará un mensaje de error y solicitará nuevamente el valor.

**Captura:**

<img width="410" height="90" alt="image" src="https://github.com/user-attachments/assets/40afb1c4-886b-49de-83d0-72276966a7c7" />



---

# 10. Validación del rango

El programa comprueba que el puerto inicial no sea mayor que el puerto final.

Por ejemplo, el siguiente rango es incorrecto:

```text
Puerto inicial: 100
Puerto final: 50
```

En este caso aparecerá:

```text
ERROR:
El puerto inicial no puede ser mayor que el puerto final.
```

El programa finalizará y será necesario ejecutarlo nuevamente con un rango correcto.

---

# 11. Ejecución del escaneo

Una vez ingresados correctamente los datos, comenzará el escaneo.

El programa mostrará información similar a:

```text
=======================================================
                INICIANDO ESCANEO
=======================================================
Dirección IP:        127.0.0.1
Puerto inicial:      1
Puerto final:        100
Puertos a analizar:  100
=======================================================

Escaneando puertos...
```

El programa comprueba cada puerto del rango utilizando una conexión TCP.

Cuando encuentra un puerto accesible, muestra:

```text
Puerto 80    - ABIERTO
```

El método `connect_ex()` utilizado por el programa devuelve `0` cuando la conexión se realiza correctamente. [1]

**Captura:**

<img width="408" height="196" alt="image" src="https://github.com/user-attachments/assets/33f96ba1-876b-40c3-a07a-25ff7ffea9f3" />



---

# 12. Resultados del escaneo

Cuando termina el análisis, el programa presenta un resumen.

Por ejemplo:

```text
=======================================================
               RESUMEN DEL ESCANEO
=======================================================
Dirección IP analizada: 127.0.0.1
Rango analizado:         1 - 100
Puertos analizados:      100
Puertos abiertos:        2
Tiempo de ejecución:     30.25 segundos
=======================================================
```

Si existen puertos abiertos, se muestran junto con una referencia del servicio asociado:

```text
PUERTOS ABIERTOS ENCONTRADOS:

Puerto 22    | Servicio aproximado: SSH
Puerto 80    | Servicio aproximado: HTTP
```

La identificación del servicio se basa en la tabla incluida dentro del programa. Por esta razón, se presenta como **servicio aproximado** y no como una identificación definitiva del servicio.

---

# 13. Interpretación de los resultados

Los resultados pueden interpretarse de la siguiente manera:

### Puerto abierto

Significa que el intento de conexión TCP al puerto obtuvo un resultado exitoso.

Ejemplo:

```text
Puerto 80 - ABIERTO
```

El programa registra este puerto en la lista de puertos abiertos.

### Puerto no reportado como abierto

Si un puerto no aparece en la lista de puertos abiertos, significa que el programa no obtuvo una conexión TCP exitosa dentro de las condiciones de la prueba.

Esto no debe interpretarse automáticamente como una vulnerabilidad o como una prueba completa de seguridad del equipo.

### Cantidad de puertos analizados

Indica cuántos puertos fueron incluidos en el rango.

Por ejemplo:

```text
Rango: 1 - 100
Puertos analizados: 100
```

### Puertos abiertos

Indica la cantidad de puertos que el programa identificó como abiertos.

### Tiempo de ejecución

Indica cuánto tiempo tardó el programa en completar el rango seleccionado.

---

# 14. Ejemplo de ejecución

Un ejemplo de prueba puede realizarse sobre un equipo o máquina virtual autorizada.

Datos ingresados:

```text
IP: 127.0.0.1
Puerto inicial: 1
Puerto final: 100
```

El programa podría presentar:

```text
=======================================================
                INICIANDO ESCANEO
=======================================================
Dirección IP:        127.0.0.1
Puerto inicial:      1
Puerto final:        100
Puertos a analizar:  100
=======================================================

Escaneando puertos...

Puerto 80    - ABIERTO

=======================================================
               RESUMEN DEL ESCANEO
=======================================================
Dirección IP analizada: 127.0.0.1
Rango analizado:         1 - 100
Puertos analizados:      100
Puertos abiertos:        1
Tiempo de ejecución:     XX.XX segundos
=======================================================

PUERTOS ABIERTOS ENCONTRADOS:

Puerto 80    | Servicio aproximado: HTTP

=======================================================
              ESCANEO FINALIZADO
=======================================================
```

**Nota:** Los resultados anteriores son únicamente un ejemplo.

<img width="468" height="502" alt="image" src="https://github.com/user-attachments/assets/d39055b3-db6d-4070-8737-5270e1379869" />


---

# 15. Cancelar el escaneo

Si durante el proceso se desea cancelar el programa, se puede utilizar:

```text
Ctrl + C
```

El programa detectará la interrupción y mostrará:

```text
=======================================================
El escaneo fue cancelado por el usuario.
=======================================================
```


---

# 16. Recomendaciones de uso

* Utilizar el programa únicamente en equipos autorizados.
* Realizar las pruebas preferentemente en un equipo propio o máquina virtual.
* No realizar escaneos sobre redes, servidores o dispositivos de terceros sin autorización.
* Mantener organizado el código dentro del repositorio de GitHub.


# ============================================================
# UNIVERSIDAD ESTATAL DE MILAGRO - UNEMI
# ASIGNATURA: SEGURIDAD INFORMÁTICA
# PRÁCTICA N.º 2
# TEMA: DESARROLLO DE UN ESCÁNER DE PUERTOS DE RED UTILIZANDO PYTHON
# ============================================================
#
# IMPORTANTE:
# Este programa debe utilizarse únicamente sobre equipos propios,
# máquinas virtuales o redes donde exista autorización.
# ============================================================

import socket
import ipaddress
import sys
import time


def mostrar_titulo():
    print("\n" + "=" * 55)
    print("               ESCÁNER DE PUERTOS TCP")
    print("=" * 55)
    print("        Práctica de Seguridad Informática")
    print("=" * 55 + "\n")


def solicitar_ip():
    while True:
        ip = input("Ingrese la dirección IP que desea analizar: ").strip()
        try:
            ipaddress.ip_address(ip)
            print("\nDirección IP válida.")
            return ip
        except ValueError:
            print("\nERROR:")
            print("La dirección IP ingresada no es válida.")
            print("Ejemplo de dirección válida: 127.0.0.1")
            print("Intente nuevamente.\n")


def solicitar_puerto(mensaje):
    while True:
        try:
            puerto = int(input(mensaje))
            if 1 <= puerto <= 65535:
                return puerto
            print("\nERROR: el número del puerto debe estar entre 1 y 65535.\n")
        except ValueError:
            print("\nERROR: debe ingresar solamente números enteros.\n")


def validar_rango(puerto_inicial, puerto_final):
    if puerto_inicial > puerto_final:
        print("\nERROR:")
        print("El puerto inicial no puede ser mayor que el puerto final.")
        return False
    return True


def obtener_servicio(puerto):
    servicios = {
        20: "FTP - Datos",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        67: "DHCP",
        68: "DHCP",
        80: "HTTP",
        110: "POP3",
        123: "NTP",
        143: "IMAP",
        161: "SNMP",
        443: "HTTPS",
        445: "SMB",
        587: "SMTP",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8000: "HTTP alternativo",
        8080: "HTTP alternativo",
    }
    return servicios.get(puerto, "Desconocido")


def escanear_puertos(ip, puerto_inicial, puerto_final):
    puertos_abiertos = []

    print("\n" + "=" * 55)
    print("                INICIANDO ESCANEO")
    print("=" * 55)
    print(f"Dirección IP:        {ip}")
    print(f"Puerto inicial:      {puerto_inicial}")
    print(f"Puerto final:        {puerto_final}")

    total_puertos = puerto_final - puerto_inicial + 1
    print(f"Puertos a analizar:  {total_puertos}")
    print("=" * 55)
    print("\nEscaneando puertos...\n")

    tiempo_inicio = time.time()

    for puerto in range(puerto_inicial, puerto_final + 1):
        try:
            socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cliente.settimeout(0.3)

            resultado = socket_cliente.connect_ex((ip, puerto))

            if resultado == 0:
                print(f"Puerto {puerto:<5} - ABIERTO")
                puertos_abiertos.append(puerto)

            socket_cliente.close()

        except KeyboardInterrupt:
            print("\n" + "=" * 55)
            print("El escaneo fue cancelado por el usuario.")
            print("=" * 55)
            sys.exit()

        except socket.error as error:
            print(f"Se produjo un error al analizar el puerto {puerto}: {error}")

    tiempo_total = time.time() - tiempo_inicio
    return puertos_abiertos, tiempo_total


def mostrar_resumen(ip, puerto_inicial, puerto_final, puertos_abiertos, tiempo_total):
    total_puertos = puerto_final - puerto_inicial + 1

    print("\n" + "=" * 55)
    print("               RESUMEN DEL ESCANEO")
    print("=" * 55)
    print(f"Dirección IP analizada: {ip}")
    print(f"Rango analizado:         {puerto_inicial} - {puerto_final}")
    print(f"Puertos analizados:      {total_puertos}")
    print(f"Puertos abiertos:        {len(puertos_abiertos)}")
    print(f"Tiempo de ejecución:     {tiempo_total:.2f} segundos")
    print("=" * 55)

    if puertos_abiertos:
        print("\nPUERTOS ABIERTOS ENCONTRADOS:\n")
        for puerto in puertos_abiertos:
            servicio = obtener_servicio(puerto)
            print(f"Puerto {puerto:<5} | Servicio aproximado: {servicio}")
    else:
        print("\nNo se encontraron puertos abiertos.")

    print("\n" + "=" * 55)
    print("              ESCANEO FINALIZADO")
    print("=" * 55)


def mostrar_advertencia():
    print("\n" + "-" * 55)
    print("AVISO DE USO RESPONSABLE")
    print("-" * 55)
    print("Este programa debe utilizarse únicamente en:")
    print("- Equipos propios.")
    print("- Máquinas virtuales propias.")
    print("- Laboratorios autorizados.")
    print("- Redes donde exista autorización.")
    print("-" * 55)

    respuesta = input(
        "\n¿Confirma que tiene autorización para realizar el escaneo? (S/N): "
    ).strip().lower()

    if respuesta not in ["s", "si", "sí"]:
        print("\nOperación cancelada.")
        print("Debe contar con autorización antes de realizar el escaneo.")
        sys.exit()


def main():
    mostrar_titulo()
    mostrar_advertencia()

    print("\n" + "-" * 55)
    print("PASO 1 - DIRECCIÓN IP")
    print("-" * 55)
    ip = solicitar_ip()

    print("\n" + "-" * 55)
    print("PASO 2 - PUERTO INICIAL")
    print("-" * 55)
    puerto_inicial = solicitar_puerto("Ingrese el puerto inicial: ")

    print("\n" + "-" * 55)
    print("PASO 3 - PUERTO FINAL")
    print("-" * 55)
    puerto_final = solicitar_puerto("Ingrese el puerto final: ")

    if not validar_rango(puerto_inicial, puerto_final):
        print(
            "\nEl programa finalizará. "
            "Ejecute nuevamente e ingrese un rango correcto."
        )
        return

    puertos_abiertos, tiempo_total = escanear_puertos(
        ip, puerto_inicial, puerto_final
    )

    mostrar_resumen(
        ip,
        puerto_inicial,
        puerto_final,
        puertos_abiertos,
        tiempo_total,
    )


if __name__ == "__main__":
    main()

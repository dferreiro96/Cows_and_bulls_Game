"""juego de Vacas y Toros (a ver si funciona jeje)"""

import random


print("""\nEste juego consiste en lo siguiente: el programa generará un número de 4 digítos aleatorio. Usted intentará 
adivinarlo. Si el número que usted diga contiene al menos 1 digíto del número aleatorio, sin importar la posición dentro del número, se le llamará 'vaca', pudiendo llegar a tener hasta 4 vacas.
 Si el número que ud introdujo tiene al menos un dígito en la  posición correcta, se le llamará: toro. Cuando alcance 4 toros, gana. No se permiten números repetidos\n""")

while True:
    aleat1 = random.sample("0123456789", 4)
    if aleat1[0] == ("0"):
        aleat1[0], aleat1[1] = aleat1[1], aleat1[0]
    aleat = int("".join(aleat1))

    contador = 0
    mil2 = aleat // 1000
    cent2 = (aleat // 100) % 10
    dec2 = (aleat // 10) % 10
    uni2 = aleat % 10
    while True:
        try:
            num = int(input("\nIntroduzca un número: "))
            if num < 1000 or num > 9999:
                print("\nRango inválido. Introduzca un número entre 1000 y 9999.")
                continue
            if len(set(str(num))) != 4:
                print("\nNo pueden haber números repetidos.")
                continue
        except ValueError:
            print("Solo se permiten números")
            continue
        break

    while num != aleat:
        contador += 1
        cont_vac = 0
        cont_t = 0

        mil = num // 1000
        cent = (num // 100) % 10
        dec = (num // 10) % 10
        uni = num % 10

        if mil == cent2:
            cont_vac += 1
        elif mil == dec2:
            cont_vac += 1
        elif mil == uni2:
            cont_vac += 1
        elif mil == mil2:
            cont_t += 1

        if cent == mil2:
            cont_vac += 1
        elif cent == dec2:
            cont_vac += 1
        elif cent == uni2:
            cont_vac += 1
        elif cent == cent2:
            cont_t += 1

        if dec == mil2:
            cont_vac += 1
        elif dec == cent2:
            cont_vac += 1
        elif dec == uni2:
            cont_vac += 1
        elif dec == dec2:
            cont_t += 1

        if uni == mil2:
            cont_vac += 1
        elif uni == cent2:
            cont_vac += 1
        elif uni == dec2:
            cont_vac += 1
        elif uni == uni2:
            cont_t += 1
        while True:
            try:
                num = int(
                    input(f"""El numero tiene {cont_vac} vaca(s) y {cont_t} toro(s)
\n Introduzca otro: """)
                )
            except ValueError:
                print("Solo se permiten números")
                continue
            break

    if num == aleat:
        contador += 1

        print(f"\nHa adivinado el número en {contador} intentos. FELICIDADES!!")

        salir = input("\nDesea salir del juego (s/n): ").lower().strip()

        while salir != ("s") and salir != ("n"):
            salir = (
                input("\nIntroduzca 's' para salir o 'n' para volver a jugar: ")
                .lower()
                .strip()
            )
            

        if salir != ("n"):
            print("Hasta luego")
            break

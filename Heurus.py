import time
from os import system

fh = open('Peliculas.txt')
soluciones = []
generos = []
directores = []
annos = []
flag = False

def loadingScreen():
    print ('[=          ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[==         ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[===        ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[====       ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[=====      ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[======     ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[=======    ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[========   ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[=========  ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[========== ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[===========]')
    time.sleep(0.1)
    _ = system('cls')

def shortLoadingScreen():
    print ('[=   ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[==  ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[=== ]')
    time.sleep(0.1)
    _ = system('cls')
    print ('[====]')

def gen():
    global flag
    correcto = ''
    for genero in generos:
        r = input('¿El genero de tu pelicula es ' + genero + '? ').lower()
        while (r != 'y' and r != 'n'):
            r = input('¿El genero de tu pelicula es ' + genero + '? (y/n) ').lower()
        if r == 'y':
            flag = True
            correcto = genero
            break
    return(correcto)

def dir():
    global flag
    correcto = ''
    for director in directores:
        r = input('¿El director de tu pelicula es ' + director + '? ').lower()
        while (r != 'y' and r != 'n'):
            r = input('¿El director de tu pelicula es ' + director + '? (y/n) ').lower()
        if r == 'y':
            flag = True
            correcto = director
            break
    return(correcto)

def ann():
    global flag
    correcto = ''
    for anno in annos:
        r = input('¿Tu pelicula es del año ' + anno + '? ').lower()
        while (r != 'y' and r != 'n'):
            r = input('¿Tu pelicula es del año ' + anno + '? (y/n) ').lower()
        if r == 'y':
            flag = True
            correcto = anno
            break
    return(correcto)

def heuristica():
    #_ = system('cls')
    print('No tengo informacion suficiente para adivinar tu pelicula')
    time.sleep(1)
    print(':c')
    time.sleep(1)
    print('Pero...')
    time.sleep(0.5)
    print('Si me das los datos de la pelicula que estabas pensado podré adivinarla la proxima vez')
    agen = input('¿Que genero es la pelicula  en la que estabas pensando?')
    adir = input('¿Quien dirige la pelicula en la que estabas pensando?')
    aann = input('¿En que año salió la pelicula en la que estabas pensando?')
    apel = input('Finalmente ¿En que pelicula pensabas?')
    with open('Peliculas.txt', 'a') as wf:
        wf.write("\n" + agen + ',' + adir + ',' + aann + ',' + apel)
    #_ = system('cls')
    exit()

def main():
    global flag

    _ = system('cls')
    print('Hola soy Heurus y tratare de adivinar la pelicula en la que estas pensando')
    time.sleep(4)
    print(':)')
    time.sleep(1)

    while True:
        start = input('Presiona S para empezar -> ')
        if start == "contraseña":
            loadingScreen()
            print('Base de datos:')
            print(soluciones)
        elif start == "s":
            loadingScreen()
            break
        else:
            print('Entrada Invalida')
            continue

    print('Empecemos')
    time.sleep(0.3)
    print('.')
    time.sleep(0.3)
    print('.')
    time.sleep(0.3)
    print('.')
    _ = system('cls')

    for line in fh:
        line = line.strip()
        soluciones.append(line.split(","))

    for solucion in soluciones:
        if solucion[0] not in generos:
            generos.append(solucion[0])

    shortLoadingScreen()
    genero_correcto = gen()
    if flag == False:
        heuristica()
    flag = False

    for solucion in soluciones:
        if solucion[0] == genero_correcto:
            if solucion[1] not in directores:
                directores.append(solucion[1])

    shortLoadingScreen()
    director_correcto = dir()
    if flag == False:
        heuristica()
    flag = False

    for solucion in soluciones:
        if solucion[0] == genero_correcto and solucion[1] == director_correcto:
            if solucion[2] not in annos:
                annos.append(solucion[2])

    shortLoadingScreen()
    anno_correcto = ann()
    if flag == False:
        heuristica()

    for solucion in soluciones:
        if solucion[0] == genero_correcto and solucion[1] == director_correcto and solucion[2] == anno_correcto:
            print(F"La pelicula en la que pensaste es {solucion[3]}")

if __name__ == '__main__':
    main()
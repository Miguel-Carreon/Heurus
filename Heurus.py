import time
from os import system

fh = open('Peliculas.txt')
soluciones = []
generos = []
directores = []
annos = []

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
    if soluciones[len(soluciones)-1][0] not in generos:
        generos.append(soluciones[len(soluciones)-1][0])
    
    if soluciones[len(soluciones)-1][1] not in directores:
        directores.append(soluciones[len(soluciones)-1][1])
    
    if soluciones[len(soluciones)-1][2] not in annos:
        annos.append(soluciones[len(soluciones)-1][2])

flag = False
for genero in generos:
    r = input('¿El genero de tu pelicula es ' + genero + '? ').lower()
    while (r != 'y' and r != 'n'):
        r = input('¿El genero de tu pelicula es ' + genero + '? (y/n) ').lower()
    if r == 'y':
        flag = True
        count = 0
        numeros = []
        for solucion in soluciones:
            if solucion[0] != genero:
                numeros.append(count)
            count += 1
        for numero in range (len(numeros)-1, -1, -1):
            try:
                directores.remove(soluciones[numeros[numero]][1])
            except:
                pass
            try:
                annos.remove(soluciones[numeros[numero]][2])
            except:
                pass
            soluciones.pop(numeros[numero])
        break
print(soluciones)

if flag == False:
    _ = system('cls')
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
    _ = system('cls')
    exit()

flag = False
for director in directores:
    r = input('¿El director de tu pelicula es ' + director + '? ').lower()
    while (r != 'y' and r != 'n'):
        r = input('¿El director de tu pelicula es ' + director + '? (y/n) ').lower()
    if r == 'y':
        flag = True
        count = 0
        numeros = []
        for solucion in soluciones:
            if solucion[1] != director:
                numeros.append(count)
            count += 1
        for numero in range (len(numeros)-1, -1, -1):
            try:
                annos.remove(soluciones[numeros[numero]][2])
            except:
                pass
            soluciones.pop(numeros[numero])
        break
print(flag)
print(soluciones)
print(annos)

if flag == False:
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

flag = False
for anno in annos:
    r = input('¿Tu pelicula es del año ' + anno + '? ').lower()
    while (r != 'y' and r != 'n'):
        r = input('¿Tu pelicula es del año ' + anno + '? (y/n) ').lower()
    if r == 'y':
        flag = True
        count = 0
        numeros = []
        for solucion in soluciones:
            if solucion[2] != anno:
                numeros.append(count)
            count += 1
        for numero in range (len(numeros)-1, -1, -1):
            soluciones.pop(numeros[numero])
        break
print(soluciones)

if flag == False:
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

#_ = system('cls')
#resp = soluciones[0][3].split(" ")
#print('Tu pelicula es:', resp[0].capitalize(), resp[1].capitalize())
print('La pelicula que pensaste es:',soluciones[0][3].capitalize())
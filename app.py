opcion = 0
name = input('Dime tu nombre: ')
print ('Hola ' + name + ', mucho gusto. ¿Necesitas hacer algún calculo?, tons toma la calculadora más malota de todo Occidente')


opcion = 0
n1 = int(input('Primer número: '))
n2 = int(input('Segundo número: '))
while True:
    print ("""
    ¿Qué quieres hacer?
    1) Sumar
    2) Restas
    3) Multiplicar
    4) Dividir
    5) Sorprendeme
    6) Salir de la calculadora
    """)
    option = int(input('Dime el tipo de operación que quieres hacer: '))
    
    if option == 1:
        print (' ')
        print ('Resultado:',n1 + n2)
    elif option == 2:
        print (' ')
        print ('Resultado:',n1 - n2)
    elif option == 3:
        print (' ')
        print ('Resultado:',n1 * n2)
    elif option == 4:
        print (' ')
        print ('Resultado:',n1 / n2)
    elif option == 5:
        print (' ')
        print ('https://matias.ma/nsfw/ copia y pega esto en el navegador')
    elif option == 6:
        print ('Regrese pronto')
        break
else:
    #quiero que esto varie dependiendo del genero del usuario, si es mujer que diga la opción 1, hombre da opción 2, rinoceronte da opción 3 y gato pollo da la opción 4
    #esto solo es porque si, no es obligatorio
    #este codigo no se esta ejecutando, para ejecutarlo solo eliminale los númerales ('#') y se ejecutara
    #if genero == 1
    #    print('¿Eres tonta o comes monte?, por favor elige algo valido')
    #if genero == 2
    #    print('¿Eres tonto o inhalas pega loka?, por favor elige algo valido')
    #if genero == 3
    #    print ('Bueno eres un rinoceronte, no puedo esperar gran cosa, ¿Que idioma hablan los rinocerontes?')
    #if genero == 4
    #    print ('No me puedo mover, se acostó en mi mano awwwwwwww')
    print ('tonto')
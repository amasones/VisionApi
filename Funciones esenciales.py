# Nota: hay funciones que pueden abarcar más variables, pero dado a que no son necesarias de momento es mejor omitirlas
# hasta futuro aviso, el codigo está optimizado en 50% ya que ciertas funciones como ver_datos funciona perfectamente
# pero tiene unos bugs que se arreglaron de una forma inortodoxa

def leer_web(url):
    # Permite leer todo los strings de una pagina para luego convertirla en su variable original, se necesita especificar la url
    from urllib.request import urlopen

    # Leer página.
    r = urlopen(url)
    # Leer el contenido.
    texto = str(r.read())

    # Convierte todos los valores a sus respectivos caracteres y limpia el texto
    texto = texto.replace("\\xc3\\xb3", 'ó')
    texto = texto.replace("\\\\u00f3", 'ó')
    texto = texto.replace("\\xc3\\xa9", 'é')
    texto = texto.replace("\\xc3\\xad", 'í')
    texto = texto.replace("\\\\u00ed", 'í')
    texto = texto.replace("\\xc3\\xb1", 'ñ')
    texto = texto.replace("\\\\u00f1", 'ñ')
    texto = texto.replace('b"', '')
    texto = texto.replace("b'", '')
    texto = texto.replace("\\n'", '')
    texto = texto.replace('\\n"', '')
    texto = texto.replace('\\n', '')

    # Evalua que el string sea correcto para su respectiva variable
    variable = eval(texto)

    r.close()
    return variable

def detalle_del_registro(variable):
    # Su funcion es agarrar los datos del diccionario y en este caso imprimirlos, pero se puede reutilizar para otras funciones
    for x in variable:
        # Agarra el dia y hora del registo
        fecha = x.get('fecha')
        dia = (fecha.get('dia'))
        mes = (fecha.get('mes'))
        ano = (fecha.get('año'))
        hora = (fecha.get('hora'))
        minutos = (fecha.get('minuto'))
        segundos = (fecha.get('segundo'))

        # Agarra los detalles del curso
        curso = x.get('curso')
        codigo = curso.get('codigo')
        curso_carrera = curso.get('Curso')
        grupo = curso.get('grupo')
        profesor = curso.get('profesor')
        semestre = curso.get('semestre')

        # Cuenta el numero de rostros
        rostros = x.get('rostros')

        # Mostrar todos los detalles
        print('\n', 'Fecha:', dia, '/', mes, '/', ano, '\n', 'Hora:', hora, ':', minutos, ':', segundos, '\n', '\n',
              'Información del curso:', '\n', 'Código:', codigo, '\n', 'Nombre del curso:', curso_carrera, '\n',
              'Profesor:', profesor, '\n', 'Grupo:', grupo, '\n', 'Semestre:', semestre, '\n',
              'Cantidad de rostros:', len(rostros), '\n',
              '-----------------------')
    return

def estadisticas_de_reconocimientos(variable):
    # Su funcion es imprimir estadisticas de datos de mayor a menor dependiendo de su porcentaje

    # Contador que luego se usara en el numero de rostros
    contador = 0

    # Determinar la cantidad de rostros
    for x in variable:
        rostros = x.get('rostros')
        cantidad_rostros = len(rostros)

    # Desempaca listas y diccionarios para agarrar el porcentaje de cada emocion.
    # Se puede modificar para admitir mas detalles pero para mantener el codigo lo mas limpio posible se omitira hasta
    # en un futuro uso.
    for y in range(cantidad_rostros):
        for x in variable:
            rostros = x.get('rostros')
            expresion_rostro = rostros[contador].get('face_expressions')
            joy = expresion_rostro.get('joy_likelihood')
            sorrow = expresion_rostro.get('sorrow_likelihood')
            anger = expresion_rostro.get('anger_likelihood')
            surprise = expresion_rostro.get('surprise_likelihood')
            under_exposed = expresion_rostro.get('under_exposed_likelihood')
            blurred = expresion_rostro.get('blurred_likelihood')
            headwear = expresion_rostro.get('headwear_likelihood')

            # Imprimir de mayor a menor las emociones y estados de las fotos
            contador += 1
            print('Rostro#', contador,'\n')


            if joy == 'VERY_LIKELY':
                print('Alegría: 100%')
            if sorrow == 'VERY_LIKELY':
                print( 'Tristeza: 100%')
            if anger == 'VERY_LIKELY':
                print( 'Enojo: 100%')
            if surprise == 'VERY_LIKELY':
                print( 'Sorpresa: 100%')
            if under_exposed == 'VERY_LIKELY':
                print( 'Sobre expuesto: 100%')
            if blurred == 'VERY_LIKELY':
                print( 'Borroso: 100%')
            if headwear == 'VERY_LIKELY':
                print( 'Gorro/Sombrero/Beanie: 100%')

            if joy == 'LIKELY':
                print( 'Alegría: 75%')
            if sorrow == 'LIKELY':
                print( 'Tristeza: 75%')
            if anger == 'LIKELY':
                print( 'Enojo: 75%')
            if surprise == 'LIKELY':
                print( 'Sorpresa: 75%')
            if under_exposed == 'LIKELY':
                print( 'Sobre expuesto: 75%')
            if blurred == 'LIKELY':
                print( 'Borroso: 75%')
            if headwear == 'LIKELY':
                print( 'Gorro/Sombrero/Beanie: 75%')

            if joy == 'POSSIBLE':
                print( 'Alegría:50%')
            if sorrow == 'POSSIBLE':
                print( 'Tristeza: 50%')
            if anger == 'POSSIBLE':
                print( 'Enojo: 50%')
            if surprise == 'POSSIBLE':
                print( 'Sorpresa: 50%')
            if under_exposed == 'POSSIBLE':
                print( 'Sobre expuesto: 50%')
            if blurred == 'POSSIBLE':
                print( 'Borroso: 50%')
            if headwear == 'POSSIBLE':
                print( 'Gorro/Sombrero/Beanie: 50%')

            if joy == 'UNLIKELY':
                print( 'Alegría:25%')
            if sorrow == 'UNLIKELY':
                print( 'Tristeza: 25%')
            if anger == 'UNLIKELY':
                print( 'Enojo: 25%')
            if surprise == 'UNLIKELY':
                print( 'Sorpresa: 25%')
            if under_exposed == 'UNLIKELY':
                print( 'Sobre expuesto: 25%')
            if blurred == 'UNLIKELY':
                print( 'Borroso: 25%')
            if headwear == 'UNLIKELY':
                print( 'Gorro/Sombrero/Beanie: 25%')

            if joy == 'VERY_UNLIKELY':
                print( 'Alegría:0%')
            if sorrow == 'VERY_UNLIKELY':
                print( 'Tristeza: 0%')
            if anger == 'VERY_UNLIKELY':
                print( 'Enojo: 0%')
            if surprise == 'VERY_UNLIKELY':
                print( 'Sorpresa: 0%')
            if under_exposed == 'VERY_UNLIKELY':
                print( 'Sobre expuesto: 0%')
            if blurred == 'VERY_UNLIKELY':
                print( 'Borroso: 0%')
            if headwear == 'VERY_UNLIKELY':
                print( 'Gorro/Sombrero/Beanie: 0%')

            print('-----------------------------------')
    return

def selector_id(numero):
    # Para esta funcion se ocupa especificar al usuario cual id(numero) quiere para que se pueda buscar en la base de datos
    from urllib.request import urlopen
    import datetime
    # Leer página.
    r = urlopen('http://leoviquez.synology.me/VisionAPI/cursos.py?id=' + str(numero))
    # Leer el contenido.
    texto = str(r.read())

    # Limpia el texto para ser evaluado.
    texto = texto.replace("b'", '')
    texto = texto.replace("\\n'", '')
    texto = texto.replace('\\n', '')

    # Evalua el texto como lista
    variable = eval(texto)

    # Determina si la lista es vacia para terminar el proceso
    if len(variable) ==0:
        print('No se encuentran registros para la Id',numero,'en este momento')
        return
    else:
        pass

    # Lista donde se almacenará la informacion con un formato diferente
    lista = []

    # Asigna cada valor a una variable(aunque no sea neceserio) para usar el import "datetime" para luego hacer un
    # sort a la lista para ordenarlo por fechas
    for x in variable:
        id_registro = (x[0])
        dia = (x[1])
        mes = (x[2])
        ano = (x[3])
        hora = (x[4])
        minuto = (x[5])
        segundos = (x[6])
        formato_fecha = datetime.date(int(ano), int(mes), int(dia))
        formato_hora = datetime.time(int(hora), int(minuto), int(segundos))
        lista.append([formato_fecha, formato_hora, id_registro])

    # Una opcion para que el usuari decida si quiere ver las fecha de una forma en especifico
    print('', 'Presione 1 para ordenar de lo más antiguo a más reciente', '\n',
          'Cualquier tecla para más reciente a más antiguo')
    decision =input('>>>')

    lista.sort()

    if decision == '1':
        pass
    else:
        lista.reverse()

    print('Los registros para el identificador del curso',numero,'son:','\n','------------------------')
    for x in lista:
        print('', 'Id del registo', x[2], '\n', 'Fecha:', x[0].strftime("%x"), '\n', 'Hora:',
              (x[1].strftime("%X")), '\n', '------------------------')

    r.close()
    return variable

def ver_datos(datos1):
    # Funcion simple que solo imprime datos dependiendo de su codigo, FALTA DE OPTIMIZAR
    # Una lista vacia donde se almacenara los codigos de los cursos
    cursos = []
    # Agregrar los cursos a la lista
    for x in datos1:
        cursos.append(x[1])
    # Elimina todos los cursos repetidos
    for x in cursos:
        for y in range(len(cursos) - 1):
            try:
                if x == cursos[y + 1]:
                    cursos.remove(x)
            except IndexError:
                pass
    # Imprimir los detalles por codigo de curso
    contador = -1
    for y in datos1:
        contador += 1
        for x in datos1:
            if x[1] == cursos[contador]:
                print('\n', 'Codigo del curso', x[1], '\n', 'Id del curso', x[0], '\n', 'Nombre del curso:', x[2], '\n',
                      'Grupo:', x[3], '\n', 'Profesor:', x[4], '\n', 'Semestre', x[5], '\n', 'Año', x[6], '\n',
                      '--------------------', )
                datos1.remove(x)
            # Un bug en la funcion es que no imprime el ultimo detalle.
            # SOLAMENTE SIRVE SI SE USA Y EN VEZ DE X, ademas tiene que ser un if, aunque el elif ahorraria memoria no
            # funciona en este caso.
            if len(datos1) == 1:
                print('\n', 'Codigo del curso', y[1], '\n', 'Id del curso', y[0], '\n', 'Nombre del curso:', y[2], '\n',
                      'Grupo:', y[3], '\n', 'Profesor:', y[4], '\n', 'Semestre', y[5], '\n', 'Año', y[6], '\n',
                      '--------------------', )


base_1 = leer_web('http://leoviquez.synology.me/VisionAPI/cursos.py')
base_3 = leer_web('http://leoviquez.synology.me/VisionAPI/index.py?id=17')

ver_datos(base_1)

selector_id(6)

detalle_del_registro(base_3)

estadisticas_de_reconocimientos(base_3)

def leer_web(url):
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
              'Profesor:', profesor, '\n', 'Grupo:', grupo, '\n', '\n', 'Cantidad de rostros:', len(rostros), '\n',
              '-----------------------')
    return


def estadisticas_de_reconocimientos(variable):
    # Contador que luego se usara en el numero de rostros
    contador = 0

    # Determinar la cantidad de rostros
    for x in variable:
        rostros = x.get('rostros')
        cantidad_rostros = len(rostros)

    # Desenpaca listas y diccionarios para agarrar el porcentaje de cada emocion.
    # Se puede modificar para admitir mas detalles pero para mantener el codigo lo mas limpio posible se omitira hasta
    # en un futuro uso.
    for x in variable:
        for y in range(cantidad_rostros):
            rostros = x.get('rostros')
            expresion_rostro = rostros[0].get('face_expressions')
            joy = expresion_rostro.get('joy_likelihood')
            sorrow = expresion_rostro.get('sorrow_likelihood')
            anger = expresion_rostro.get('anger_likelihood')
            surprise = expresion_rostro.get('surprise_likelihood')
            under_exposed = expresion_rostro.get('under_exposed_likelihood')
            blurred = expresion_rostro.get('blurred_likelihood')
            headwear = expresion_rostro.get('headwear_likelihood')

            # Imprimir de mayor a menor las emociones y estados de las fotos
            contador += 1
            print('Rostro#', contador)

            if joy == 'VERY_LIKELY':
                print('\n', 'Alegría: 100%')
            if sorrow == 'VERY_LIKELY':
                print('\n', 'Tristeza: 100%')
            if anger == 'VERY_LIKELY':
                print('\n', 'Enojo: 100%')
            if surprise == 'VERY_LIKELY':
                print('\n', 'Sorpresa: 100%')
            if under_exposed == 'VERY_LIKELY':
                print('\n', 'Sobre expuesto: 100%')
            if blurred == 'VERY_LIKELY':
                print('\n', 'Borroso: 100%')
            if headwear == 'VERY_LIKELY':
                print('\n', 'Gorro/Sombrero/Beanie: 100%')

            if joy == 'LIKELY':
                print('\n', 'Alegría: 75%')
            if sorrow == 'LIKELY':
                print('\n', 'Tristeza: 75%')
            if anger == 'LIKELY':
                print('\n', 'Enojo: 75%')
            if surprise == 'LIKELY':
                print('\n', 'Sorpresa: 75%')
            if under_exposed == 'LIKELY':
                print('\n', 'Sobre expuesto: 75%')
            if blurred == 'LIKELY':
                print('\n', 'Borroso: 75%')
            if headwear == 'LIKELY':
                print('\n', 'Gorro/Sombrero/Beanie: 75%')

            if joy == 'POSSIBLE':
                print('\n', 'Alegría:50%')
            if sorrow == 'POSSIBLE':
                print('\n', 'Tristeza: 50%')
            if anger == 'POSSIBLE':
                print('\n', 'Enojo: 50%')
            if surprise == 'POSSIBLE':
                print('\n', 'Sorpresa: 50%')
            if under_exposed == 'POSSIBLE':
                print('\n', 'Sobre expuesto: 50%')
            if blurred == 'POSSIBLE':
                print('\n', 'Borroso: 50%')
            if headwear == 'POSSIBLE':
                print('\n', 'Gorro/Sombrero/Beanie: 50%')

            if joy == 'UNLIKELY':
                print('\n', 'Alegría:25%')
            if sorrow == 'UNLIKELY':
                print('\n', 'Tristeza: 25%')
            if anger == 'UNLIKELY':
                print('\n', 'Enojo: 25%')
            if surprise == 'UNLIKELY':
                print('\n', 'Sorpresa: 25%')
            if under_exposed == 'UNLIKELY':
                print('\n', 'Sobre expuesto: 25%')
            if blurred == 'UNLIKELY':
                print('\n', 'Borroso: 25%')
            if headwear == 'UNLIKELY':
                print('\n', 'Gorro/Sombrero/Beanie: 25%')

            if joy == 'VERY_UNLIKELY':
                print('\n', 'Alegría:0%')
            if sorrow == 'VERY_UNLIKELY':
                print('\n', 'Tristeza: 0%')
            if anger == 'VERY_UNLIKELY':
                print('\n', 'Enojo: 0%')
            if surprise == 'VERY_UNLIKELY':
                print('\n', 'Sorpresa: 0%')
            if under_exposed == 'VERY_UNLIKELY':
                print('\n', 'Sobre expuesto: 0%')
            if blurred == 'VERY_UNLIKELY':
                print('\n', 'Borroso: 0%')
            if headwear == 'VERY_UNLIKELY':
                print('\n', 'Gorro/Sombrero/Beanie: 0%')

            print('-----------------------------------')
    return


datos = leer_web('http://leoviquez.synology.me/VisionAPI/index.py?id=17')
estadisticas_de_reconocimientos(datos)

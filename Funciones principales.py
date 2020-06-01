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
    for x in variable:
        # Desenpaca listas y diccionarios para agarrar el porcentaje de cada emocion
        rostros = x.get('rostros')
        expresion_rostro=rostros[0].get('face_expressions')
        joy=expresion_rostro.get('joy_likelihood')
        sorrow = expresion_rostro.get('sorrow_likelihood')
        anger = expresion_rostro.get('anger_likelihood')
        surprise = expresion_rostro.get('surprise_likelihood')
        under_exposed=expresion_rostro.get('under_exposed_likelihood')
        blurred=expresion_rostro.get('blurred_likelihood')
        headwear=expresion_rostro.get('headwear_likelihood')

        # Imprimir de mayor a menor las emociones y estados de las fotos
        if joy == 'VERY_LIKELY':
            print('\n','Alegría: 100%')
        if sorrow == 'VERY_LIKELY':
            print('\n','Tristeza: 100%')
        if anger == 'VERY_LIKELY':
            print('\n','Enojo: 100%')
        if surprise == 'VERY_LIKELY':
            print('\n','Sorpresa: 100%')
            
datos = leer_web('http://leoviquez.synology.me/VisionAPI/index.py?id=17')
estadisticas_de_reconocimientos(datos)

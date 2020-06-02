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


def ver_datos(datos1):
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
                    basura = cursos.pop(y)
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


datos1 = leer_web('http://leoviquez.synology.me/VisionAPI/cursos.py')
datos2 = leer_web('http://leoviquez.synology.me/VisionAPI/cursos.py?id=6')
datos3 = leer_web('http://leoviquez.synology.me/VisionAPI/index.py?id=17')
ver_datos(datos1)

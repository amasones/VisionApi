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


selector_id(6)

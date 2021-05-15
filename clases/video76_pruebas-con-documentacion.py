import doctest


def areaTriangulo(base, altura):
    """
    TEST
    Calcular el area de un triangulo dado
    >>> areaTriangulo(3, 6)
    'El area es: 9.0'
    >>> areaTriangulo(9, 9)
    'El area es: 40.5'
    """

    return f"El area es: {(base * altura) / 2}"


def compruebaMail(mailUsuario):
    """
    La funcion compruebaMail evalua un mail
    recibido en busca de la @. Si tiene una @
    es correcto, si tiene más de una @ es incorrecto
    si la @ está la final es incorrecto

    >>> compruebaMail('jorge@email.com')
    True

    >>> compruebaMail('jorgeemail.com@')
    False

    >>> compruebaMail('jorgeemail.com')
    False

    >>> compruebaMail('jorgeemail@.com')
    False
    """
    arroba = mailUsuario.count('@')

    if arroba != 1 or mailUsuario.rfind('@') == len(mailUsuario) - 1 or mailUsuario.find('@') == 0:
        return False
    else:
        return True

doctest.testmod()

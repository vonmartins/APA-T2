"""
Módulo que define funciones con números primos

Martí Domínguez Rivero

>>> esPrimo(4)
False

>>> esPrimo(13)
True

>>> esPrimo(-4)
False

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Devuelve True si el número es primo, False en caso contrario.

    >>> esPrimo(4)
    False
    >>> esPrimo(13)
    True
    >>> esPrimo(-4)
    False

    """
    if numero < 2:
        return False
    for prova in range(2, numero): # El final es el postúltimo
        if numero % prova == 0 : 
            return False

    return True 

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos del número.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(90, 14)
    630

    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_unicos = set(factores1) | set(factores2) # Encontramos los factores únicos y los juntamos
    mcm = 1
    for factor in factores_unicos:
        mcm *= factor ** max(factores1.count(factor), factores2.count(factor)) # Para cada factor único, tomamos el máximo número de veces que aparece
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12

    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) & set(factores2) # Encontramos los factores únicos y juntamos con AND
    mcd = 1
    for factor in factores_comunes:
        mcd *= factor ** min(factores1.count(factor), factores2.count(factor)) # Para cada factor tomamos el MÍNIMO número de veces que aparece
    return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcmN(42, 60, 70, 63)
    1260

    """
    from functools import reduce # Con ayuda de internet e IA 
    return reduce(mcm, numeros)

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210

    """
    from functools import reduce # Con ayuda de internet e IA 
    return reduce(mcd, numeros)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

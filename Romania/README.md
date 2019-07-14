# 🇷🇴 Romania

El sistema de encriptación RSA, como parte de la fase de generación de claves públicas y privadas, debe generar dos números primos grandes p y q y un número n = p*q que se usará luego para encriptar y desencriptar mensajes (ver https://simple.wikipedia.org/wiki/RSA_algorithm)

Una reconocida empresa de Palermagro decidió realizar su propia implementación de este sistema. Decidieron generar los primos p y q con dos algoritmos diferentes pensando que así obtendrían mayor seguridad.

La ingeniera Melanie S. implementó la siguiente función:

```
def generate_p():
    '''
    algoritmo eficiente, seguro y testeado para generar primos grandes
    '''
    ...
    ...
    return p
```

El ingeniero N. Álvarez, sin muchas ganas de programar, decidió tomar un atajo y programar lo siguiente:

```
def generate_q():
    '''
    genera un primo
    '''
    return 1094782941871623486260250734009229761
```

Has tenido acceso a uno de los mensajes encriptados así como también a un PEM que contiene la clave pública de encriptación. ¿Sos capaz de descubrir el contenido del mensaje original?

https://s3.amazonaws.com/it.challenge.18/problem20.zip

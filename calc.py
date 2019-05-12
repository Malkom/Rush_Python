#!/usr/bin/env python3


from math import *


class Calculate:
    """
    Cette classe implément toutes les méthodes de calcul
    """
    def add(a, b):
        """
        Additionne 2 nombres et retourne le résultat
        """
        return a + b

    def subtract(a, b):
        """
        Soustrait 2 nombres et retourne le résultat
        """
        return a - b

    def multiply(a, b):
        """
        Multiplie 2 nombres et retourne le résultat
        """
        return a * b

    def divide(a, b):
        """
        Divise 2 nombres et retourne le résultat
        """
        return a / b

    def lognep(a):
        """
        Calcule le logarithme népérien d'un nombre et retourne le résultat
        """
        return log10(a)

    def exp(a):
        """
        Calcule l'exponentiel d'un nombre et retourne le résultat
        """
        return exp(a)

    def cos(a):
        """
         Calcule le cosinus d'un nombre et retourne le résultat
         """
        return cos(a)

    def sin(a):
        """
         Calcule le sinus d'un nombre et retourne le résultat
         """
        return sin(a)

    def tan(a):
        """
         Calcule la tangente d'un nombre et retourne le résultatn:
         """
        return tan(a)

    def acos(a):
        """
         Calcule l'arcosinus d'un nombre et retourne le résultat
         """
        return acos(a)

    def asin(a):
        """
         Calcule l'arcsinus d'un nombre et retourne le résultat

         :param a:
         :return:
         """
        return asin(a)

    def atan(a):
        """
         Calcule l'artangente d'un nombre et retourne le résultat
         """
        return atan(a)

    def degrees(a):
        """
         Convertit en degrée un nombre en radian et retourne le résultat:
         """
        return degrees(a)

    def radians(a):
        """
         Convertit en radian un nombre en degrée et retourne le résultat
         """
        return radians(a)

    def pi():
        """
        Retourne la constante Pi
        """
        return pi

    def e():
        """
        Retourne la constante e
        """
        return e

    def pow(a, b):
        """
        Elève le nombre 'a' à la puissance 'b' et retourne le résultat
        """
        return pow(a, b)

    def square(a):
        """
        Elève un nombre au carré et retourne le résultat
        """
        return sqrt(a)

    def fact(a):
        """
        Calcule le factoriel d'un nombre et retourne le résultat
        """
        return factorial(a)

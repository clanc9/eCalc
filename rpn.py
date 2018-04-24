from constants import *
from math import cos, tan, sin, floor, factorial, sqrt, log, log10

class Rpn:
    """Manipulation de formule en notation polonaise inversée

    Calculer le résultat d'une formule mathématique
    en notation polonaire inversée (reverse Polish notation ou rpn en anglais).
    """
    def __init__(self, formulaRpn):
        self.formulaRpn = formulaRpn

    def calcRpn(self):
        """Effectue calcul à partir d'une formule npi (rpn)

        Fonction qui calcule le résultat d'une formule mathématique en notation polonaise
        inversée. Cherche d'abord l'opérateur puis désempile les 1 ou 2 opérandes
        qui le précèdent. Réanalyse la formule résultante (après pop) jusqu'à ce
        qu'il ne reste qu'une seule valeur.
        """
        formulaRpn = self.formulaRpn
        while (len(formulaRpn) > 1):
            i = 0
            for v in formulaRpn:
                if str(v) in BINARY_OPERATORS and i < 2:
                    a = formulaRpn[i-1]
                    if v == "+":
                        ret = a
                    elif v == "-":
                        ret = -a
                    else:
                        return "Erreur : formule erronée"
                    formulaRpn.pop(i-1)
                    formulaRpn[i-1] = ret
                    break
                elif str(v) in BINARY_OPERATORS and i > 1:
                    a = formulaRpn[i-2]
                    b = formulaRpn[i-1]
                    if v == "+":
                        ret = a + b
                    elif v == "-":
                        ret = a - b
                    elif v == "x":
                        ret = a * b
                    elif v == "/":
                        try:
                            ret = a / b
                        except ZeroDivisionError:
                            return "Erreur : divison par zéro"
                    elif v == "mod":
                        try:
                            ret = a % b
                        except ZeroDivisionError:
                            return "Erreur : divison par zéro"
                    elif v == "^":
                        try:
                            ret = a ** b
                        except ValueError:
                            return "Erreur : opération impossible"
                    formulaRpn.pop(i-2)
                    formulaRpn.pop(i-2)
                    formulaRpn[i-2] = ret
                    break
                elif str(v) in UNARY_OPERATORS:
                    a = formulaRpn[i-1]
                    if v == "sqr":
                        if a >= 0:
                            ret = sqrt(a)
                        else:
                            return "Erreur : racine carrée de nombre négatif"
                    if v == "cos":
                        ret = cos(a)
                    if v == "sin":
                        ret = sin(a)
                    if v == "tan":
                        ret = tan(a)
                    if v == "ln":
                        try:
                            ret = log(a)
                        except ValueError:
                            return "Erreur : opération impossible"
                    if v == "log":
                        try:
                            ret = log10(a)
                        except ValueError:
                            return "Erreur : opération impossible"
                    if v == "!":
                        try:
                            ret = factorial(a)
                        except ValueError:
                            return "Erreur : fonction factorielle non permise"
                    formulaRpn.pop(i-1)
                    formulaRpn[i-1] = ret
                    break
                else:
                    i += 1
        ## fin de la boucle while
        result = formulaRpn[0]
        if type(result) == str:
            return "Erreur : expression erronée"
        elif result == 0.0:
            return 0
        elif result >-1 and result < 1:
            return result
        else:
            if floor(result) == result:
                return int(result)
            else:
                return result

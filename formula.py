import re
from constants import *

class Formula:
    """Manipulation et transformation de formules mathématiques complexes

    Stocke les formules suivantes:
        :formule initiale (variable .formula),
        :formule sous forme de liste d'opérandes et d'opérateurs (variable .formulaInfix)
        :formule en notation polonaise inversée (sigle anglais Rpn, variable .formulaRpn)
    """
    def __init__(self, string):
        self.formula = string
        self.formulaInfix = []
        self.formulaRpn = []

    def formatAndValidate(self):
        """Validation d'une formule sous forme de chaîne de caractères

        Vérifie que le nombre de parenthèses ouvertes est égal à celui
        des parenthèses fermées. Si oui, retourne une chaîne où les
        espaces ont été enlevées et où les virgules ont été remplacées par des points.
        """
        f1 = self.formula
        if (f1.count('(') != f1.count(')')):
            self.formula = False
        else:
            self.formula = f1.replace(',', '.').replace(' ','')

    def strFormulaToList(self):
        """Extraction des opérandes et des opérateurs

        Extrait les nombres et les opérateurs de la formule.
        Transforme les nombres-string en nombres décimaux.
        Retourne une liste comportant les opérandes
        ainsi que les opérateurs et les parenthèses.
        Place le tout dans une liste et la renvoie.
        """
        sep_re = re.compile(r'\s*(%s|%s|%s|%s|%s|%s|%s|%s|%s|%s)\s*' % (
                    re.escape(LEFT_PAR),
                    re.escape(RIGHT_PAR),
                    re.escape("+"),
                    re.escape("-"),
                    re.escape("x"),
                    re.escape("/"),
                    re.escape("!"),
                    re.escape("mod"),
                    re.escape("^"),
                    re.escape("e"),
                    ))
        f = [ v.strip() for v in sep_re.split(self.formula.strip()) if v ]
        l = [ self.transformToFloatIfNumber(t) for t in f  ]
        i = 0
        a = len(l)

        # simplifies the cases where a plus or minus sign is in front of a number
        # by replacing the two list entries with a single one
        while (i < a):
            if l[i] == "-":
                if type(l[i-1]) != float and l[i-1] != RIGHT_PAR:
                    l.pop(i)
                    x = l[i]
                    l[i] = -x
                    a -= 1
            elif l[i] == "+":
                if type(l[i-1]) != float and l[i-1] != RIGHT_PAR:
                    l.pop(i)
                    a -= 1
            elif l[i] == "e":
                s = str(l[i-1]) + "e"
                if l[i+1] == "-" or l[i+1] == "+":
                    s = s + l[i+1]
                    l.pop(i+1)
                    a -= 1
                s = s + str(int(l[i+1]))
                l[i-1] = float(s)
                l.pop(i)
                l.pop(i)
                a -= 2
            i += 1
        self.formulaInfix = l

    def transformToFloatIfNumber(self, v):
        try:
            return float(v)
        except ValueError:
            return v

    def inToPost(self):
        """Transformation de formule mathématique

        À partir de la notation standard (liste d'opérateurs et de nombres),
        construction d'une formule en notation polonaise inversée (NPI, ou RPN en anglais).
        Modèle sur https://stackoverflow.com/questions/42703422/infix-to-postfix-algorithm-in-python
        """
        stack = []
        post = []
        for v in self.formulaInfix:
            if type(v) == float:
                #append numbers to formula
                post.append(v)
            else:
                if v == LEFT_PAR:
                    stack.append(v)
                elif v == RIGHT_PAR:
                    operator = stack.pop()
                    while operator != LEFT_PAR:
                        post.append(operator)
                        operator = stack.pop()
                else:
                    while (len(stack) != 0) and self.lowerPriority(v, stack):
                        post.append(stack.pop())
                    #append operators to formula
                    stack.append(v)
        while (len(stack) != 0):
            post.append(stack.pop())
        self.formulaRpn = post

    def lowerPriority(self, v, stackoperators):
        """Détermine la priorité des opérateurs mathématiques

        Consulte le dictionnaire constant PRIORITY pour établir
        la priorité des opérateurs arithmétiques placés dans la pile
        (de 0=parenthèse gauche à 4 pour opérations unaires).
        """
        if v in UNARY_OPERATORS:
            return False
        top = stackoperators.copy().pop()
        if PRIORITY[v] < PRIORITY[top]:
            return True
        else:
            return False

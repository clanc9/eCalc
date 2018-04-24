import tkinter as tk
import rpn
import formula
from constants import *

class GuiCalculator(tk.Frame):
    """Interface graphique pour une calculatrice

    Définit les cadres d'affichages, les boutons pour les touches
    ainsi que les fonctions associées.  Contient la fonction
    de calcul, qui fait appel aux objets Formula et Rpn.
    """
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #tk.Frame.pack(self)
        self.focus_set()
        self.bind("<Key>", self.keyboard)
        self.pack()
        self.formulaStr = tk.StringVar(self)
        self.formulaStr.set("")
        self.errorMsg = tk.StringVar(self)
        self.errorMsg.set("")
        self.resultDisplayed = False
        self.frameTop = tk.Frame(parent).pack(padx=2, pady=2)
        self.frameBtns = tk.Frame(parent)
        self.create_widgets()
        self.createButtons()

    def create_widgets(self):
        """Créer les cadres pour l'affichage de la formule et
        des messages d'erreur.
        """
        self.entry = tk.Label(self.frameTop)
        self.entry["textvariable"] = self.formulaStr
        self.entry["background"] = "white"
        self.entry["font"] = "Arial 18"
        self.entry["foreground"] = "black"
        self.entry["width"] = 400
        self.entry["height"] = 2
        self.entry["padx"] = 15
        self.entry["anchor"] = tk.E
        self.errorBox = tk.Label(self.frameTop)
        self.errorBox["textvariable"] = self.errorMsg
        self.errorBox["background"] = self["background"]
        self.errorBox["font"] = "Arial 12"
        self.errorBox["foreground"] = "white"
        self.errorBox["width"] = 400
        self.errorBox.pack(padx=5, pady=2)
        self.entry.pack(padx=5, pady=2)

    def clearErrorMessage(self):
        """Efface le message d'erreur
        """
        if self.errorMsg != "":
            self.errorMsg.set("")
            self.errorBox["background"] = self["background"]

    def createButtons(self):
        """Crée les touches de la calculatrice
        """
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="sin", command=lambda: self.btn("sin(")).grid(row=1, column=1)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="log", command=lambda: self.btn("log(")).grid(row=1, column=2)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="(", command=lambda: self.btn("(")).grid(row=1, column=3)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text=",", command=lambda: self.btn(",")).grid(row=1, column=4)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text=")", command=lambda: self.btn(")")).grid(row=1, column=5)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="+", command=lambda: self.btn(" + ")).grid(row=1, column=6)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="C", command=lambda: self.clear()).grid(row=1, column=7)

        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="cos", command=lambda: self.btn("cos(")).grid(row=2, column=1)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="ln", command=lambda: self.btn("ln(")).grid(row=2, column=2)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="1", command=lambda: self.btn("1")).grid(row=2, column=3)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="2", command=lambda: self.btn("2")).grid(row=2, column=4)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="3", command=lambda: self.btn("3")).grid(row=2, column=5)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="-", command=lambda: self.btn(" - ")).grid(row=2, column=6)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="<-", command=lambda: self.back()).grid(row=2, column=7)

        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14",text="tan", command=lambda: self.btn("tan(")).grid(row=3, column=1)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14",text="x^y", command=lambda: self.btn("^")).grid(row=3, column=2)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold",text="4", command=lambda: self.btn("4")).grid(row=3, column=3)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold",text="5", command=lambda: self.btn("5")).grid(row=3, column=4)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold",text="6", command=lambda: self.btn("6")).grid(row=3, column=5)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14",text="x", command=lambda: self.btn(" x ")).grid(row=3, column=6)
        tk.Button(self.frameBtns, width=2, height=4, font="Arial 16 bold",text="=", command=lambda: self.calculate()).grid(row=3, column=7, rowspan=3)

        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="n!", command=lambda: self.btn("!")).grid(row=4, column=1)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="1/x", command=lambda: self.btnOneOver()).grid(row=4, column=2)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="7", command=lambda: self.btn("7")).grid(row=4, column=3)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="8", command=lambda: self.btn("8")).grid(row=4, column=4)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="/", command=lambda: self.btn(" / ")).grid(row=4, column=6)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="9", command=lambda: self.btn("9")).grid(row=4, column=5)

        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="sqr", command=lambda: self.btn("sqr(")).grid(row=5, column=1)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="x2", command=lambda: self.btnSquare()).grid(row=5, column=2)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", state=tk.DISABLED, text="").grid(row=5, column=3)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14 bold", text="0", command=lambda: self.btn("0")).grid(row=5, column=4)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", state=tk.DISABLED, text="").grid(row=5, column=5)
        tk.Button(self.frameBtns, width=2, height=1, font="Arial 14", text="mod", command=lambda: self.btn(" mod ")).grid(row=5, column=6)
        self.frameBtns.pack(padx=2, pady=5)

    def btn(self, char):
        """Evénement bouton

        Vérifie q-ue l'action est possible (dictionnaire ADD_RULES).
        Si oui, ajoute l'élément à la formule
        """
        if self.resultDisplayed:
            self.resultDisplayed = False
            if char in DIGITS or char == LEFT_PAR or char == RIGHT_PAR or char == ",":
                self.formulaStr.set("")
        old = self.formulaStr.get()
        x = char
        if char in DIGITS:
            x = "digit"
        if old[-1:] in ADD_RULES[x]:
            new = old + char
            self.formulaStr.set(new)
            self.clearErrorMessage()
            return
        if char[:-1] in UNARY_OPERATORS and char != "!":
            new = char + old + RIGHT_PAR
            self.formulaStr.set(new)
            self.clearErrorMessage()

    def btnOneOver(self):
        """Fonction inverse

        Crée l'inverse de la formule entrée.
        Place celle-ci entre parenthèses
        et la fait précéder de < 1 / >.
        """
        if self.resultDisplayed:
            self.resultDisplayed = False
        old = self.formulaStr.get()
        if old != "":
            if old.count("(") == old.count(")"):
                new = "1 / (" + old + ")"
                self.formulaStr.set(new)

                self.clearErrorMessage()

    def btnSquare(self):
        """Élévation d'un nombre au carré

        Affiche le carré de la formule entrée.
        """
        if self.resultDisplayed:
            self.resultDisplayed = False
        old = self.formulaStr.get()
        if old != "":
            if old.count("(") == old.count(")"):
                new = "(" + old + ")" + "^2"
                self.formulaStr.set(new)
                self.clearErrorMessage()
                self.calculate()

    def clear(self):
        """Efface la formule.
        """
        self.clearErrorMessage()
        self.formulaStr.set("")

    def back(self):
        """Retour en arrière dans la formule mathématique

        Efface le dernier caractère entré.
        S'il s'agit d'un opérateur unaire présentant une
        parenthèse ouverte, alors efface l'opérateur
        en entier (de 2 à 3 caractères.)
        """
        self.clearErrorMessage()
        if len(self.formulaStr.get()):
            old = self.formulaStr.get()
            if old[-1:] == RIGHT_PAR and old[0] == LEFT_PAR:
                self.formulaStr.set(old[1:-1])
                return
            elif old[-1:] == " ":
                self.formulaStr.set(old[:-3])
                return
            if old[-1:] == LEFT_PAR:
                if old[-1:-3] != "ln(":
                    n = 1
                else:
                    n = 0
                self.formulaStr.set(old[:-3-n])
                if old[-1:] == " ":
                    self.formulastr.set(old[:-1])
            else:
                self.formulaStr.set(old[:-1])

    def keyboard(self, event):
        key = event.keysym
        if key == "BackSpace":
            self.back()
        elif key == "Return" or key == "KP_Enter":
            self.calculate()
        elif key in DIGITS:
            self.btn(key)
        elif key in [ "KP_" + d for d in DIGITS]:
            self.btn(key[-1:])
        else:
            if key in KEYS:
                self.btn(KEYS[key])

    def calculate(self):
        """Calcul à partir d'une chaîne de caractères

        Effectue les opérations suivantes:
        1. crée un objet Formula à partir de l'entrée de l'utilisateur
        2. formatte et valide cette Formula
        3. extrait les opérateurs et les opérandes
        4. bâtit une formule en notation polonaise inversée
        5. crée un objet Rpn à l'aide de cette formule
        6. effectue le calcul
        7. affiche le résultat (ou le message d'erreur s'il y a lieu)
        """
        if not self.resultDisplayed and len(self.formulaStr.get()):
            x = formula.Formula(self.formulaStr.get())
            x.formatAndValidate()
            if (x.formula == False):
                result = "Erreur : parenthèses"
            else:
                x.strFormulaToList()
                x.inToPost()
                rpnObject = rpn.Rpn(x.formulaRpn)
                result = rpnObject.calcRpn()
                del rpnObject
            if type(result) == str:
                self.errorMsg.set(result)
                self.errorBox["background"] = "red"
            else:
                if type(result) == int:
                    if result == 0:
                        self.formulaStr.set("0")
                    elif abs(result) > 1e+08 or abs(result) < 1e-08:
                        self.formulaStr.set(format(result, ".4e"))
                    else:
                        self.formulaStr.set(str(result))
                else:
                    if abs(result) > 1e+08 or abs(result) < 1e-08:
                        s = format(result, ".4e")
                    else:
                        y = round(result, 10)
                        s = str(y)
                    self.formulaStr.set(s.replace(".", ","))
                self.resultDisplayed = True
            del x

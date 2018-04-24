#
# constantes utilisées par les objets Formula, Guicalc et Rpn
#
BINARY_OPERATORS = ["+","-","x","/", "mod", "^"]
UNARY_OPERATORS = ["sqr", "cos", "sin", "tan", "log", "ln", "!"]
DIGITS = "0123456789"
LEFT_PAR = "("
RIGHT_PAR = ")"
PRIORITY = { LEFT_PAR: 0, '+': 1, '-': 1, 'x': 2, '/': 2, 'mod': 2, '^': 3 , '!': 4, 'sqr':4, 'cos':4, 'sin':4, 'tan':4 }
ADD_RULES = { "digit" : [n for n in DIGITS ] + [LEFT_PAR, " ", "", ",", "^"],
              "," : [n for n in DIGITS],
              LEFT_PAR : [" ", "", LEFT_PAR],
              RIGHT_PAR : [n for n in DIGITS] + [RIGHT_PAR],
              " + " : [n for n in DIGITS] + [LEFT_PAR, RIGHT_PAR, "", "!"],
              " - " : [n for n in DIGITS] + [LEFT_PAR, RIGHT_PAR, "", "!"],
              " / " : [n for n in DIGITS] + [RIGHT_PAR, "!"],
              " x " : [n for n in DIGITS] + [RIGHT_PAR, "!"],
              " mod " : [n for n in DIGITS] + [RIGHT_PAR, "!"],
              "^" : [n for n in DIGITS] + [RIGHT_PAR, "!"],
              "sqr(" : [" ", "", LEFT_PAR ],
              "cos(" : [" ", "", LEFT_PAR ],
              "sin(" : [" ", "", LEFT_PAR ],
              "tan(" : [" ", "", LEFT_PAR ],
              "log(" : [" ", "", LEFT_PAR ],
              "ln(" : [" ", "", LEFT_PAR ],
              "!" : [n for n in DIGITS] + [RIGHT_PAR],
              }
KEYS = { "minus" : " - ",
         "plus" : " + ",
         "asterisk" : " x ",
         "x" : " x ",
         "comma" : ",",
         "exclam" : "!",
         "parenleft" :  LEFT_PAR,
         "parenright" : RIGHT_PAR,
         #keyboard pad KP_
         "KP_Add" : " + ",
         "KP_Subtract" : " - ",
         "KP_Divide" : " / ",
         "KP_Multiply" : " x ",
         }

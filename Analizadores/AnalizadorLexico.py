import ply.lex as lex

tokens = (
    'palabraReservada',
    'numero',
    'ID',
    'suma',
    'resta',
    'division',
    'multiplicacion',
    'coma',
    'puntoYComa',
    'parentesis',
    'comparador',
    'asignacion',
    'operadorLogico', 
    'corchete',
    'paso',
        
)

#Expresiones regulares de reconocimiento

t_palabraReservada = r'int|bool|string|double|if|while|for|void'
def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t
t_ID = r'[a-zA-Z0-9]+'
t_suma = r'\+'
t_resta = r'-'
t_multiplicacion = r'\*'
t_division = r'/'
t_puntoYComa = r';'
t_coma = r','
t_parentesis = r'[()]'
t_comparador = r'\=\=|\!\=|\<\=|\>\=|\>|\<'
t_asignacion = r'\='
t_operadorLogico = r'&&|&|\|\||\|'
t_corchete = r'[{}]'
t_paso = r'\+\+|\-\-'




#Caracteres ignorados
t_ignore = ' \t'

#Manejo de errores
def t_error(t):
    print("Token desconocido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
'''
data = 'int 3+4 Red1, Black12 (Green) != 0 || <= 10 texto while'

lexer.input(data)
while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)
   '''
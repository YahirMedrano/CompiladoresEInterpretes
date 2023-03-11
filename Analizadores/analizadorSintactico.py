import ply.yacc as yacc
from AnalizadorLexico import tokens

'''
expresion : expresion + termino |
            expresion - termino |
            termino
            
termino : factor |         
          
factor : NUMERO
'''

def p_expresion_suma(p):
    'expresion : termino suma termino'
    p[0] = p[1] + p[3]
    print('Expresion SUMA escrita de manera correcta.')

def p_expresion_resta(p):
    'expresion : termino resta termino'
    p[0] = p[1] - p[3]
    print('Expresion RESTA escrita de manera correcta.')
    
def p_expresion_multiplicacion(p):
    'expresion : termino multiplicacion termino'
    p[0] = p[1] * p[3]
    print('Expresion MULTIPLICACION escrita de manera correcta.')
    
def p_expresion_division(p):
    'expresion : termino division termino'
    p[0] = p[1] / p[3]
    print('Expresion DIVISION escrita de manera correcta.')
    
def p_expresion_funcion(p):
    'expresion : palabraReservada ID'
    p[0] = p[1]
    print('Expresion FUNCION escrita de manera correcta.')

def p_exp_Ini(p):
    'expresion : palabraReservada ID ini'
    p[0] = p[1], p[2], p[3]
    print('Expresion Inicializacion escrita de manera correcta.')  
    
def p_expesion_coma(p):
    'expresion : coma'
    p[0] = p[1]
    print('Expresion Coma escrita de manera correcta.')
     
def p_expesion_puntoYComa(p):
    'expresion : puntoYComa'
    p[0] = p[1]
    print('Expresion Punto Y Coma escrita de manera correcta.')
    
def p_expesion_parentesis(p):
    'expresion : parentesis'
    p[0] = p[1]
    print('Expresion Parentesis escrita de manera correcta.')
    
def p_expesion_comparador(p):
    'expresion : comparador'
    p[0] = p[1]
    print('Expresion Comparador escrita de manera correcta.')
    
def p_expesion_operadorLogico(p):
    'expresion : operadorLogico'
    p[0] = p[1]
    print('Expresion Operador Logico escrita de manera correcta.')   
    
def p_expresion_ciclo(p):
    'expresion : palabraReservada condicion corchete corchete'
    p[0] = p[1], p[2], p[3], p[4]
    print('Expresion CICLO escrita de manera correcta.') 
    
def p_ini(p):
    'ini : asignacion termino'
    p[0] = p[1], p[2] 
    
def p_condicion_while(p):
    'condicion : parentesis ID comparador termino parentesis'
    p[0] = p[1], p[2], p[3], p[4], p[5]
    
def p_condicion_for(p):
    'condicion : parentesis palabraReservada ID asignacion termino puntoYComa ID comparador termino puntoYComa ID asignacion ID paso parentesis'   
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15]
    
def p_termino_id(p):
    'termino : ID'
    p[0] = p[1]  

def p_termino_numero(p):
    'termino : numero'
    p[0] = p[1]
    
def p_error(p):
    print('Error de sintaxis!')
    
parser = yacc.yacc()

while(True):
    try: 
        entrada = input()
    except EOFError:
        break
    if entrada.__eq__('exit'): break
    if not entrada: continue
    
    resultado = parser.parse(entrada)
    print("Resultado = " + (str)(resultado))

import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'DO', 'WHILE', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'INT', 'IDENTIFIER', 'PRINT',
    'PLUS', 'MINUS', 'MUL', 'DIV', 'RETURN', 'EQUALS',
    'LT', 'GT', 'EQUALEQUAL', 'NOTEQUAL',
    'LTEQUAL', 'GTEQUAL',
)


t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_ignore = ' \t'
t_EQUALEQUAL = r'=='
t_NOTEQUAL = r'!='
t_LT = r'\<'
t_GT = r'\>'
t_EQUALS = r'\='
t_LTEQUAL=r'\<\='
t_GTEQUAL=r'\>\='

def t_PRINT(t):
    r'println|print'
    return t

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_INT(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_program(p):
    '''program : do_while_statements'''
    p[0]="function syntax is valid"

def p_do_while_statements(p):
    '''do_while_statements : do_while_statements do_while_statement
                                        | do_while_statement'''

def p_do_while_statement(p):
    '''do_while_statement : DO LBRACE statements RBRACE WHILE LPAREN conditions RPAREN SEMICOLON'''
    
def p_statements(p):
    '''statements : statements statement
                  | statement
                  | return_statement
                  | empty'''

def p_statement(p):
    '''statement : assignment SEMICOLON
                 | print_statement SEMICOLON'''

def p_return_statement(p):
    '''return_statement : RETURN statement'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN''' 

def p_conditions(p):
    '''conditions : expression LT expression
                            | expression GT expression
                            | expression EQUALEQUAL expression
                            | expression NOTEQUAL expression
                            | expression LTEQUAL expression
                            | expression GTEQUAL expression'''

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''

def p_expression(p):
    '''expression : term
                  | expression signs term'''

def p_signs(p):
    '''signs : PLUS
                | MINUS
                | DIV
                | MUL'''

def p_term(p):
    '''term : INT
            | IDENTIFIER'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value '{p.value}'")
    else:
        print("Syntax error at the end of input!")

parser = yacc.yacc()

def check(input_code):
    res=None
    try:
        res=parser.parse(input_code)
    except Exception as e:
        print(f"Error: {e}")
    return res

input_code = '''
do {
x = x + 1;
}
whil (x <= 10);
'''

result=check(input_code)
if result:
    print(result)

import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'DEF', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'INT', 'COLON', 'COMMA', 'EQUALS', 'PRINT',
    'PLUS', 'MINUS', 'DIV', 'MUL', 
    'SEMICOLON', 'RETURN',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_SEMICOLON = r';'


def t_RETURN(t):
    r'return'
    return t

t_ignore = ' \t'

def t_DEF(t):
    r'def'
    return t

def t_PRINT(t):
    r'println'
    return t

def t_INT(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Lexer rule for 'IDENTIFIER' (variable/function names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Newline rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_program(p):
    '''program : functions'''
    p[0]="function syntax is valid"

def p_functions(p):
    '''functions : functions function
                 | function'''

def p_function(p):
    '''function : DEF IDENTIFIER LPAREN params RPAREN COLON type EQUALS LBRACE statements RBRACE'''
    
def p_params(p):
    '''params : params COMMA param
                | param
                | empty'''

def p_param(p):
    '''param : IDENTIFIER COLON type'''

def p_type(p):
    '''type : INT
                | IDENTIFIER''' #for user-defined data types
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement'''

def p_statement(p):
    '''statement : assignment SEMICOLON
                  | print_statement SEMICOLON
                  | return_statement SEMICOLON'''

def p_return_statement(p):
    '''return_statement : RETURN expression'''

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''

def p_expression(p):
    '''expression : term
                  | expression signs term
                  '''

def p_term(p):
    '''term : IDENTIFIER'''

def p_signs(p):
    '''signs : PLUS
                | MINUS
                | DIV
                | MUL'''

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''

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
        printf(f"Error: {e}")
    return res

# Example input
input_code = '''
def add(x: Int, y: Int): Int = {
  printn(x + y);
  return x + y;
}
'''

result=check(input_code)
if result:
    print(result);

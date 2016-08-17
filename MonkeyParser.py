from ply import *
import MonkeyLex

tokens = MonkeyLex.tokens

def p_program(p):
    '''program  : program actions
                | actions
    '''
    if len(p) == 2 and p[1]:
        p[0] = {}
        line,act = p[1]
        p[0][line] = act
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            for act_obj in p[2]:
                line, act = act_obj
                p[0][line] = act

def p_program_error(p):
    '''program : error '''
    p[0] = None
    p.parser.error = 1

def p_actions(p):
    '''actions   : actions action
                | action
    '''
    if len(p) = 2:
        if not p[0]:
            p[0] = []
        p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        p[0].append(p[2])

def p_action(p):
    '''action   : movement target BOOL
                | movement target
                | movement STRING BOOL
                | movement STRING
    '''
    pass
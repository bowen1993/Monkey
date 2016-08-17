from ply import *

keywords = (
    'Perfer', 'Patient', 'Visit', 'Blind', 'Click', 'Input', 'Choose',
    'Back', 'Forward', 'Accept', 'Auth', 'Dismiss', 'Press', 'Switch',
    'Repeat', 'Task', 'End', 'Judge', 'Empty', 'Not'
)

tokens = keywords + (
    'ID', 'NUMBER', 'STRING', 'BOOL', 'EQUAL'
)

t_ignore = '\t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t;

def t_NUMBER(t):
    r"""(\d+(\.\d*)?|\.\d+)([eE][-+]? \d+)?"""
    t.value = float(t.value)
    return t

t_STRING = r'\".*?\"'
t_BOOL = r'(true)|(false)'
t_EQUAL = r'='
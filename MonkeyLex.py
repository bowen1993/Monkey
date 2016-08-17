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


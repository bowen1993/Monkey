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

def p_action_target(p):
    '''action   : movement target BOOL NEWLINE
                | movement target NEWLINE
    '''
    if not p[1][0]:
        print("%s At Line %d", (p[1][1], p.lineno(1)))
        p[0] = None
        p.parser.error = 1
    else:
        lineno = p.lineno(0)
        action_dict = {
            'move':p[1][1],
            'target':p[2],
            'is_wait': True if p[3] else False,
            'type':'target'
        }
        p[0] = (lineno, action_dict)

def p_action_command(p):
    '''
    action  : movement STRING NEWLINE
    '''
    if not p[1][0]:
        print("%s At Line %d", (p[1][1], p.lineno(1)))
        p[0] = None
        p.parser.error = 1
    else:
        lineno = p.lineno(0)
        action_dict = {
            'move': p[1][1],
            'value':p[2],
            'type':'command'
        }
        p[0] = (lineno, action_dict)

def p_action_empty(p):
    '''action  : NEWLINE
    '''
    p[0] = None

def p_action_bad(p):
    '''action   : error NEWLINE
    '''
    print("Wrong action at line %d" % p.lineno(0))
    p[0] = None
    p.parser.error = 1

def p_movement(p):
    '''movement : Perfer
                | Patient
                | Visit
                | Blind
                | Click
                | Input
                | Choose
                | Back
                | Forward
                | Accept
                | Auth
                | Dismiss
                | Press
                | Switch
    '''
    p[0] = (True, p[1])

def p_movement_bad(p):
    '''movement : error
    '''
    p[0] = (False, "Wrong movement setting")
    p.parser.error = 1

def p_compound_action(p):
    '''compound_action  : repeat_block
                        | task_block
    '''
    lineno = p.lineno(0)
    p[0] = (lineno, p[1])

def p_repeat_block(p):
    '''repeat_block : Repeat NUMBER NEWLINE actions End NEWLINE
                    | Repeat NUMBER NEWLINE compound_action End NEWLINE
    '''
    pass

def p_task_block(p):
    '''task_block   : Task NEWLINE actions End
                    | Task NEWLINE compound_action End
    '''
    pass

#TODO: Judge action
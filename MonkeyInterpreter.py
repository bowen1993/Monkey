from CodeGenerator import *
class MonkeyInterpreter:
    def __init__(self, prog, filename=""):
        self.prog = prog
        self.func_table = {}
        self.code_str = ''
        self.filename = filename
        self.url = ''
        self.driver = ''
        self.indent = 0
        self._code_init()
    
    def _code_init(self):
        self.code_str = """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
        """

    def save(self):
        if len(self.filename) > 0:
            code_file = open(self.filename, 'w')
            code_file.write(self.code_str)
            code_file.close()
            return (True, 'Success')
        else:
            return (False, 'No filename or empty filename')
    
    def curr_indent(self):
        return '    '*self.indent

    def translate(self):
        for action in self.prog:
            if action['type'] == 'auth':
                self.code_str += self.transAuth(action)
            elif 'single' in action['type']:
                self.code_str += self.transSingleAction(action)
            elif 'target' in action['type']:
                self.code_str += self.transTargetAction(action)
            elif 'command' in action['type']:
                self.code_str += self.transCommandAction(action)
            elif 'judge' in action['type']:
                self.code_str += self.transJudgeAction(action)
            elif 'repeat' in action['type']:
                self.code_str += self.transRepeat(action)
            elif 'task' in action['type']:
                self.code_str += self.transTask(action)
    
    def transAuth(self, action):
        username = action['username']
        password = action['password']
        return self.curr_indent() + "driver.switch_to.alert.authenticate('%s','%s')" % (username, password)
    
    def transSingleAction(self, action):
        move = action['move']
        is_success, stmt_str = globals()[move]()
        if is_success:
            return stmt_str
    
    def transTargetAction(self, action):
        move = action['move']
        args = {
            'target':action['target']
        }
        if 'value' in action:
            args['value'] = action['value']
        is_success, stmt_str = globals()[move](**args)
        if is_success:
            return stmt_str
    
    def transCommandAction(self, action):
        move = action['move']
        args = {
            'value':
        }
        is_success, stmt_str = globals()[move](**args)
        if is_success:
            return stmt_str
    
    def transJudgeAction(self, action):
        args = {
            'target':action['target'],
            'value':action['expect'],
            'is_equal' : action['is_equal']
        }
        is_success, stmt_str = Judge(**args)
        if is_success:
            return stmt_str
    
    def transRepeat(self, action):
        return ""
    
    def transTask(self, action):
        return ""
class MonkeyInterpreter:
    def __init__(self, prog, filename=""):
        self.prog = prog
        self.func_table = {}
        self.code_str = ''
        self.filename = filename

    def save(self):
        if len(self.filename) > 0:
            code_file = open(self.filename, 'w')
            code_file.write(self.code_str)
            code_file.close()
            return (True, 'Success')
        else:
            return (False, 'No filename or empty filename')
    
    def translate(self):
        pass
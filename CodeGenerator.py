def Prefer(value="PhantomJS"):
    return True, "driver = webdriver.%s()\n" % browser_value

def Patient(value=0):
    return True, ""

def Visit(value=""):
    if len(value) > 0:
        return True, "driver.get('%s')\n" % value
    else:
        return False, "Wrong URL"

def Blind(value=True):
    return True, ""

def judge_target(target):
    if '/' in target:
        return 'xpath'
    elif '#' in target or '.' in target: 
        return 'css'
    else:
        return 'element'

def get_find_stmt(target):
    find_stmt = ""
    find_type = judge_target(target)
    if find_type == 'xpath':
        find_stmt = "ele = driver.find_element_by_xpath('%s')\n" % target
    elif find_type == 'css':
        find_stmt = "ele = driver.find_element_by_css_selector('%s')\n" % target
    elif find_type == "element":
        find_stmt = "ele = driver.find_element_by_tag_name('%s')\n" % target
    return find_stmt

def Click(target=""):
    if len(target) > 0:
        find_stmt = get_find_stmt(target)
        return True, "%sele.click()" % find_stmt
    else:
        return False, "No target"

def Input(target="", value=""):
    if len(target) > 0:
        find_stmt = get_find_stmt(target)
        return True, "%sele.send_keys('%s')\n" % (find_stmt, value)
    else:
        return False, "No target"

def Choose(target="", value=""):
    return True, ""

def Back():
    return True, "driver.back()\n"

def Forward():
    return True, "driver.forward()\n"

def Switch(value=""):
    return True, "driver.switch_to.window('%s')\n" % value

def Judge(target="", value="", is_equal=True):
    if len(target) > 0:
        find_stmt = get_find_stmt(target)
        comp = "in" if is_equal else "not in"
        assert_str = "assert '%s' %s ele.text" % (value, comp)
        return True, "%s%s\n" % (find_stmt, assert_str)
    else:
        return False, "No target"
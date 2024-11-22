import re
from models import *

def find_extras(s):
    return re.findall(r'extras=\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', s, re.DOTALL)
def remove_charsequence(s):
    return re.sub(r'\n\s*\[', r'\n[', s)

def extras_to_dict(e):
    it = e.split('=')
    f = {}
    for i, (a, b) in enumerate(zip(it, it[1:])):
        aconv = lambda s: s.split(' ')[-1]
        bconv = lambda s: ' '.join(s.split(' ')[:-1])
        x, y = '', ''
        if i == 0:
            x, y = a.strip(), bconv(b)
        elif i == len(it)-2:
            x, y = aconv(a), b
        else:
            x, y = aconv(a), bconv(b)
        f[x]=remove_charsequence(y.strip())
    return f

def construct_char_sequence(a: str):
    s = a.strip()
    res = []
    number_re = r'^\[\d\] (.*)$'

    for m in s.split('\n')[1:]:
        r = re.search(number_re, m, re.DOTALL)
        if r: res.append(r.group(1))
        else: res[-1] += f'\n{m}'

    return res

def dumpsys_to_python(a: str):
    """convert a dumpsys type to python type"""
    s = a.strip()
    match_bool = re.search(r'^Boolean \((true|false)\)$', s)
    match_string = re.search(r'^String \((.*)\)$', s, re.DOTALL)
    match_applicationinfo = re.search(r'^ApplicationInfo \(ApplicationInfo{([a-z0-9]*) ([_\.a-zA-Z0-9]*)(?<= )?(.*)}\)$', s)
    match_int = re.search(r'^Integer \(([0-9])\)$', s)
    match_charsequence = re.search(r'^CharSequence\[\] \((\d*)\)$', s.split('\n')[0])
    match_null = s == 'null'

    if match_bool and match_bool.group(1) in ('false', 'true'):
        return match_bool.group(1) == 'true'
    elif match_string:
        return match_string.group(1)
    elif match_applicationinfo:
        return ApplicationInfo(match_applicationinfo.group(1), match_applicationinfo.group(2), match_applicationinfo.group(3) or None)
    elif match_int:
        return int(match_int.group(1))
    elif match_charsequence:
        return construct_char_sequence(a)
    elif match_null:
        return None
    return a

def convert_types(d:dict):
    new = {}
    for k, v in d.items():
        new[k]=dumpsys_to_python(v)
    return new

def todict(output: str):
    for e in find_extras(output):
        yield convert_types(extras_to_dict(e))



# User should use this:

def parse(output: str):
    return [Notification.from_parsed(d) for d in todict(output)]

def from_file(filename: str):
    content = ''
    with open(filename) as f:
        content = f.read()
    return parse(content)

def full_text(text: Optional[str], extra_lines: Optional[List[str]]) -> Optional[str]:
    # Convert text + extra lines to just text
    lines = [] if text == None or text.strip() == '' else [text]
    lines += [] if extra_lines == None else extra_lines
    res = '\n\n'.join(lines)
    return res if len(res) > 0 else None
from models import *
from parser import todict

def parse(output: str):
    return [Notification.from_parsed(d) for d in todict(output)]

def from_file(filename: str):
    content = ''
    with open(filename) as f:
        content = f.read()
    return parse(content)
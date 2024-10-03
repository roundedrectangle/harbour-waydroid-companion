import pyotherside as pyo
import subprocess as sp
import codecs

def get_dumpsys():
    proc = sp.run(['waydroid', 'shell'], input=b'dumpsys notification --noredact', capture_output=True)
    return proc.stdout.decode()
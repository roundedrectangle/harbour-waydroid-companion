from pyotherside import send as qsend
from typing import Optional
import subprocess as sp
#import codecs

# Runs CLI commands and returns the output (mostly)

def get_dumpsys(service: Optional[str]):
    return sp.run(['waydroid', 'shell'], input=f'dumpsys {service}'.encode(), capture_output=True).stdout.decode()

def get_status():
    return sp.run(['waydroid', 'status'], capture_output=True).stdout.decode()

def set_container(start: bool):
    return sp.run(['waydroid', 'container', 'start' if start else 'stop'], capture_output=True).stdout.decode()
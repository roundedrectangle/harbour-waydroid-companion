from pyotherside import send as qsend
from typing import Optional
import subprocess as sp
#import codecs

# Run some commands and return the output

def get_dumpsys(service: Optional[str]):
    proc = sp.run(['waydroid', 'shell'], input=f'dumpsys {service}'.encode(), capture_output=True)
    return proc.stdout.decode()

def get_status():
    result = sp.run(['waydroid', 'status'], capture_output=True).stdout.decode()
    return result
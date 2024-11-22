import re
from typing import Optional
import os

from models import RunStatus, Status

def get_value(out: str, key: str):
    match = re.search(rf'^{key}:\s*(.*)$', out, re.M)
    if match:
        return match.group(1)

# Runnables:
# Session: RUNNING or STOPPED
# Container: RUNNING or STOPPED but can be something else (?)

def run_status_conv(status: Optional[str]) -> Optional[RunStatus]:
    if status == None:
        return RunStatus()
    return RunStatus(status == 'RUNNING' or (False if status == 'STOPPED' else None), status) if status else None

def parse(status: str, rooted: Optional[bool]=None):
    return Status(
        rooted if rooted != None else os.getuid() == 0,
        *(run_status_conv(get_value(status, runnable)) for runnable in ('Session', 'Container')),
        *(get_value(status, seq) for seq in ('Vendor type', 'Session user', 'Wayland display', 'IP address'))
    )
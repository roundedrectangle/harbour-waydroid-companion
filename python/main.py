from typing import List, Optional
import pyotherside as pyo
import os
import subprocess as sp
from waydroid import get_dumpsys
from norifications import parse
import models

def full_text(text: Optional[str], extra_lines: Optional[List[str]]) -> Optional[str]:
    lines = [] if text != None and text.strip() == '' else [text]
    lines += [] if extra_lines == None else extra_lines
    res = '\n\n'.join(lines)
    return res if len(res) > 0 else None

class Communicator:
    rooted: bool = False
    def __init__(self) -> None:
        self.check_root()
        self.send_notifications()
    
    def check_root(self):
        self.rooted = os.getuid() == 0
        pyo.send('rooted', self.rooted)

    def send_notification(self, n: models.Notification):
        pyo.send('notification', n.package or '', n.title or '', n.summary or '', full_text(n.text, n.textLines) or '')
    
    def send_notifications(self):
        notifs = parse(get_dumpsys())
        for n in notifs:
            self.send_notification(n)

comm = Communicator()
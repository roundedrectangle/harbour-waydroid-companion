import logging
from typing import Union, Optional
from pyotherside import send as qsend
import os

import waydroid as wd
import notifications as notif
import status as st

class Communicator:
    status: st.Status

    def __init__(self) -> None:
        logging.basicConfig(level=logging.WARNING)
        self.reload_status()
    
    def reload_status(self):
        self.status = st.parse(wd.get_status())
        qsend('status', self.status.dict)
    
    def toggle_container(self):
        self.reload_status() # just to make sure
        out = wd.set_container(not self.status.container.state)
        self.reload_status()
        return out
        #qsend('container_result', out)
    
    def send_notifications(self):
        notifs = notif.parse(wd.get_dumpsys('notification --noredact'))
        for n in notifs:
            qsend('notification', n.package or '', n.title or '', n.summary or '', notif.full_text(n.text, n.textLines) or '')

comm = Communicator()
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum, auto

# Notifications

@dataclass
class Notification:
    package: str
    text: str
    title: str
    textLines: Optional[List[str]] = None
    summary: Optional[str] = None
    icon: Optional[str] = None

    @classmethod
    def from_parsed(cls, parsed: dict):
        return cls(
            parsed['android.appInfo'].name,
            parsed['android.text'],
            parsed['android.title'],
            parsed.get('android.textLines', None),
            parsed.get('android.summaryText', None)
        )

@dataclass
class ApplicationInfo:
    id: str
    name: str
    extra: Optional[str] = None

# Status

@dataclass
class RunStatus:
    state: Optional[bool] = None
    fallback_state: Optional[str] = None

    @property
    def dict(self):
        return {
            'state': self.state or False,
            'state2': int(self.state) if isinstance(self.state, bool) else -1,
            'full': self.fallback_state or ''
        }

@dataclass
class Status:
    rooted: bool
    session: RunStatus
    container: RunStatus
    vendor: Optional[str]
    user: Optional[str]
    display: Optional[str]
    ip: Optional[str]

    @property
    def dict(self):
        res = {}
        for attr in ('session','container'):
            res[attr] = getattr(self, attr).dict
        for attr in ('vendor','user','display','ip'):
            res[attr] = getattr(self, attr) or ''
        return res
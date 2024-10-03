from dataclasses import dataclass
from typing import Optional, List

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

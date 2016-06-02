from persistent import Persistent
from zope.component.factory import Factory
from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import ITeam

class SparcTeam(SparcEntity):
    implements(ITeam)
    
    def __init__(self, **kwargs):
        super(SparcTeam, self).__init__(**kwargs)
sparcTeamactory = Factory(SparcTeam)


class PersistentSparcTeam(SparcTeam, Persistent):
    """A Sparc Team that can be persisted in a ZODB"""
    implements(ITeam)
persistentSparcTeamFactory = Factory(PersistentSparcTeam)
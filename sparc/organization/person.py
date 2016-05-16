from persistent import Persistent
from zope.component.factory import Factory
from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import IPerson

class SparcPerson(SparcEntity):
    implements(IPerson)
    
    def __init__(self, **kwargs):
        super(SparcPerson, self).__init__(**kwargs)
sparcPersonFactory = Factory(SparcPerson)


class PersistentSparcPerson(SparcPerson, Persistent):
    """A Sparc Person that can be persisted in a ZODB"""
    implements(IPerson)
persistentSparcPersonFactory = Factory(PersistentSparcPerson)
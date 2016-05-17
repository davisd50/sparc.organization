from persistent import Persistent
from zope.component.factory import Factory
from zope.interface import implements
from sparc.entity import SparcEntity
from interfaces import ICompany

class SparcCompany(SparcEntity):
    implements(ICompany)
    
    def __init__(self, **kwargs):
        super(SparcCompany, self).__init__(**kwargs)
sparcCompanyFactory = Factory(SparcCompany)


class PersistentSparcCompany(SparcCompany, Persistent):
    """A Sparc Company that can be persisted in a ZODB"""
    implements(ICompany)
persistentSparcCompanyFactory = Factory(PersistentSparcCompany)
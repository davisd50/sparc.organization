from persistent import Persistent
from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from sparc.entity import SparcEntity
from interfaces import IContact

class SparcContact(SparcEntity):
    implements(IContact)
    
    def __init__(self, **kwargs):
        super(SparcContact, self).__init__(**kwargs)
        for field in ['email_addresses',
                      'phone_numbers',
                      'postal_addresses',
                      'companies']:
            if field in kwargs:
                setattr(self, field, kwargs[field])
    
    email_addresses = FieldProperty(IContact['email_addresses'])
    phone_numbers = FieldProperty(IContact['phone_numbers'])
    postal_addresses = FieldProperty(IContact['postal_addresses'])
    companies = FieldProperty(IContact['companies'])
    
sparcContactFactory = Factory(SparcContact)


class PersistentSparcContact(SparcContact, Persistent):
    """A Sparc Contact that can be persisted in a ZODB"""
    implements(IContact)
persistentSparcContactFactory = Factory(PersistentSparcContact)
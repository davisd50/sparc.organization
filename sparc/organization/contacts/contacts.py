from persistent import Persistent
from repoze.catalog.indexes.keyword import CatalogKeywordIndex
from repoze.catalog.indexes.text import CatalogTextIndex
from repoze.catalog.interfaces import ICatalog
from zope.component import createObject
from zope.interface import implementer
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface.exceptions import DoesNotImplement
from zope.schema.fieldproperty import FieldProperty
from sparc.catalog.repoze import IDocumentMap
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


# ICatalog for contacts
@implementer(ICatalog)
def contacts_catalog_factory_helper(doc_map=None):
    if not IDocumentMap.providedBy(doc_map):
        raise DoesNotImplement(IDocumentMap)
    # We need to add some indexes to the default IEntity ones that come with
    # sparc.catalog.repoze.entity_catalog.  These are helper functions to get the
    # strings that will be indexed.
    def list_attribute_entries(attr, object, default):
        return [a for a in (getattr(object, attr))] if hasattr(object, attr) else default
    def index_email_addresses(contact, default):
        return list_attribute_entries('email_addresses', contact, default)
    def index_phone_numbers(contact, default):
        return list_attribute_entries('phone_numbers', contact, default)
    def index_postal_addresses(contact, default):
        return list_attribute_entries('postal_addresses', contact, default)
    def index_email_domain(contact, default):
        domains = []
        if getattr(contact, 'email_addresses', None):
            domains = map(lambda e: e.partition('@')[2], contact.email_addresses)
        return domains if domains else default
    
    # Add IContact-secific indexes into catalog
    catalog = createObject(u"sparc.catalog.repoze.entity_catalog", 
                                                            doc_map=doc_map)
    catalog['email_addresses'] = CatalogKeywordIndex(index_email_addresses)
    catalog['email_addresses_text'] = CatalogTextIndex(index_email_addresses)
    catalog['phone_numbers'] = CatalogKeywordIndex(index_phone_numbers)
    catalog['phone_numbers_text'] = CatalogTextIndex(index_phone_numbers)
    catalog['postal_addresses_text'] = CatalogTextIndex(index_postal_addresses)
    # this one's specific to the IDirectory interface
    catalog['email_domain'] = CatalogKeywordIndex(index_email_domain)
    catalog['email_domain_text'] = CatalogTextIndex(index_email_domain)
    return catalog
contactsCatalogFactory = Factory(contacts_catalog_factory_helper)

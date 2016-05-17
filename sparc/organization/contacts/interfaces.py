from zope import schema
from zope.interface import Interface
from sparc.entity import IEntity
from sparc.organization import ICompany
from sparc.organization import IOrganizableEntity

class IAddress(IEntity):
    """A generic address"""
    address = schema.Text(
            title = u'Address',
            description = u'The entity address',
            )
    
class IEmailAddress(IAddress):
    """An email address (entity name identifies type...work, personal, etc)"""
    
class IPhoneNumber(IAddress):
    """A telephone number (entity name identifies type...work, personal, etc)"""
    
class IPostalAddress(IAddress):
    """A snail mail address location (entity name identifies type...work, personal, etc)"""

class IContact(IOrganizableEntity):
    """Contact information for an entity"""
    email_addresses = schema.List(
            title = u'Email Addresses',
            description = u'Email addresses for contact',
            value_type = schema.Field(
                    constraint = lambda v: IEmailAddress.providedBy(v)
                    )
            )
    phone_numbers = schema.List(
            title = u'Phone Numbers',
            description = u'Phone numbers for contact',
            value_type = schema.Field(
                    constraint = lambda v: IPhoneNumber.providedBy(v)
                    )
            )
    postal_addresses = schema.List(
            title = u'Postal Addresses',
            description = u'Postal addresses for contact',
            value_type = schema.Field(
                    constraint = lambda v: IPostalAddress.providedBy(v)
                    )
            )
    companies = schema.List(
            title = u'Associated Companies',
            description = u'Companies associated with contact',
            value_type = schema.Field(
                    constraint = lambda v: ICompany.providedBy(v)
                    )
            )

class IDirectoryLookup(Interface):
    """A lookup directory for a contact"""
    def __getitem__(id):
        """Return IContact for given id"""
    def __iter__():
        """Iterator of all readable & available contacts in directory"""
    def by_name(name):
        """Return iterable of contacts by exact name"""
    def search_name(name_re):
        """Return iterable of contacts matching regular expression"""
    def by_email(email):
        """Return iterable of contacts that have exact email address"""
    def search_email(email_re):
        """Return iterable of contacts matching regular expression"""

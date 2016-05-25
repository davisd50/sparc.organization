from zope import schema
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
            value_type = schema.TextLine(title=u'email')
            )
    phone_numbers = schema.List(
            title = u'Phone Numbers',
            description = u'Phone numbers for contact',
            value_type = schema.TextLine(title=u'phone')
            )
    postal_addresses = schema.List(
            title = u'Postal Addresses',
            description = u'Postal addresses for contact',
            value_type = schema.Text(title=u'address')
            )
    companies = schema.List(
            title = u'Associated Companies',
            description = u'Companies associated with contact',
            value_type = schema.Field(
                    constraint = lambda v: ICompany.providedBy(v)
                    )
            )

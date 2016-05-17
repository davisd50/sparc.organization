from sparc.entity import IEntity

class IOrganizableEntity(IEntity):
    """An entity that can be part of an organization"""

class IPerson(IOrganizableEntity):
    """A Person with a name and Id"""

class ICompany(IOrganizableEntity):
    """A Company with a name and Id"""
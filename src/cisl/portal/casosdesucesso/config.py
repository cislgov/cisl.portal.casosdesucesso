# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

PROJECTNAME = 'cisl.portal.casosdesucesso'


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'cisl.portal.casosdesucesso:uninstall',
            u'cisl.portal.casosdesucesso.upgrades.v1010:default'
        ]

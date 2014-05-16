# -*- coding: utf-8 -*-

from cisl.portal.casosdesucesso.interfaces import IExample
from five import grok
from plone.dexterity.content import Container


class Example(Container):
    """Exemplo de tipo de conteúdo."""

    grok.implements(IExample)
